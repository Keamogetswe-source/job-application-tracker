import json

def lambda_handler(event, context):
    data = [
        {"company": "Acme", "role": "Junior Data Analyst", "status": "Applied"},
        {"company": "Globex", "role": "BI Analyst", "status": "Interview"},
    ]
    return {
        "statusCode":200,
           "headers": {"Content-Type": "application/json"},
        "body": json.dumps(data),
    }