import json
import logging
import os

import boto3

logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Initialize DynamoDB boto3 object
dynamodb = boto3.resource('dynamodb')
# Set DynamoDB table name variable from env
ddbTableName = os.environ['databaseName']
table = dynamodb.Table(ddbTableName)

ALLOWED_ORIGINS = [
    "https://estebanmoreno.link",
    "https://www.estebanmoreno.link",
]


def lambda_handler(event, context):
    origin = (event.get("headers") or {}).get("origin", "")
    cors_origin = origin if origin in ALLOWED_ORIGINS else ALLOWED_ORIGINS[0]

    headers = {
        "Access-Control-Allow-Origin": cors_origin,
        "Access-Control-Allow-Headers": "Content-Type",
        "Access-Control-Allow-Methods": "OPTIONS,POST,GET",
    }

    try:
        # Atomically increment the counter; ADD creates the attribute if absent
        table.update_item(
            Key={"id": "Visits"},
            UpdateExpression="ADD Visits :value",
            ExpressionAttributeValues={":value": 1},
        )

        ddbResponse = table.get_item(Key={"id": "Visits"})
        item = ddbResponse.get("Item", {})
        visits = int(item.get("Visits", 0))

    except Exception as e:
        logger.error("DynamoDB operation failed: %s", str(e))
        return {
            "isBase64Encoded": False,
            "statusCode": 500,
            "headers": headers,
            "body": json.dumps({"error": "Internal server error"}),
        }

    return {
        "isBase64Encoded": False,
        "statusCode": 200,
        "headers": headers,
        "body": json.dumps({"count": visits}),
    }
