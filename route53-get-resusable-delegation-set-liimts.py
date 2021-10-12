import boto3

client = boto3.client('route53')
response = client.get_reusable_delegation_set_limit(
    Type='MAX_ZONES_BY_REUSABLE_DELEGATION_SET',
    DelegationSetId='N0953557IKIEW071BV7F'
)
print(response)