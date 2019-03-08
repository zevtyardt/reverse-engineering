import re
x = open('3.dis').read()
o = ''.join(re.findall(r'\(\'(.*?)\'\)', x))[9:][:-28]
# decode string: .decode("hex").decode("u8")
s = o.decode("hex").decode("u8")
with open('out.py', 'w') as f:
    f.write(s)
