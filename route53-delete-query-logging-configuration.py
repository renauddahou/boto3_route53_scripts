import boto3

client = boto3.client('route53')
response = client.delete_query_logging_config(
    Id='43da740f-1810-4723-b258-9c0ee70748cd'
)
print(response)