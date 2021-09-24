#!/usr/bin/python3

# a**2 = int mod p

p = 29
ints = [14, 6 , 11]

qr = [ sr for sr in range(p) if (pow(sr, 2, 29) in ints) ]

print(min(qr))
