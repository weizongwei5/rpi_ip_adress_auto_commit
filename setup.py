#!/usr/bin/env python3
# @weizongwei5
# Launch python script on startup
###############################################################################

import getpass
import os
import time


username = getpass.getuser()
config=".config"
autostart="autostart"


sp="/"

userhome = "/home/"+ username
# userhome = "/home/"+ username +"/testrpi"
config_dir = userhome + sp + config
autostart_dir = config_dir + sp + autostart
git_dir=userhome + sp + "git" + sp + "rpi_ip_adress_auto_commit"

os.chdir(userhome)

os.system("mkdir "+config)
os.chdir(config_dir)

os.system("mkdir "+autostart)
os.chdir(autostart_dir)

fp = open('auto_commit_ip_address2github.desktop', 'w') 
fp.write(
"[Desktop Entry] "+"\n"+
" Name=ScanTest "+"\n"+
" Comment=My Python Program "+"\n"+
" Exec=python "+git_dir+"/autogetip_and_commit.py" +"\n"+
"Terminal=true"+"\n"+
"MultipleArgs=false"+"\n"+
"Type=Application"+"\n"+
"Categories=Application;Development;"+"\n"+
"StartupNotify=true")
 
fp.close()

