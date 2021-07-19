#!/usr/bin/python3

from pwn import *

# nc jupiter.challenges.picoctf.org 29221

s = remote("jupiter.challenges.picoctf.org", 29221)

h = s.recv().decode().split("Please give the ")[-1]
h = h.split(' as')[0].split()

ans = ''
for i in h:
	ans += chr(int(i, 2))

s.sendline(ans.encode())

h = s.recv().decode().split("Please give me the  ")[-1]
h = h.split(' as')[0].split()

ans = ''
for i in h:
	ans += chr(int(i, 8))

s.sendline(ans.encode())

h = s.recv().decode().split("Please give me the ")[-1]
h = h.split(' as')[0].split()[0]

s.sendline(bytes.fromhex(h).decode().encode())

h = s.recv().decode().split("Flag: ")[-1]

f = open('flag.txt', 'w')
f.write(h)
f.close()

print(h)

s.close()
