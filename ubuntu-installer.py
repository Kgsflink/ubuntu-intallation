
import os
cmd = 'apt update'
os.system(cmd)
cmd = 'apt upgrade -y ' 
os.system(cmd)
cmd = 'termux-setup-storage -y'
os.system(cmd)
cmd = 'apt install git'
os.system(cmd) 
cmd = 'apt install wget '
os.system(cmd)
cmd = 'curl https://raw.githubusercontent.com/AndronixApp/AndronixOrigin/master/repo-fix.sh > repo.sh && chmod +x repo.sh && bash repo.sh && pkg update -y && pkg install wget curl proot tar -y && wget https://raw.githubusercontent.com/AndronixApp/AndronixOrigin/master/Installer/Ubuntu/ubuntu-xfce.sh -O ubuntu-xfce.sh && chmod +x ubuntu-xfce.sh && bash ubuntu-xfce.sh '
os.system(cmd)
cmd = 'apt autoremove python'
os.system(cmd)
