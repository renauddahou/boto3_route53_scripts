import boto3

client = boto3.client('route53',region_name="us-east-1")
response = client.create_query_logging_config(
    HostedZoneId='Z01765103CJ1HG1H1J2LO',
    CloudWatchLogsLogGroupArn='arn:aws:logs:us-east-1:585584209241:log-group:/aws/route53/hands-on.cloud'
)
print(response)