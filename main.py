#!/usr/bin/env python3
import os
import json
import argparse
import datetime
LOG_FILE="/home/pi/update_ip_log.txt"

def update_ip_file(hostname, ipaddr, cur_time):
    info = {
        "hostname": hostname,
        "ip": ipaddr,
        "last_update": cur_time.strftime('%d_%b_%Y_%I:%M:%S %p')
    }
    with open(LOG_FILE, 'w') as f:
        f.write(hostname)
        f.write(ipaddr)
        f.write(cur_time.strftime('%d_%b_%Y_%I:%M:%S %p'))
    json_obj = json.dumps(info, indent=4)
    with open(os.path.join(os.getcwd(), "{}.json".format(hostname)), "w") as outfile:
        outfile.write(json_obj)
        
# def push_to_repo(hostname, cur_time):
#     repo = Repo('/home/pi/mbot-ip')
#     try:
#         repo.git.add(all=True)
#         repo.index.commit("{} auto-updating IP address at {}".format(hostname, cur_time.strftime('%d_%b_%Y_%I:%M:%S %p')))
#         origin = repo.remote(name='origin')
#         origin.push()
#     except:
#         print("Some error when pushing code")
if __name__ == '__main__':
    with open(LOG_FILE, 'w') as f:
        f.write("RUNNING...")
    parser = argparse.ArgumentParser()
    parser.add_argument("-hostname", type=str, help="Hostname of this bot")
    parser.add_argument("-ip", type=str, help="IP of this bot")
    args = parser.parse_args()
    utctoday = datetime.datetime.utcnow() #UTC
    utc2est = datetime.timedelta(hours=5)
    today = utctoday - utc2est #EST
    update_ip_file(args.hostname, args.ip, today)


  #######################################################

#   # Retrieving information from the host

  
#   hostname = socket.gethostname()

#   # Get MAC address - individual ID for each device
#   str_temp = open('/sys/class/net/wlan0/address').read()
#   mac = str_temp[0:17]

#   arg = 'ip route list'
#   p = subprocess.Popen(arg,shell=True,stdout=subprocess.PIPE)
#   data = p.communicate()
#   temp = str(data[0])
#   split_data = temp.split()
#   ipaddr = split_data[split_data.index('src')+1]

#   
#   push_to_repo(hostname, today)    
