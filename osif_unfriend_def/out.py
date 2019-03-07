print ('\r[*] All friend id successfully retrieved          ')
print ('[*] Start')
try:
    counter = 0
    for post in posts:
        if counter >= 50:
            break
        else:
            counter = counter + 1
        r = requests.post('https://graph.facebook.com/me/friends/%s?method=delete&access_token=%s' % (post['id'], token))
        a = json.loads(r.text)
        try:
            cek = a['error']['message']
            print (W + '[' + R + post['name'] + W + '] failed')
        except TypeError:
            print (W + '[' + G + post['name'] + W + '] removed')
    print ('[*] done')
    bot()
except KeyboardInterrupt:
    print ('\r[!] Stopped !!               ')
    bot()
