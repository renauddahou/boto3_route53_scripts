import boto3

client = boto3.client('route53')
response = client.list_hosted_zones_by_vpc(
    VPCId='vpc-4b43de20',
    VPCRegion='us-east-2'
)
print(response)