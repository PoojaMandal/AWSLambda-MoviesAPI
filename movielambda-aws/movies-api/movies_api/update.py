import json
import boto3
import os

dynamodb = boto3.resource('dynamodb')
table_name = os.environ.get('MOVIES_TABLE')

def lambda_handler(event, context):
    # Parse movie ID from path parameters
    movie_id = event['pathParameters']['id']

    # Parse request body to extract updated movie details
    request_body = json.loads(event['body'])

    # Extract updated movie details
    updated_movie_name = request_body.get('movieName')
    updated_movie_type = request_body.get('movie_type')

    # Update movie details in DynamoDB
    table = dynamodb.Table(table_name)
    try:
        response = table.update_item(
            Key={
                'id': int(movie_id)
            },
            UpdateExpression="set movieName = :n, movie_type = :t",
            ExpressionAttributeValues={
                ':n': updated_movie_name,
                ':t': updated_movie_type
            },
            ReturnValues="UPDATED_NEW"
        )
        updated_movie = response['Attributes']
        
        return {
            'statusCode': 200,
            'headers': {},
            'body': json.dumps(updated_movie)
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'headers': {},
            'body': json.dumps({'error': str(e)})
        }
