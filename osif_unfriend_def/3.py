import dat2 # dat

d = dat2.d # dat
k = dat2.k # dat

e = ''
i,j = (0,0)

while 1:
    if i >= len(d): break
    if j >= len(k): j = 0
    e += chr(d[i] ^ k[j])
    i += 1
    j += 1

with open('4.pyc','wb') as f: # 3.pyc
    f.write('\x03\xf3\x0d\x0a\xeb\x56\x92\x5a' + e)
    print "All done..."
