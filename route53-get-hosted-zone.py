import boto3

client = boto3.client('route53')
response = client.get_hosted_zone(
    Id='Z04348832HMRIVU622GN5'
)
print(response)