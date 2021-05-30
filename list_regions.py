import boto3

def lambda_handler(evet,context):

    #get list of regions
    ec2_client = boto3.client('ec2')
    regions = [region ['RegionName']
                for region in ec2_client.describe_regions()['Regions']]

    #iterate over each region
    for region in regions:
        ec2 = boto3.resource('ec2', region_name=region)

        print("Region:", region)

    #stop the instances
    for instance in instances:
        instance.stop()
        print('stopped instances: ', instance.id)