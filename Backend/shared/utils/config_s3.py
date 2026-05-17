import boto3
import os
import secrets

from botocore.exceptions import ClientError
from pathlib import Path
from mypy_boto3_s3 import  S3Client
from dotenv import load_dotenv
from shared.errors.uploads_errors import UploadsError
import os

load_dotenv(override=True)
def aws_config_s3():
    s3_client = boto3.client(
        "s3",
        aws_access_key_id=os.getenv("AWS_ACCESS_KEY"),
        aws_secret_access_key=os.getenv("AWS_SECRET_KEY"),
        endpoint_url=os.getenv("AWS_ENDPINTS"),
    )
    return s3_client

def aws_upload_file_and_full_rename(files,path,lang):
    try:
        s3_client = aws_config_s3()
        bucket_url = os.getenv("AWS_CUSTOM_DOMAIN")
        # file
        file_name = Path(files.filename)
        new_name = f"{secrets.token_urlsafe(12)}.webp"
        new_file_name = file_name.with_name(new_name)
        # uploads
        s3_client.upload_fileobj(files.file, os.getenv("BUCKET_NAME"), f"{path}/{new_file_name}")
    except ClientError:
        raise UploadsError(lang["uploads"]["failed"])

    return f"{bucket_url}/{path}/{new_file_name}"


def aws_upload_file_and_rename_name(files,path, lang):
    try:
        s3_client = aws_config_s3()
        bucket_url = os.getenv("AWS_CUSTOM_DOMAIN")
        # file
        file_name = Path(files.filename)
        file_extension=file_name.suffix
        new_name = secrets.token_urlsafe(12)
        new_file_name = file_name.with_name(f"{new_name}{file_extension}")
        # uploads
        s3_client.upload_fileobj(files.file, os.getenv("BUCKET_NAME"), f"{path}/{new_file_name}")
    except ClientError:
        raise UploadsError(lang["uploads"]["failed"])

    return f"{bucket_url}/{path}/{new_file_name}"
