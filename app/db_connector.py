import json

import boto3
import psycopg2


def get_secret(secret_name: str):
    client = boto3.client('secretsmanager')
    secret_value = client.get_secret_value(SecretId=secret_name)
    return json.loads(secret_value['SecretString'])


def get_config(database_name: str):
    client = boto3.client('ssm')
    parameter = client.get_parameter(Name=database_name, WithDecryption=True)
    return parameter['Parameter']['Value']


def run_query(database_name: str, user_name: str, secret_name: str, query: str):
    password = get_secret(secret_name)
    username = get_config(user_name)
    db_url = get_config(database_name)
    # Connect to the database (replace with your database library and connection logic)
    with database_connection(db_url, username, password) as conn:
        cursor = conn.cursor()
        cursor.execute(query)
        return cursor.fetchall()


def database_connection(db_url, username, password):
    conn = psycopg2.connect(db_url, user=username, password=password)
    return conn


def get_user_details(name):

    query = "SELECT * FROM users WHERE username='{}'".format(name)
    users = run_query("user_db", "test_user_id", "test_password", query)
