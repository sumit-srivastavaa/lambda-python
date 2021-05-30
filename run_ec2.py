import boto3
ec2 = boto3.client('ec2')
response = ec2.run_instances(
    ImageId='ami-0d5eff06f840b45e9',
    InstanceType='t2.micro',
    KeyName = 'sumitkey',
    MinCount=1,
    MaxCount=4
    
)

response