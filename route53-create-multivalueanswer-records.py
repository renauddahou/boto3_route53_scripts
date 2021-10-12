import boto3

client = boto3.client('route53')
response = client.change_resource_record_sets(
    ChangeBatch={
        'Changes': [
            {
                'Action': 'CREATE',
                'ResourceRecordSet': {
                    'Name': 'testwebserver01.hands-on.cloud',
                    'SetIdentifier': 'Multivalueanswer01',
                    'ResourceRecords': [
                        {
                            'Value': '3.128.188.18',
                        },
                    ],
                    'MultiValueAnswer': True,
                    'TTL': 60,
                    'Type': 'A',
                },
            },
        ],
        'Comment': 'Web Server',
    },
    HostedZoneId='Z00594533FY3S68ROG6V2',
)
print(response)