import boto3

client = boto3.client('route53')
response = client.get_health_check_last_failure_reason(
    HealthCheckId='a389b0b5-5322-49ef-b1c3-3edb9e5f617b'
)
print(response)