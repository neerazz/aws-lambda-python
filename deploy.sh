#!/bin/bash

# Define variables
S3_BUCKET="your-s3-bucket-name"
LAMBDA_FUNCTION_NAME="your-lambda-function-name"
ZIP_FILE="lambda.zip"

# Install dependencies
pip install -r requirements.txt -t ./

# Bundle files into a zip
zip -r $ZIP_FILE ./*

# Upload to S3
aws s3 cp $ZIP_FILE s3://$S3_BUCKET/$ZIP_FILE

# Update Lambda function
aws lambda update-function-code --function-name $LAMBDA_FUNCTION_NAME --s3-bucket $S3_BUCKET --s3-key $ZIP_FILE
