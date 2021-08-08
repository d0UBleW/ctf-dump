#!/usr/bin/python3

from pwn import *

with open('challenge.txt') as f:
    content = f.readlines()[0].strip()

content = bytes.fromhex(content)
known = b"ICTF{"

plain = b''
for i in range(len(content)):
    plain += xor(content[i], known[ i % len(known) ])

with open('output.txt', 'wb') as f:
    f.write(plain)
