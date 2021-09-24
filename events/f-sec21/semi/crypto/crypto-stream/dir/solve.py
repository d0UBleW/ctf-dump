with open('flag.enc', 'r') as f:
    con = f.read()

con = bytes.fromhex(con)

known = b'fs'

n1 = con[0] ^ known[0]
n2 = con[1] ^ known[1]


import random

for i in con:
    print(chr(i ^ n1), end='')
    random.seed(n1)
    n1 = n2
    n2 = random.randint(0, 255)
