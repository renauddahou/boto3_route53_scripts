import boto3

client = boto3.client('route53')
response = client.test_dns_answer(
    HostedZoneId='Z00594533FY3S68ROG6V2',
    RecordName='testwebserver.hands-on.cloud',
    RecordType='A',
)
print(response)