#!/usr/bin/python3

xored = '7432717d2a7f266e5b3556b432617f33ac87e6b4'
xored = [xored[i:i+2] for i in range(0, 40, 2)]

a = lambda n: a(n-2) + a(n-1) if n >= 2 else (2 if n == 0 else 1)

print('sdctf{', end='')
for i in range(20):
	print(chr((a(i) & 0xff) ^ int(xored[i],16)), end='')

print('}')
