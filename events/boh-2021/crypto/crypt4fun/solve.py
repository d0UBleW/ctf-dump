#!/usr/bin/env python3


import hashlib

if __name__ == "__main__":
    f = open("flag.enc", "r")
    enc = f.read()

    second = ''
    
    hexd = "0123456789abcdef"
    for i in range(0, len(enc), 40):
        for c in hexd:
            hsh = hashlib.sha1(c.encode())
            if hsh.hexdigest() == enc[i:i+40]:
                second += c
                break

    flag = ''
    for i in range(0, len(second), 32):
        for c in range(0, 255):
            c = chr(c)
            hsh = hashlib.md5(c.encode())
            if hsh.hexdigest() == second[i:i+32]:
                flag += c
                break

    print(flag)
