import boto3

client = boto3.client('route53')
response = client.create_reusable_delegation_set(
    CallerReference='delegationset001',
    HostedZoneId='Z00594533FY3S68ROG6V2'
)
print(response)