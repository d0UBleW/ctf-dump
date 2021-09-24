#!/usr/bin/python3

"""
use ssh-keygen to convert bruce_rsa.pub to PEM
```
$ ssh-keygen -f bruce_rsa.pub -e -m pem > bruce.pem
```
"""

from Crypto.PublicKey import RSA

with open('bruce.pem') as f:
    keyDER = f.read()

key = RSA.importKey(keyDER)

print(key.n)
