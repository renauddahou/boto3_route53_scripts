import boto3

client = boto3.client('route53')
response = client.get_query_logging_config(
    Id='b9db30fa-7594-4184-8d68-1fa13b149028'
)
print(response)