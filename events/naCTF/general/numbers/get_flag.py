#!/usr/bin/python3

with open('encflag.txt') as f:
    tx = f.read()

print("".join(chr(int(i)-1) for i in tx.split()))
