#!/usr/bin/python3
import binascii
from pwn import *
import time
import re

with open("hex_chal.txt") as f:
    content = ''.join(f.read().split())

with open('result.txt', 'w') as f:
    pass

content = binascii.unhexlify(content)

known = "ICTF{"

for i in range(len(content)):
    key = xor(content[i:], known)[:5].decode()
    res = xor(content[i:], key).decode()
    match = re.findall('ICTF{.*}', res)
    if (match != []):
        with open('result.txt', 'a') as f:
            f.write(f"{match=}\n{key=}\n")
        print(f"{match=}\n{key=}\n")
