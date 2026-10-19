import json
import boto3

table = boto3.resource("dynamodb").Table("applications")

def lambda_handler(event, context):
    items = table.scan()["Items"]
    return {
        "statusCode": 200,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps(items),
    }