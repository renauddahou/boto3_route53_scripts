import boto3

client = boto3.client('route53')
response = client.get_hosted_zone_count()

print(response)