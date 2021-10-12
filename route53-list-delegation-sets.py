import boto3

client = boto3.client('route53')
response = client.list_reusable_delegation_sets()
print(response)