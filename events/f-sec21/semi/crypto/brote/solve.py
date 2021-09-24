import hashlib

target = "6ef11bc47eadba4c9c4c44f1e4aaa84f"

a = "abcdefghijklmnopqrstuvwxyz0123456789"


import itertools

test = itertools.product(a, a, repeat=1)
for i in test:
    for j in a:
        tmp = ''.join(i) + j + 'c'
        s = tmp
        tmp = tmp.encode()
        tmp = hashlib.sha1(tmp).hexdigest().encode('utf-8')
        if (hashlib.md5(tmp).hexdigest() == target):
            print(s)
            break

