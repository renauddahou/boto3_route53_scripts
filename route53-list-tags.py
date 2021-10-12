import boto3

client = boto3.client('route53')
response = client.list_tags_for_resource(
    ResourceType='hostedzone',
    ResourceId='Z00594533FY3S68ROG6V2'
)
print(response)