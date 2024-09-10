"""An AWS Python Pulumi program"""

import pulumi
from pulumi_aws import s3
import pulumi_aws as aws


# Create an AWS resource (S3 Bucket)
bucket = s3.Bucket('jarvis-bucket')

# Create a new VPC
vpc = aws.ec2.Vpc("my-vpc",
    cidr_block="10.1.0.0/16",
    tags={
        "Name": "jarvis-vpc",
    })

# Create an internet gateway
igw = aws.ec2.InternetGateway("my-igw",
    vpc_id=vpc.id,
    tags={
        "tags": [
            {"key": "Name", "value": "jarvis-igw"},
        ],
    })

# Export the VPC ID
pulumi.export("vpc_id", vpc.id)
