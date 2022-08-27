#!/usr/bin/env python3

import subprocess
import socket
import os
import json
import datetime
from git import Repo

def update_ip_file(hostname, ipaddr, cur_time):
    info = {
        "hostname": hostname,
        "ip": ipaddr,
        "last_update": cur_time.strftime('%d_%b_%Y_%I:%M:%S %p')
    }
    json_obj = json.dumps(info, indent=4)
    with open(os.path.join(os.getcwd(), "{}.json".format(hostname)), "w") as outfile:
        outfile.write(json_obj)
        
def push_to_repo(hostname, cur_time):
    repo = Repo('/home/pi/mbot-ip')
    try:
        repo.git.add(all=True)
        repo.index.commit("{} auto-updating IP address at {}".format(hostname, cur_time.strftime('%d_%b_%Y_%I:%M:%S %p')))
        origin = repo.remote(name='origin')
        origin.push()
    except:
        print("Some error when pushing code")
if __name__ == '__main__':
  #######################################################

  # Retrieving information from the host

  utctoday = datetime.datetime.utcnow() #UTC
  utc2est = datetime.timedelta(hours=5)
  today = utctoday - utc2est #EST
  
  hostname = socket.gethostname()

  # Get MAC address - individual ID for each device
  str_temp = open('/sys/class/net/wlan0/address').read()
  mac = str_temp[0:17]

  arg = 'ip route list'
  p = subprocess.Popen(arg,shell=True,stdout=subprocess.PIPE)
  data = p.communicate()
  temp = str(data[0])
  split_data = temp.split()
  ipaddr = split_data[split_data.index('src')+1]

  update_ip_file(hostname, ipaddr, today)
  push_to_repo(hostname, today)    