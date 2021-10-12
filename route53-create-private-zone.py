import boto3

client = boto3.client('route53')
response = client.create_hosted_zone(
    Name='hands-on.private',
    VPC={
        'VPCRegion': 'us-east-2',
        'VPCId': 'vpc-4b43de20'
    },
    CallerReference='handsonprivate001',
)
print(response)