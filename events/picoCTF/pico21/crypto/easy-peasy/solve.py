#!/usr/bin/python3

from pwn import *

s = remote("mercury.picoctf.net", 64260)

s.recv()
enc_flag = bytes.fromhex(s.recv().decode('UTF-8').split('\n')[1])
b49968 = 'a'*49968
s.sendline(b49968)
s.recvuntil(b'\nWhat data would you like to encrypt? ')
s.sendline(enc_flag)
tmp = bytes.fromhex(s.recv().decode('UTF-8').split('\n')[-2]).decode('UTF-8')
flag = "picoCTF{"+tmp+"}"
f = open('flag.txt', 'w').write(flag)
print("flag.txt created.")

s.close()

# flag xor key = enc_flag
# enc_flag xor key = flag
# enc_flag length = 64 in {:02x} format meaning the flag is 32 bytes long
# hence, the key used to xor the flag starts from index 0 up to 31 and now our key_location is equal to 32
# we need to bring it back to the beginning by passing 50000 - 32 = 49968 bytes long payload due to the modulus operator
# then we give the encrypted flag such that it is xored by the correct key to get back the flag