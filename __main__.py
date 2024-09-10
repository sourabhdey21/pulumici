"""An AWS Python Pulumi program"""

import pulumi
from pulumi_aws import s3

# Create an AWS resource (S3 Bucket)
bucket = s3.Bucket('pulumi-bucket')

# Export the name of the bucket
pulumi.export('bucket_name', bucket.id)

# Create an AWS resource (VPC)
vpc = s3.Vpc('pulumi-vpc', cidr_block='10.0.0.0/16')
pulumi.export('vpc_id', vpc.id)


