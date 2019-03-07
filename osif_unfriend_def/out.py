# uncompyle6 version 3.2.5
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.7.2 (default, Jan 16 2019, 21:02:05) 
# [Clang 7.0.2 (https://android.googlesource.com/toolchain/clang 003100370607242d
# Embedded file name: <script>
# Compiled at: 2018-02-25 13:25:47
print '\r[*] All friend id successfully retrieved          '
print '[*] Start'
try:
    counter = 0
    for post in posts:
        if counter >= 50:
            break
        else:
            counter += 1
        r = requests.post('https://graph.facebook.com/me/friends/%s?method=delete&access_token=%s' % (post['id'], token))
        a = json.loads(r.text)
        try:
            cek = a['error']['message']
            print W + '[' + R + post['name'] + W + '] Failed   '
        except TypeError:
            print W + '[' + G + post['name'] + W + '] Removed  '

    print '[*] done'
    bot()
except KeyboardInterrupt:
    print '\r[!] Stopped !!               '
    bot()
# okay decompiling 4.pyc
