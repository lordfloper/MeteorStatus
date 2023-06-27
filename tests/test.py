import MeteorsStatus

event = {
    "Records": [
        {
            "s3": {
                "bucket": {
                    "name": "meteorsdata"
                },
                "object": {
                    "key": "near_earth_objects-2023-06-07.json"
                }
            }
        }
    ]
}

MeteorsStatus.lambda_handler(event, {})