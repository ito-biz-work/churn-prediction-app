from aws_cdk import (
    RemovalPolicy,
    Stack,
    aws_ec2 as ec2,
    aws_rds as rds,
    aws_s3 as s3,
    aws_ssm as ssm,
)
from constructs import Construct


class DataStack(Stack):
    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # ==========================================
        # ネットワーク
        # ==========================================
        # VPC・サブネットの作成
        self.vpc = ec2.Vpc(
            self,
            "ChurnAppCdkVpc",
            max_azs=2,  # マルチAZ配置
            nat_gateways=0,
            subnet_configuration=[
                ec2.SubnetConfiguration(
                    name="public", subnet_type=ec2.SubnetType.PUBLIC, cidr_mask=24
                ),
                ec2.SubnetConfiguration(
                    name="private",
                    subnet_type=ec2.SubnetType.PRIVATE_WITH_EGRESS,
                    cidr_mask=24,
                ),
            ],
        )

        # S3 Gateway Endpointの作成
        self.vpc.add_gateway_endpoint(
            "S3Endpoint", service=ec2.GatewayVpcEndpointAwsService.S3
        )

        # ==========================================
        # ストレージ
        # ==========================================
        # フロントエンド静的ファイル用S3バケットの作成
        self.frontend_bucket = s3.Bucket(
            self,
            "ChurnAppCdkFrontendBucket",
            block_public_access=s3.BlockPublicAccess.BLOCK_ALL,
            removal_policy=RemovalPolicy.DESTROY,
            auto_delete_objects=True,
        )

        # 学習済みモデル用S3バケットの作成
        self.model_bucket = s3.Bucket(
            self,
            "ChurnAppCdkModelBucket",
            block_public_access=s3.BlockPublicAccess.BLOCK_ALL,
            removal_policy=RemovalPolicy.RETAIN,
        )

        # ==========================================
        # データストア（RDS）
        # ==========================================
        # セキュリティグループの作成
        self.rds_sg = ec2.SecurityGroup(
            self,
            "ChurnAppCdkRdsSecurityGroup",
            vpc=self.vpc,
            description="Security group for RDS",
            allow_all_outbound=True,
        )

        # RDSインスタンスの作成
        self.rds_instance = rds.DatabaseInstance(
            self,
            "ChurnAppCdkRdsInstance",
            engine=rds.DatabaseInstanceEngine.postgres(
                version=rds.PostgresEngineVersion.VER_18_4
            ),
            instance_type=ec2.InstanceType.of(
                ec2.InstanceClass.BURSTABLE4_GRAVITON, ec2.InstanceSize.MICRO
            ),
            vpc=self.vpc,
            vpc_subnets=ec2.SubnetSelection(
                subnet_type=ec2.SubnetType.PRIVATE_WITH_EGRESS
            ),
            security_groups=[self.rds_sg],
            database_name="churn",
            credentials=rds.Credentials.from_generated_secret("churn_admin"),
            allocated_storage=20,
            max_allocated_storage=100,
            removal_policy=RemovalPolicy.RETAIN,
        )

        # ==========================================
        # パラメータストア（SSM）
        # ==========================================
        ssm.StringParameter(
            self,
            "ChurnAppCdkDatabaseUrlParameter",
            parameter_name="/churn-app-cdk/database-url",
            string_value=self.rds_instance.db_instance_endpoint_address,
        )
        ssm.StringParameter(
            self,
            "ChurnAppCdkModelBucketNameParameter",
            parameter_name="/churn-app-cdk/s3-ml-bucket-name",
            string_value=self.model_bucket.bucket_name,
        )
