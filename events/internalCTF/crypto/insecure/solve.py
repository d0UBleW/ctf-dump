#!/usr/bin/python3

from Crypto.PublicKey import RSA
from base64 import b64decode

f = open('base')
base = f.read()
keyDER = b64decode(base)
print(keyDER)
f.close()
#key = RSA.importKey(keyDER)
#print(key.d)
