#!/usr/bin/env python3

import urllib.parse
import base64
from pwn import *
import string

rot13 = lambda x: chr((ord(x) - ord('a') + 13) % 26 + ord('a'))

# nc pwn-2021.duc.tf 31905

p = remote("pwn-2021.duc.tf", 31905)

p.recvuntil(b"quiz...")
p.sendline(b"")
p.recvline()
p.recvline()
p.sendline(b"2")
p.recvuntil(b": ")
d = p.recvline().strip()
d = int(d.decode(), 16)
p.sendline(str(d).encode())
p.recvuntil(b": ")
d = p.recvline().strip()
d = int(d.decode(), 16)
p.sendline(chr(d).encode())
p.recvuntil(b": ")
d = p.recvline().strip().decode()
d = urllib.parse.unquote(d).encode()
p.sendline(d)
p.recvuntil(b": ")
d = p.recvline().strip().decode()
d = base64.b64decode(d)
p.sendline(d)
p.recvuntil(b": ")
d = p.recvline().strip()
d = base64.b64encode(d)
p.sendline(d)
p.recvuntil(b": ")
d = p.recvline().strip().decode()
d = ''.join([ rot13(c) if c in string.ascii_lowercase else c for c in d ])
p.sendline(d.encode())
p.recvuntil(b": ")
d = p.recvline().strip().decode()
d = ''.join([ rot13(c) if c in string.ascii_lowercase else c for c in d ])
p.sendline(d.encode())
p.recvuntil(b": ")
d = p.recvline().strip().decode()
d = str(int(d, 2))
p.sendline(d.encode())
p.recvuntil(b": ")
d = p.recvline().strip().decode()
d = bin(int(d))
p.sendline(d.encode())
p.recvline()
p.recvline()
p.recvline()
p.sendline(b"DUCTF")
while True:
    try:
        print(p.recvline())
    except:
        break

p.close()
