import boto3

client = boto3.client('route53')
response = client.change_resource_record_sets(
    ChangeBatch={
        'Changes': [
            {
                'Action': 'CREATE',
                'ResourceRecordSet': {
                    'Name': 'stagingwebserver.hands-on.cloud',
                    'Region': 'us-east-2',
                    'ResourceRecords': [
                        {
                            'Value': '18.116.151.109',
                        },
                    ],
                    'SetIdentifier': 'Ohio region',
                    'TTL': 60,
                    'Type': 'A',
                },
            },
            {
                'Action': 'CREATE',
                'ResourceRecordSet': {
                    'Name': 'stagingwebserver.hands-on.cloud',
                    'Region': 'us-west-2',
                    'ResourceRecords': [
                        {
                            'Value': '3.131.244.131',
                        },
                    ],
                    'SetIdentifier': 'Oregon region',
                    'TTL': 60,
                    'Type': 'A',
                },
            },
        ],
        'Comment': 'Staging Web servers for hands-on.cloud',
    },
    HostedZoneId='Z00594533FY3S68ROG6V2',
)
print(response)