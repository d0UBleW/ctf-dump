#!/usr/bin/python3

from pwn import *

# nc crypto.2021.chall.actf.co 21600

s = remote('crypto.2021.chall.actf.co', 21600)



s.close()