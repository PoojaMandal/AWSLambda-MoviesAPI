import simplejson as json
import boto3
import os
from boto3.dynamodb.conditions import Key

dynamodb = boto3.resource('dynamodb')
table_name = os.environ.get('MOVIES_TABLE')


def lambda_handler(event, context):
    # dynamodb = boto3.resource('dynamodb')
    # table_name = os.environ.get('ORDERS_TABLE')
    table = dynamodb.Table(table_name)
    movie_id = int(event['pathParameters']['id'])
    response = table.query(KeyConditionExpression = Key('id').eq(movie_id))
    return {
        'statusCode': 200,
        'headers': {},
        'body': json.dumps(response['Items'])
    }