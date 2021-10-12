import boto3

client = boto3.client('route53')
response = client.get_health_check_count()

print(response)