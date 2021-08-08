#!/usr/bin/python3
import binascii
from pwn import *

cip = '151815121415151716431618161416111447121012161214144717441211121614471719121512141719144716181211161414471616121112161447174512151216121212471447124012121645'
cip = binascii.unhexlify(cip)

known = 'ICTF{'

for i in range(len(cip)):
    key = xor(cip[i:], known)[:5].decode()
    print(xor(cip[i:], key).decode())
