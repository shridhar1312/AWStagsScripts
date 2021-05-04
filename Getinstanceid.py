#here we want to list containers based on tags with name bastion and other tags should not have tag "createdby:spotinst:aws:ec2:group"

#Have managed to get list of tags for instance-->next part is make if condition that will iterate over each list

import boto3

def lambda_handler(context,event):

    ec2_client = boto3.client('ec2')
    
    ec2 = boto3.resource('ec2', region_name='us-east-1')

    for instance in ec2.instances.all():
        l = instance.tags
        #print("list:::" ,l) 

# Making list of tags in one list
        list = [ ]
        for iter in l:
            #print("RTag:::",iter['Value'])
            Rtag = iter['Value']
            list.append(Rtag)
        print("final list:::",list)
        for tagg in list:
            print("tagg",tagg)
            Ltag=tagg.lower()
            print("Ltag:::::",Ltag)
            # if ((Ltag.find('bastion') != -1 ) and (Ltag != 'spotinst:aws:ec2:group' )):
            #     print("Printing instance for tag consist of bastion::",instance.id)
            # else:
            #     print("Doesn't contain bastion tag")
           
