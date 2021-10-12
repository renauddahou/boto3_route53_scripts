import boto3

client = boto3.client('route53')
response = client.delete_hosted_zone(
    Id='Z104108719AYS9LM7Z6DV'
)
print(response)