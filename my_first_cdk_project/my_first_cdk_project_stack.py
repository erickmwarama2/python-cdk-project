from aws_cdk import (
    # Duration,
    # Stack,
    # aws_sqs as sqs,
    core,
    aws_s3 as _s3
)
from constructs import Construct

class MyFirstCdkProjectStack(core.Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        _s3.Bucket(
            self,
            "myBucketId",
            bucket_name="erickfirstcdkbucket",
            versioned=True,
            encryption=_s3.BucketEncryption.KMS_MANAGED
        )