import dis, re, sys
x = sys.argv[1]
disaFor = 'import marshal, dis\ndis.dis(marshal.loads(b{0}), file=open("{1}.py", "w"))'
count = 1
while True:
    file = open(x + '.py', 'r').read()
    exec (disaFor.format(re.search(r'((?<![\\])[\'"])((?:.(?!(?<![\\])\1))*.?)\1', file).group(), 'hasil_2'))
    print ('all done..percobaan ke %s' % count)
    x = 'hasil_2'
    count += 1