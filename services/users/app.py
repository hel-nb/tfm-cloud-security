def lambda_handler(event, context):
    if event.get("fail"):
        return {
            "statusCode": 500,
            "body": "Forced error"
        }
        
    return {
        "statusCode": 200,
        "body": "Users service DEV"
    }
