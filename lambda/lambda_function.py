import json
import os
import time
import boto3

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table(os.environ.get("TABLE_NAME", "EnergyReadings"))

def lambda_handler(event, context):
    """
    Processes IoT energy readings and stores them in DynamoDB.

    Expected event:
    {
        "deviceId": "ESP32-001",
        "voltage": 230.5,
        "current": 3.2,
        "power": 737.6
    }
    """

    try:
        body = event

        if "body" in event:
            body = json.loads(event["body"])

        item = {
            "deviceId": body["deviceId"],
            "timestamp": int(time.time()),
            "voltage": float(body["voltage"]),
            "current": float(body["current"]),
            "power": float(body["power"])
        }

        table.put_item(Item=item)

        return {
            "statusCode": 200,
            "body": json.dumps({
                "message": "Energy reading stored successfully.",
                "data": item
            })
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({
                "error": str(e)
            })
        }