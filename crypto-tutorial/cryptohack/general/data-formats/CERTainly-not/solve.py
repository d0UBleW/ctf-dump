#!/usr/bin/python3

with open('modulus.txt') as f:
    mod = f.read()

print(int(mod, 16))
