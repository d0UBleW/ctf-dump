#!/usr/bin/python3

import binascii
from pwn import *

with open('challenge.txt') as f:
    content = f.readlines()[0].strip()

content = binascii.unhexlify(content)

for i in range(2**8):
    tmp = xor(content, i)

flag = xor(content, 33)
print(binascii.unhexlify(flag))
print(bytes.fromhex(flag.decode()).decode())
