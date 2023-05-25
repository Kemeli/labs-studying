from chalice import Chalice, Response
import logging
import boto3
from botocore.exceptions import ClientError
import json
import os
import time
import sys
import requests
import io


AWS_REGION = 'us-east-1'
ENDPOINT_URL = 'http://host.docker.internal:4566'
BUCKET = 'backup'

GADGETS = [
    'https://game.42sp.org.br/static/assets/achievements/get_next_linem.png',
    'https://game.42sp.org.br/static/assets/achievements/ft_printfe.png',
    'https://game.42sp.org.br/static/assets/achievements/born2berootm.png',
    'https://game.42sp.org.br/static/assets/achievements/netpracticee.png'
    ]

s3_client = boto3.client('s3', region_name=AWS_REGION,
                         endpoint_url=ENDPOINT_URL)

def create_bucket_s3(bucket_name):
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
def create_bucket(event, context):
    create_bucket_s3(BUCKET)

@app.lambda_function()
def delete_image(event, context):
    client = boto3.client('s3')
    s3_client.delete_object(Bucket=BUCKET, Key=event['filename'])
    return 'Deleted Successfully!'

@app.lambda_function()
def upload_image_by_request(event, context):
    for gadget in GADGETS:
        response = requests.get(gadget).content
        s3_client.put_object(Body=response, Bucket=BUCKET, Key=os.path.basename(gadget))
    return f'Uploaded Successfully!'


@app.lambda_function()
def upload_image(event, context):
    directories = [
        '.',
        '/opt/python/lib/python%s.%s/site-packages' % sys.version_info[:2]
    ]
    for dirname in directories:
        full_path = os.path.join(dirname, event['filename'])
        if os.path.isfile(full_path):
            upload_file(full_path, BUCKET)
    return 'Uploaded Successfully!'

@app.lambda_function()
def list_objects(event, context):
    contents = []
    for key in s3_client.list_objects(Bucket=BUCKET)['Contents']:
        contents.append(key['Key'])
    return {'Contens:': contents}

@app.route('/download/{filename}', methods=['GET'])
def download_file(filename):
    bytes_buffer = io.BytesIO()
    s3_client.download_fileobj(Bucket=BUCKET, Key=filename, Fileobj=bytes_buffer)
    byte_value = bytes_buffer.getvalue()
    return Response(body=byte_value, 
        headers = {
                'Content-Type': 'application/octet-stream',
                'Content-Disposition': f'attachment; filename="{filename}"'
            })