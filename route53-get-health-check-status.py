import boto3

client = boto3.client('route53')
response = client.get_health_check_status(
    HealthCheckId='45f6f4b8-3d69-43c1-9cbd-f1d403c31a51'
)
print(response)