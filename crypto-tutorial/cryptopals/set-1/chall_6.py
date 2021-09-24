#!/usr/bin/env python3

import chall_2
from base64 import b64decode

def bit_diff(bs1, bs2):
    '''
    bs1: byte string 1
    bs2: byte string 2

    bs1 and bs2 must have the same length

    returns the number of differing bits
    '''
    # assert len(bs1) == len(bs2), "Strings are not the same length"

    out = chall_2.fixed_XOR(s1, s2)

    return sum(bin(b).count('1') for b in out)

if __name__ == "__main__":
    s1 = b"this is a test"
    s2 = b"wokka wokka!!!"
    print(bit_diff(s1, s2))

    with open('6.txt') as f:
        content = f.read().strip()

    print(b64decode(content))

