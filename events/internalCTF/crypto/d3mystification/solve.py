#!/usr/bin/python3

from Crypto.PublicKey import RSA
from base64 import b64decode

with open('ci.txt', 'r') as f:
    content = f.read()

print(b64decode(content))

#key = RSA.importKey(content)
#print(key)
