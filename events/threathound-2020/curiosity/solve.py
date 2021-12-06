#!/usr/bin/env python3

from Crypto.PublicKey import RSA

with open("outder","r") as f:
    key = RSA.importKey(f.read())
