import boto3

client = boto3.client('route53')
response = client.get_query_logging_config(
    Id='rqlc-1154ca6d24654070'
)
print(response)