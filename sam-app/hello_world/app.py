import json

# import requests


def lambda_handler(event, context):
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "approval added with approvals!!",
            # "location": ip.text.replace("\n", "")
        }),
    }
