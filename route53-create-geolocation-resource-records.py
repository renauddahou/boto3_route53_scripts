import boto3

client = boto3.client('route53')
response = client.change_resource_record_sets(
    ChangeBatch={
        'Changes': [
            {
                'Action': 'CREATE',
                'ResourceRecordSet': {
                    'GeoLocation': {
                        'ContinentCode': 'NA',
                    },
                    'Name': 'prod01webserver.hands-on.cloud',
                    'ResourceRecords': [
                        {
                            'Value': '137.215.223.99',
                        },
                    ],
                    'SetIdentifier': 'North America',
                    'TTL': 60,
                    'Type': 'A',
                },
            },
            {
                'Action': 'CREATE',
                'ResourceRecordSet': {
                    'GeoLocation': {
                        'ContinentCode': 'AF',
                    },
                    'Name': 'prod01webserver.hands-on.cloud',
                    'ResourceRecords': [
                        {
                            'Value': '16.190.26.7',
                        },
                    ],
                    'SetIdentifier': 'Africa',
                    'TTL': 60,
                    'Type': 'A',
                },
            },
            {
                'Action': 'CREATE',
                'ResourceRecordSet': {
                    'GeoLocation': {
                        'ContinentCode': 'EU',
                    },
                    'Name': 'prod01webserver.hands-on.cloud',
                    'ResourceRecords': [
                        {
                            'Value': '154.196.99.176',
                        },
                    ],
                    'SetIdentifier': 'Europe',
                    'TTL': 60,
                    'Type': 'A',
                },
            },
            {
                'Action': 'CREATE',
                'ResourceRecordSet': {
                    'GeoLocation': {
                        'CountryCode': '*',
                    },
                    'Name': 'prod01webserver.hands-on.cloud',
                    'ResourceRecords': [
                        {
                            'Value': '162.235.70.246',
                        },
                    ],
                    'SetIdentifier': 'Other locations',
                    'TTL': 60,
                    'Type': 'A',
                },
            },
        ],
        'Comment': 'Geolocation configuration for hands-on.cloud',
    },
    HostedZoneId='Z00594533FY3S68ROG6V2',
)
print(response)