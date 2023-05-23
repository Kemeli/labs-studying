import logging
import boto3
from botocore.exceptions import ClientError
import json
import os

AWS_REGION = 'us-east-1'
ENDPOINT_URL = 'http://localhost:4566'


s3_client = boto3.client('s3', region_name=AWS_REGION,
                         endpoint_url=ENDPOINT_URL)

def create_bucket(bucket_name):
    try:
        response = s3_client.create_bucket(
            Bucket=bucket_name)
    except ClientError:
        #logger.exception('Could not create S3 bucket locally.')
        raise
    else:
        return response

def main():
    s3 = create_bucket(input('bucket_name: '))

if __name__ == '__main__':
    main()