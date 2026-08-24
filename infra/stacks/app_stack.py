from aws_cdk import (
    Stack,
    aws_ec2 as ec2,
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
