import boto3

client = boto3.client('route53')
response = client.get_health_check(
    HealthCheckId='a389b0b5-5322-49ef-b1c3-3edb9e5f617b'
)
print(response)