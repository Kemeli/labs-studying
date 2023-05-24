from chalice import Chalice, Response
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

def upload_file(file_name, bucket, object_name=None):
    try:
        if object_name is None:
            object_name = os.path.basename(file_name)
        response = s3_client.upload_file(
            file_name, bucket, object_name)
    except ClientError:
        # logger.exception('Could not upload file to S3 bucket.')
        raise
    else:
        return response

app = Chalice(app_name='backup')


@app.lambda_function()
def first_function(event, context):
    create_bucket('backup')


@app.lambda_function()
def second_function(event, context):
   return upload_to_s3('test_up.txt')


@app.route('/upload/{file_name}', methods=['PUT'],
           content_types=['application/octet-stream'])
def upload_to_s3(file_name):

    # get raw body of PUT request
    body = app.current_request.raw_body
    print("\n\nbody: ", body)

    # write body to tmp file
    tmp_file_name = '/tmp/' + 'file_name'
    with open(tmp_file_name, 'wb') as tmp_file:
        tmp_file.write(body)

    # upload tmp file to s3 bucket
    s3_client.upload_file(tmp_file_name, 'backup', file_name)

    return Response(body='upload successful: {}'.format(file_name),
                    status_code=200,
                    headers={'Content-Type': 'text/plain'})
