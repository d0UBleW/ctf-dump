#!/usr/bin/python3

# nc mercury.picoctf.net 4572

from pwn import *
import gmpy

s = remote('mercury.picoctf.net', 4572)

enc_flag = s.recvuntil("\n").decode('UTF-8').split()[-1].strip()
n = s.recvuntil('\n').decode('UTF-8').split()[-1].strip()
e = s.recvuntil('\n').decode('UTF-8').split()[-1].strip()

s.recv()

new = int(enc_flag) % int(n)

x = 'aa'

y = pow(int(x.encode().hex(),16), int(e), int(n))

i = 0
while i < 10:
	s.sendline('aa')
	res = s.recvuntil('\n').decode('UTF-8').split()[-1].strip()
	res = int(res) % int(n)
	print(res)
	print(y)
	print()
	# print(s.recv())
	i += 1
print(n)
print(e)


s.close()

