import simplejson as json
import boto3
import os

dynamodb = boto3.resource('dynamodb')
table_name = os.environ.get('MOVIES_TABLE')

def lambda_handler(event, context):
    table = dynamodb.Table(table_name)
    response = table.scan()
    
    movies = response['Items']
    
    return {
        'statusCode': 200,
        'headers': {},
        'body': json.dumps(movies)
    }
