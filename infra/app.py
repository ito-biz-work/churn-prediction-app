import os

import aws_cdk as cdk
from stack import InfraStack

app = cdk.App()

# スタックの作成
InfraStack(
    app,
    "InfraStack",
    env=cdk.Environment(
        account=os.environ["CDK_DEFAULT_ACCOUNT"],
        region=os.environ["CDK_DEFAULT_REGION"],
    ),
)

# タグの一括付与
cdk.Tags.of(app).add("Project", "ChurnApp-v3")
cdk.Tags.of(app).add("ManagedBy", "CDK")

app.synth()
