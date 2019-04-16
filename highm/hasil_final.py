N = '\x1b[0m'
R = '\x1b[1;37m\x1b[31m'
G = '\x1b[1;32m'
B = '\x1b[1;37m\x1b[34m'

import marshal
banner = ("""
%s
   /\  /(_) __ _| |__   /\/\
  / /_/ / |/ _` | '_ \ /    \
 / __  /| | (_| | | | / /\/\ \
 \/ /_/ |_|\__, |_| |_\/    \/
           |___/
%s
""" % (B, N))
print (banner)
counter = 0
file = str(input('Path file » '))
any = str(input('Any type » ')).encode()
count = int(input('Count marshal » '))
if count < 400:
    out = str(input('Output » '))
    od = open(file).read()
    cpanel = compile(od, '<%s>' % any, 'exec')
    dor = marshal.dumps(cpanel)
    results = repr(dor)
    s = open(out, 'w')
    s.write('import marshal\nexec(marshal.loads(' + str(results) + '))')
    s.close()
    while True:
        if count >= counter:
            ops = open(out).read()
            cc = compile(ops, '<%s>' % any, 'exec')
            pp = marshal.dumps(cc)
            res = repr(pp)
            print ('%s%s%s' % (R, counter, N))
            wrote = open(out, 'w')
            wrote.write('import marshal\nexec(marshal.loads(' + str(res) + '))')
            wrote.close()
            counter += 1
        else:
            break # POP_BLOCK
    print ('%sSuccess%s' % (G, N))
else:
    exit()