import boto3

client = boto3.client('route53')
response = client.list_query_logging_configs()
print(response)