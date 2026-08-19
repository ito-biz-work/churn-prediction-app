from aws_cdk import (
    RemovalPolicy,
    Stack,
    aws_ec2 as ec2,
    aws_s3 as s3,
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
