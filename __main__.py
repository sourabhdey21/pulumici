"""An AWS Python Pulumi program"""

import pulumi
from pulumi_aws import s3, ec2

# Create an AWS resource (S3 Bucket)
bucket = s3.Bucket('jarvis-bucket')

# Create a new VPC
vpc = ec2.Vpc("my-vpc",
    cidr_block="10.1.0.0/16",
    tags={
        "tags": {
            "Name": "jarvis-vpc",
        },
    })

# Create a subnet
subnet = ec2.Subnet("my-subnet",
    vpc_id=vpc.id,
    cidr_block="10.1.1.0/24",
    availability_zone="us-east-1a",
    tags={
        "tags": {
            "Name": "jarvis-subnet",
        },
    })

# Export the VPC ID
pulumi.export("vpc_id", vpc.id)
