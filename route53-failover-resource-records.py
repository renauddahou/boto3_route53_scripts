import boto3

client = boto3.client('route53')
response = client.change_resource_record_sets(
    ChangeBatch={
        'Changes': [
            {
                'Action': 'CREATE',
                'ResourceRecordSet': {
                    'Failover': 'PRIMARY',
                    'HealthCheckId': '18ac9f16-47e0-4982-bcbd-12670ddc07e3',
                    'Name': 'prodwebserver.hands-on.cloud',
                    'ResourceRecords': [
                        {
                            'Value': '3.139.19.216',
                        },
                    ],
                    'SetIdentifier': 'Production Server 1',
                    'TTL': 60,
                    'Type': 'A',
                },
            },
            {
                'Action': 'CREATE',
                'ResourceRecordSet': {
                    'Failover': 'SECONDARY',
                    'HealthCheckId': '88a8a313-65f9-48da-a1d4-e3573454287b',
                    'Name': 'prodwebserver.hands-on.cloud',
                    'ResourceRecords': [
                        {
                            'Value': '3.17.17.88',
                        },
                    ],
                    'SetIdentifier': 'Production Server 2',
                    'TTL': 60,
                    'Type': 'A',
                },
            },
        ],
        'Comment': 'Failover configuration for hands-on.cloud',
    },
    HostedZoneId='Z00594533FY3S68ROG6V2',
)
print(response)