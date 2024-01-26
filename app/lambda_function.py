import db_connector
import json


def lambda_runner(event, context):
    # Get 'name' from query string parameters
    query_params = event['queryStringParameters']
    name = query_params["name"] if "name" in query_params else ""

    # Connect to database and fetch user details
    user_details = db_connector.get_user_details(query_params["name"])

    return {
        'statusCode': 200,
        'body': json.dumps(user_details)
    }
