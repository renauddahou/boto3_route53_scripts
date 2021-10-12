import boto3

client = boto3.client('route53')
response = client.list_health_checks()
print(response)