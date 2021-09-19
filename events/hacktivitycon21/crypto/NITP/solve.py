#!/usr/bin/env python3

from pwn import *

# nc challenge.ctf.games 30138

p = remote("challenge.ctf.games", 30138)

enc = p.recvuntil(b">").decode().split('\n')[1].strip()
p.sendline(b"\x00")
pad = p.recvuntil(b">").decode().split('\n')[1].strip()

p.close()

enc = bytes.fromhex(enc)
pad = bytes.fromhex(pad)

print(''.join([ chr(enc[i] ^ pad[i]) for i in range(len(enc)) ]))
