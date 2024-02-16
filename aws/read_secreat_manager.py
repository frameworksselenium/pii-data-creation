import boto3
from botocore.exceptions import ClientError
import json

def get_secret():
    secret_name = "postgres_secret"
    region_name = "us-east-1"

    # Create a Secrets Manager client
    # session = boto3.session.Session()
    # client = session.client(
    #     service_name='secretsmanager',
    #     region_name=region_name
    # )

    session = boto3.session.Session()
    client = session.client(
        service_name='secretsmanager',
        region_name=region_name,
        aws_access_key_id='AKIA3PLF4DOAXDKWX5U7',
        aws_secret_access_key='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'
    )

    try:
        get_secret_value_response = client.get_secret_value(
            SecretId=secret_name
        )
    except ClientError as e:
        # For a list of exceptions thrown, see
        # https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_GetSecretValue.html
        raise e

    secret = get_secret_value_response['SecretString']

    return json.loads(secret)
