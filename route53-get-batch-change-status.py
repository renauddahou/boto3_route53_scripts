import boto3

client = boto3.client('route53')
response = client.get_change(
    Id='C0658219L4CEONQU6XZ4'
)
print(response)