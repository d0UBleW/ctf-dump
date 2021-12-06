#!/usr/bin/env python3

import binascii

if __name__ == "__main__":
    ct_1 = "4fd098298db95b7f1bc205b0a6d8ac15f1f821d72fbfa979d1c2148a24feaafdee8d3108e8ce29c3ce1291"
    pt_1 = "hey let's rob the bank at midnight tonight!"
    ct_2 = "41d9806ec1b55c78258703be87ac9e06edb7369133b1d67ac0960d8632cfb7f2e7974e0ff3c536c1871b"

    key = b''
    ct_1 = binascii.unhexlify(ct_1)
    ct_2 = binascii.unhexlify(ct_2)
    pt_1 = pt_1.encode()


    print(''.join(chr(ct_1[i]^pt_1[i]^ct_2[i]) for i in range(len(ct_2))))
