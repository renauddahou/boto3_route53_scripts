import boto3

client = boto3.client('route53')
response = client.associate_vpc_with_hosted_zone(
    HostedZoneId='Z04348832HMRIVU622GN5',
    VPC={
        'VPCRegion': 'us-east-2',
        'VPCId': 'vpc-08d4905ad0cd75085'
    },
    Comment='Attach my-vpc-01'
)
print(response)