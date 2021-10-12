import boto3

client = boto3.client('route53')
response = client.create_key_signing_key(
    CallerReference='key001',
    HostedZoneId='Z00594533FY3S68ROG6V2',
    KeyManagementServiceArn='arn:aws:kms:us-east-1:585584209241:key/6bd3f30e-e659-477d-a782-1104ea64df72',
    Name='handsoncloudkey',
    Status='ACTIVE',
)
print(response)