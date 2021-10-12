import boto3

client = boto3.client('route53')
response = client.create_hosted_zone(
    Name='hands-on.cloud',
    CallerReference='handsoncloud001',
)
print(response)