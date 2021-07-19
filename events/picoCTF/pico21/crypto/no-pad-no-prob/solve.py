#!/usr/bin/python3

# nc mercury.picoctf.net 30048

from pwn import *

s = remote('mercury.picoctf.net', 30048)

s.recv()
tmp = s.recv().decode('UTF-8').split()
print(tmp)
print()
ciphertext = tmp[-6]
e = tmp[-8]
n = tmp[-10]

load = int(ciphertext) + int(n)
# my = 'picoCTF{}'.encode('UTF-8')
# my_enc = str(pow(int(my.hex(),16), int(e), int(n)))
# print(my_enc)
s.sendline(str(load))

flag = s.recv().decode('UTF-8').split()[-1]
print(bytes.fromhex(hex(int(flag))[2:]))

# print(n)
# print(e)
# print(ciphertext)

s.close()