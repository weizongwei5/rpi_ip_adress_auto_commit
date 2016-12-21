# -*- coding: utf-8 -*-
# @weizongwei5
###############################################################################


import socket
import os
import getpass
import time
import urllib2


def get_ip_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    return s.getsockname()[0]

def get_current_time():
    ISOTIMEFORMAT ='%Y-%m-%d %X'
    return time.strftime(ISOTIMEFORMAT, time.localtime())

def internet_on():
    try:
        urllib2.urlopen('http://baidu.com', timeout=1)
        return True
    except urllib2.URLError as err:
        print "network not connected!!\n 网络没连接！！"
        return False

i = 1
while(i <= 10):
    is_valid=(internet_on())
    if(is_valid):
        i=11
    time.sleep(3)
    i += 1

username = getpass.getuser()
separator = "/"

ip_adress = get_ip_address()  # current ip
cur_dir = os.getcwd()  # current dir
git_dir = "/home/" + username + "/git"

print(ip_adress+" "+ get_current_time()+"\n")
os.chdir(git_dir + separator + "rpi_ip_adress_auto_commit")  # change dir

os.system('git pull')

fp = open('ip.txt', 'w')
fp.write(ip_adress +" "+ get_current_time()+"\n")
fp.close()

os.system('git add -A')

os.system("git commit -m \'ip commit on " + socket.gethostname() + "\'")

os.system('git push')
