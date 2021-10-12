import json
import boto3

client = boto3.client('logs',region_name='us-east-1')

policy = {
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "Route53LogsToCloudWatchLogs",
      "Effect": "Allow",
      "Principal": {
        "Service": [
          "route53.amazonaws.com"
        ]
      },
      "Action": [
        "logs:CreateLogStream",
        "logs:PutLogEvents"
      ],
      "Resource": "arn:aws:logs:us-east-1:585584209241:log-group:*"
    }
  ]
}

response = client.put_resource_policy(
    policyName='Route53Logs',
    policyDocument= json.dumps(policy)
)
print(response)