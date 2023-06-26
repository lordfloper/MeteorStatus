import json
import urllib.parse
import os
import boto3 

TABLENAME = "Potentially_hazardous_asteroid",
MAX_DISTANCE_CHANGE = 10
MAX_SPEED_CHANGE = 10

SNS_TOPIC_ARN = os.getenv("SNS_TOPIC_ARN")

def check_hazard_status(name, speed, distance):
    # dynamodb = boto3.client("dynamodb")
    sns = boto3.client("sns")

    # response = dynamodb.get_item(
    #     TableName = TABLENAME,
    #     Key = {'name': {'S': name} }
    # )

    # print(response['Item'])

    sns.publish(
        TopicArn = SNS_TOPIC_ARN,
        Subject = "Hazard! Warning!",
        Message = f"Dangerous, dangerous asteroid {name}. Distance {distance}. Speed {speed}."
    )

def lambda_handler(event, context):
    # TODO implement

    s3 = boto3.client("s3")

    for record in event["Records"]:
        data = {}
        asteroid_status = []
    
        bucket = record["s3"]["bucket"]["name"]
        key = urllib.parse.unquote_plus(record["s3"]["object"]["key"], encoding="utf-8")

        data = json.loads(
            s3.get_object(
                Bucket=bucket,
                Key=key)
            ["Body"].read()
        )
                    
        for date in data.values():
            for objects in date:
                print(f"""
                    Object name: {objects['name']}
                    Dangerous: {objects['is_potentially_hazardous_asteroid']}
                    Size: {objects['estimated_diameter']['meters']['estimated_diameter_max']}
                """)
                asteroid_status.append({
                    "name": objects['name'],
                    "dangerous": objects['is_potentially_hazardous_asteroid'],
                })



