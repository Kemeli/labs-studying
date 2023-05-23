from chalice import Chalice
import logging
import boto3
from botocore.exceptions import ClientError
import json
import os

AWS_REGION = 'us-east-1'
ENDPOINT_URL = 'http://host.docker.internal:4566'


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

app = Chalice(app_name='backup')


@app.lambda_function()
def first_function(event, context):
    create_bucket('test2')


@app.lambda_function()
def second_function(event, context):
    return {'hello': 'world2'}
