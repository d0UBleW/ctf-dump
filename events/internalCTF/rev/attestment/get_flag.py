#!/usr/bin/python3

import os

username = "aaaaaaaa" # should be > 7

c = "S0osh62r|a9ex<m;d }}"

"""
for i in range(len(c)):
    test = test | c[i] ^ i ^ input[i]
# test should be 0
"""

f = [chr(i ^ ord(char)) for i, char in enumerate(c)]
flag = ''.join(f)

os.system(f'./Attestment {username} {flag}')

