#!/usr/bin/python3

from Crypto.Util.number import inverse
import gmpy

f = open("rsa.txt")

n, p, q, e, c = [x.strip() for x in f.readlines()]
n = int(n.split()[-1])
p = int(p.split()[-1])
q = int(q.split()[-1])
e = int(e.split()[-1])
c = int(c.split()[-1])

d = inverse(e, (p-1)*(q-1))
m = pow(c, d, n)

print(bytes.fromhex(hex(m)[2:]).decode())

#print(m.to_bytes(2, "big"))

f.close()
