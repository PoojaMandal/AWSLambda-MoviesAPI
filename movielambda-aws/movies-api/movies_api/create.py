import json
import boto3
import os

dynamodb = boto3.resource('dynamodb')
table_name = os.environ.get('MOVIES_TABLE')

def lambda_handler(event, context):
    try:
        # Check if 'body' key exists in the event
        if 'body' in event:
            movie = json.loads(event['body'])
            # dynamodb = boto3.resource('dynamodb')
            # table_name = os.environ.get('ORDERS_TABLE')
            table = dynamodb.Table(table_name)
            response = table.put_item(TableName=table_name, Item=movie)
            print(response)
            return {
                'statusCode': 201,
                'headers': {},
                'body': json.dumps({'message': 'Movie Created'})
            }
        else:
            return {
                'statusCode': 400,
                'headers': {},
                'body': json.dumps({'error': 'Request body is missing'})
            }
    except Exception as e:
        return {
            'statusCode': 500,
            'headers': {},
            'body': json.dumps({'error': str(e)})
        }
