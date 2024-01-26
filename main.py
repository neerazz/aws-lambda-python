from app.lambda_function import lambda_runner


def lambda_handler(event, context):
    print(event)
    lambda_runner(event, context)