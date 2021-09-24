#!/usr/bin/env python3

import chall_2
import binascii

'''
Implement repeating-key XOR
'''

pt = '''Burning 'em, if you ain't quick and nimble
I go crazy when I hear a cymbal'''

pt = pt.encode()

key = bytearray(b"ICE")

ext_key = bytearray(b'\x00'*len(pt))

for i in range(len(pt)):
    ext_key[i] = key[i % len(key)]

ext_key = bytes(ext_key)

out = chall_2.fixed_XOR(pt, ext_key)

print(binascii.hexlify(out))
