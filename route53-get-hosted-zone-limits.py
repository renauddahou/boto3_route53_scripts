import boto3

client = boto3.client('route53')
response = client.get_hosted_zone_limit(
    Type='MAX_VPCS_ASSOCIATED_BY_ZONE',
    HostedZoneId='Z04348832HMRIVU622GN5'
)
print(response)