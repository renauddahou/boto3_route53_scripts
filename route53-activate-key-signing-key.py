import boto3

client = boto3.client('route53')
response = client.activate_key_signing_key(
    HostedZoneId='Z00594533FY3S68ROG6V2',
    Name='handsoncloudkey'
)
print(response)