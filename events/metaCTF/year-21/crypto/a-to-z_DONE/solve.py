#!/usr/bin/env python3

import string
import json

def rot(ct):
    res = {}
    for i in range(26):
        pt = ''
        for char in ct:
            if char in string.ascii_lowercase:
                idx = string.ascii_lowercase.index(char)
                pt += string.ascii_lowercase[(idx + i) % 26]
            elif char in string.ascii_uppercase:
                idx = string.ascii_uppercase.index(char)
                pt += string.ascii_uppercase[(idx + i) % 26]
            else:
                pt += char
        res[i] = pt
    return res

def atbash(ct):
    lower = {k: v for k, v in zip(string.ascii_lowercase, string.ascii_lowercase[::-1])}
    upper = {k: v for k, v in zip(string.ascii_uppercase, string.ascii_uppercase[::-1])}
    pt = ''
    for char in ct:
        if char in lower.keys():
            pt += lower[char]
        elif char in upper.keys():
            pt += upper[char]
        else:
            pt += char
    return pt



if __name__ == "__main__":
    ct = "yzhsufo_rh_nb_uze_wdziu"
    res = rot(ct)
    print("ROT13")
    print("=====")
    print(json.dumps(res, indent=4))
    
    print("\n\nAtbash")
    print("======")
    print(atbash(ct))
