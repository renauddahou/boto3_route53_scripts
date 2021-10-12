import boto3

client = boto3.client('route53')
response = client.list_resource_record_sets(
    HostedZoneId='Z00594533FY3S68ROG6V2'
)
print(response)