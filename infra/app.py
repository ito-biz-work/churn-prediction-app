import aws_cdk as cdk
from stack import PortfolioInfraStack

app = cdk.App()
PortfolioInfraStack(app, "PortfolioInfraStack")
app.synth()
