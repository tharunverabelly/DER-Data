import json
import boto3

def lambda_handler(event, context):
    # TODO implement
    client_dynamo = boto3.resource('dynamodb', region_name='us-east-1')
    table=client_dynamo.Table('Session_Packets')
    try:
        response=table.put_item(Item = event)
        return "Done"
    except:
        raise