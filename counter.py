import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.table('gino-resume-test')

def lambda_handler(event, context):
    response = table.get_item(key = {
        "id":"0"
    })
    views = response['Item']['views']
    views += 1
    print(views)
    repsonse = table.put_item(Item = {
        "id":"1"
        "views":views
    })
    
