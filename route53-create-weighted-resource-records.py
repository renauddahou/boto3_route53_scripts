import boto3

client = boto3.client('route53')
response = client.change_resource_record_sets(
    ChangeBatch={
        'Changes': [
            {
                'Action': 'CREATE',
                'ResourceRecordSet': {
                    'Name': 'testwebserver.hands-on.cloud',
                    'ResourceRecords': [
                        {
                            'Value': '18.116.151.109',
                        },
                    ],
                    'SetIdentifier': 'Test Server 1',
                    'TTL': 60,
                    'Type': 'A',
                    'Weight': 60,
                },
            },
            {
                'Action': 'CREATE',
                'ResourceRecordSet': {
                    'Name': 'testwebserver.hands-on.cloud',
                    'ResourceRecords': [
                        {
                            'Value': '18.216.198.81',
                        },
                    ],
                    'SetIdentifier': 'Test Server 2',
                    'TTL': 60,
                    'Type': 'A',
                    'Weight': 40,
                },
            },
        ],
        'Comment': 'Test Web servers for hands-on.cloud',
    },
    HostedZoneId='Z00594533FY3S68ROG6V2',
)
print(response)