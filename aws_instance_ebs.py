#!/usr/bin/env python
# coding: utf-8

# In[1]:


import subprocess
import json


# In[4]:


def create_instance_ebs():
    instance = json.loads(subprocess.getoutput('aws ec2 run-instances --image-id ami-0ad704c126371a549 --count 1 --instance-type t2.micro --key-name amzlinux --security-group-ids sg-06f4c6f8b3f98f5bc'))
    az = instance['Instances'][0]['Placement']['AvailabilityZone']
    insid = instance['Instances'][0]['InstanceId']
    ebs = json.loads(subprocess.getoutput('aws ec2 create-volume --volume-type gp2 --size 5 --availability-zone {0}'.format(az)))
    vid = ebs['VolumeId']
    attach = subprocess.getoutput('aws ec2 attach-volume --volume-id {0} --instance-id {1} --device /dev/sdf'.format(vid,insid))
    return "Instance created and 5 GB EBS Volume Attached"


# In[ ]:




