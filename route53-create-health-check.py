import boto3

client = boto3.client('route53')
response = client.create_health_check(
    CallerReference='healthcheck001',
    HealthCheckConfig={
        'IPAddress': '18.216.198.81',
        'Port': 443,
        'Type': 'HTTPS',
        'ResourcePath': '/testhealth.html',
        'RequestInterval': 30,
        'FailureThreshold': 4,
        'Regions': [
            'us-east-1','us-west-1','us-west-2','eu-west-1',
        ],
    }
)
print(response)