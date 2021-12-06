#!/usr/bin/env python3

from Crypto.Util.number import inverse, long_to_bytes


if __name__ == "__main__":
    ct = 0x2526512a4abf23fca755defc497b9ab
    e = 257
    n = 0x592f144c0aeac50bdf57cf6a6a6e135
    phi = 7409108828132483917965783712161745440
    d = inverse(e, phi)
    pt = long_to_bytes(pow(ct, d, n)).decode()
    print(f"MetaCTF{{{pt}}}")
