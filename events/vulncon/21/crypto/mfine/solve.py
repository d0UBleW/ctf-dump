#!/usr/bin/env python3

import json
import re
import sympy
from pprint import pprint

# def gcd(a, b):
#     if b == 0:
#         return a
#     return gcd(b, a%b)

# def modInvPrime(a, b):
#     return pow(a, b-2, b)

if __name__ == "__main__":
    dist = [' ', 'E', 'T', 'A', 'O', 'I', 'N', 'S', 'R', 'H', 'D', 'L', 'U', 'C', 'M', 'F', 'Y', 'W', 'G', 'P', 'B', 'V', 'K', 'X', 'Q', 'J', 'Z']
    print(dist)

    ciphertext = open("cipher.txt").read().replace('\n', '')

    ALPHA = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ{}_ #"

    m = len(ALPHA)

    freq_result = []
    for i in range(1, m):
        modInv = sympy.mod_inverse(i, m)
        for j in range(m):
            plaintext = ''
            freq = {k: 0 for k in ALPHA}
            for letter in ciphertext:
                idx = ALPHA.index(letter)
                x = (modInv * (idx - j)) % m
                plaintext += ALPHA[x]
                freq[ALPHA[x]] += 1
            result = re.findall("VULNCON{.*}", plaintext)
            if len(result) > 0:
                print(result)

            for k, v in freq.items():
                freq[k] = v / len(ciphertext)
            freq = {k: v for k, v in sorted(freq.items(), key=lambda x: x[1], reverse=True)}
            verify = len(list(filter(lambda x: list(freq.keys())[x[0]] == x[1], enumerate(dist))))
            freq_result.append(((i, j), verify, plaintext))

    pprint(sorted(freq_result, key=lambda x: x[1]))
