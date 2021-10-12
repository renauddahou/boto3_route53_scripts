import boto3

client = boto3.client('route53')
response = client.get_reusable_delegation_set(
    Id='N0953557IKIEW071BV7F'
)
print(response)