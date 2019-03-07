import sys, re
if len(sys.argv) != 2:
    sys.exit('no filename')
file = open(sys.argv[1]).read()
s = re.findall(r'(?si).*?1 \(d\)', file)
for i in range(2):
    c = re.findall(r'(?si)load_const.*?\((\d*)\)', s[i])
    if i == 1:
        c = c[2:]
    c = [int(i) for i in c]
    with open('dat.py', 'a') as f:
        f.write(str(c) + '\n')
