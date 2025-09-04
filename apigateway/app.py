# import requests

def lambda_handler(event, context):
    return {
        "statusCode": 200,
        "body": event["queryStringParameters"]["foo"]
    }