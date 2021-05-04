import boto3

def lambda_handler(context,event):

    ec2_client = boto3.client('ec2')
    
    ec2 = boto3.resource('ec2', region_name='us-east-1')

    for instance in ec2.instances.all():
        l = instance.tags
        print("list:::" ,l) #[{'Key': 'Name', 'Value': 'BASTION'}]
        Rtag=l[0]['Value']
        print("required tag:::",Rtag)
        Ltag = Rtag.lower()
        if (Ltag.find('bastion') != -1):
            print("Printing instance for tag consist of bastion::",instance.id)
        else:
            print("Doesn't contain bastion tag")   
