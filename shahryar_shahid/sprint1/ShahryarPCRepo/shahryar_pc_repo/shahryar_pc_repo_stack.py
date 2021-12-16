from aws_cdk import (
    core as cdk,
    aws_lambda as lambda_,
    aws_events as events_,
    aws_events_targets as targets_
)

# For consistency with other languages, `cdk` is the preferred import name for
# the CDK's core module.  The following line also imports it as `core` for use
# with examples from the CDK Developer's Guide, which are in the process of
# being updated to use `cdk`.  You may delete this import if you don't need it.



class ShahryarPcRepoStack(cdk.Stack):

    def __init__(self, scope: cdk.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here

        HWlambda = self.create_lambda("HelloLambda", "./resources", "webhealth_lambda.lambda_handler")
        
        lambda_schedule = events_.Schedule.rate(cdk.Duration.minutes(1))
        lambda_target = targets_.LambdaFunction(handler=HWlambda)
        rule = events_.Rule(self, "webHealth_Invocation", description="Periodic Lambda", enabled=True, schedule=lambda_schedule, targets=[lambda_target])
        
    def create_lambda(self, newid, asset, handler):
        return lambda_.Function(self, id = newid,
        runtime=lambda_.Runtime.PYTHON_3_8,
        handler=handler,
        code=lambda_.Code.from_asset(asset)
        )
