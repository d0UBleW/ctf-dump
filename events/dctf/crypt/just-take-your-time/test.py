#!/usr/bin/python3

from pwn import *
from time import time
from secrets import token_hex
from Crypto.Cipher import DES3

while True:
	r = remote('dctf-chall-just-take-your-time.westeurope.azurecontainer.io', 9999)

	a, _, b, *c = r.recv().decode().split('\n')[1].split()
	a = int(a)
	b = int(b)

	r.sendline(str(a*b))

	key = str(int(time())).zfill(16).encode()
	decrypt_this = r.recv().decode().split('\n')[1]
	decrypt_this = bytes.fromhex(decrypt_this)

	d_cipher = DES3.new(key, DES3.MODE_CFB, b'00000000')
	dec = d_cipher.decrypt(decrypt_this)

	r.sendline(dec)

	resp = r.recv()

	r.close()

	if b'Congratulations' in resp:
		break

print(resp.decode())
flag = resp.decode().split('\n')[-2]

open('flag.txt', 'w').write(flag)
