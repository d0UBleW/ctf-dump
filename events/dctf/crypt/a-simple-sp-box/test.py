#!/usr/bin/python3

from pwn import *

r = remote('dctf1-chall-sp-box.westeurope.azurecontainer.io', 8888)

resp = r.recv()
print(resp)
msg = resp.decode().split('\n')[-2]
print(msg)
print(len(msg))


r.close()
