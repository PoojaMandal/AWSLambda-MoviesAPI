import json
import boto3
import os

dynamodb = boto3.resource('dynamodb')
table_name = os.environ.get('MOVIES_TABLE')

def lambda_handler(event, context):
    # Parse movie ID from path parameters
    movie_id = event['pathParameters']['id']

    # Delete the movie from DynamoDB
    table = dynamodb.Table(table_name)
    try:
        response = table.delete_item(
            Key={
                'id': int(movie_id)
            }
        )
        
        return {
            'statusCode': 200,
            'headers': {},
            'body': json.dumps({'message': 'Movie deleted successfully'})
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'headers': {},
            'body': json.dumps({'error': str(e)})
        }
