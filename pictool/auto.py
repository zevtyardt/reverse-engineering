import dis, re, sys, base64
x = sys.argv[1]
disaFor = 'import marshal, dis\ndis.dis(marshal.loads(b"{0}"), file=open("{1}.py", "w"))'
count = 1
while True:
    file = open(x + '.py', 'r').read()
    string = re.findall(r'((?<![\\])[\'"])((?:.(?!(?<![\\])\1))*.?)\1', file)

    if not 'marshal' in file:
        bs = base64.b64decode(string[1][1])
        with open( 'hasil.py', 'wb') as f:
            f.write(bs)
        print ('all done..percobaan ke %s, base64' % count)
    else:
        exec (disaFor.format(string[0][1], 'hasil'))
        print ('all done..percobaan ke %s, marshal' % count)
    x = 'hasil'
    count += 1
