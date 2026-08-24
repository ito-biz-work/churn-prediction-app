from aws_cdk import (
    RemovalPolicy,
    Stack,
    aws_ec2 as ec2,
    aws_ecr as ecr,
    aws_ecs as ecs,
    aws_elasticloadbalancingv2 as elb,
)
from constructs import Construct

from infra.stacks.data_stack import DataStack


class AppStack(Stack):
    def __init__(
        self, scope: Construct, id: str, data_stack: DataStack, **kwargs
    ) -> None:
        super().__init__(scope, id, **kwargs)

        # ==========================================
        # ネットワーク
        # ==========================================
        # NAT Gatewayの作成
        public_subnet = data_stack.vpc.public_subnets[0]

        eip = ec2.CfnEIP(self, "ChurnAppCdkNatEIP")
        nat_gateway = ec2.CfnNatGateway(
            self,
            "ChurnAppCdkNatGateway",
            allocation_id=eip.attr_allocation_id,
            subnet_id=public_subnet.subnet_id,
        )

        for i, isolated_subnet in enumerate(data_stack.vpc.isolated_subnets):
            ec2.CfnRoute(
                self,
                f"ChurnAppCdkNatRoute{i}",
                route_table_id=isolated_subnet.route_table.route_table_id,
                destination_cidr_block="0.0.0.0/0",
                nat_gateway_id=nat_gateway.ref,
            )

        # ==========================================
        # コンテナ基盤（ECS / ECR）
        # ==========================================
        # ECSクラスタの作成
        cluster = ecs.Cluster(
            self,
            "ChurnAppCdkCluster",
            vpc=data_stack.vpc,
        )

        # ECRリポジトリの作成
        backend_repo = ecr.Repository(
            self,
            "ChurnAppCdkBackendRepo",
            repository_name="churn-app-backend",
            removal_policy=RemovalPolicy.DESTROY,
            auto_delete_images=True,
        )

        # ==========================================
        # アプリケーション（Fargate）
        # ==========================================
        # タスク定義
        task_definition = ecs.FargateTaskDefinition(
            self,
            "ChurnAppCdkTaskDef",
            cpu=256,
            memory_limit_mib=512,
        )
        task_definition.add_container(
            "ChurnAppCdkContainer",
            image=ecs.ContainerImage.from_ecr_repository(backend_repo, tag="latest"),
            port_mappings=[ecs.PortMapping(container_port=8000)],
            environment={
                "DATABASE_URL": data_stack.rds_instance.db_instance_endpoint_address,
                "S3_BUCKET_NAME": data_stack.model_bucket.bucket_name,
            },
        )

        # Fargateサービスの作成
        fargate_service = ecs.FargateService(
            self,
            "ChurnAppCdkFargateService",
            cluster=cluster,
            task_definition=task_definition,
            desired_count=1,
            vpc_subnets=ec2.SubnetSelection(
                subnet_type=ec2.SubnetType.PRIVATE_ISOLATED
            ),
        )

        # FargateサービスからRDSへのセキュリティグループ通信許可（インバウンドルール）
        data_stack.rds_sg.add_ingress_rule(
            peer=fargate_service.connections.security_groups[0],
            connection=ec2.Port.tcp(5432),
            description="Allow Fargate service to access RDS",
        )

        # モデル用S3バケットへの読み書き権限（IAM）をFargateタスクに付与
        data_stack.model_bucket.grant_read_write(
            fargate_service.task_definition.task_role
        )

        # ==========================================
        # ロードバランサー（ALB）
        # ==========================================
        # ALBの作成
        alb = elb.ApplicationLoadBalancer(
            self,
            "ChurnAppCdkALB",
            vpc=data_stack.vpc,
            internet_facing=True,
        )
        # ALBのリスナー
        listener = alb.add_listener(
            "ChurnAppCdkListener",
            port=443,
            certificates=[data_stack.alb_certificate],  # ACM証明書を指定
        )

        # ターゲットグループの紐づけ
        listener.add_targets(
            "ChurnAppCdkTarget",
            port=8000,
            targets=[fargate_service],
        )
