#!/usr/bin/python3

def e_gcd(a, b, s=1, s1=0, t=0, t1=1):
    if b == 0:
        return a, s, t
    return e_gcd( b, a%b, s1, ( s - s1*(a // b) ), t1, ( t - t1*(a//b) ) )

gcd, s, t = e_gcd(32321, 26513)
print(gcd, s, t)
