import dat

d = dat.d
k = dat.k

e = ''
i,j = (0,0)

while 1:
    if i >= len(d): break
    if j >= len(k): j = 0
    e += chr(d[i] ^ k[j])
    i += 1
    j += 1

with open('3.pyc','wb') as f:
    f.write('\x03\xf3\x0d\x0a\xeb\x56\x92\x5a' + e)
    print "All done..."
