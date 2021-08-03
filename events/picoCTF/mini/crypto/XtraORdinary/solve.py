import binascii
import time
from pwn import *

with open('output.txt') as f:
    c = f.read().strip()
    c = bytes.fromhex(c)

random_strs = [
    b'my encryption method',
    b'is absolutely impenetrable',
    b'and you will never',
    b'ever',
    b'ever',
    b'ever',
    b'ever',
    b'ever',
    b'ever',
    b'break it'
]

# The for loops make XOR the encrypted flag with strings in `random_strs`.
# However, XOR-ing a string with a bunch of other similar strings results in a pattern.
# i.e., a ^ b ^ b ^ b = a ^ b, because b ^ b cancels out each other resulting in a ^ b ^ 0 or can be written as a ^ b (xor identity).
# Hence, the encrypted flag is either being XOR-ed with the strings in `random_strs` or not.
# And come up with a solution to perform every single combination of XOR operation that can be done between the encrypted flag and the random strings
# 0000000000, 0000000001, 0000000010, ..., where the encrypted flag will be XOR-ed when the bit is 1, using the position of the `1` bit as the index of `random_strs`
combi = [ "{:010b}".format(i) for i in range(2**len(random_strs)) ]
res = []

for i in combi:
    tmp = c
    for idx, bit in enumerate(i):
        if (bit == '1'):
            tmp = xor(tmp, random_strs[idx])
    res.append(tmp)


for i in res:
    key = xor(b"picoCTF{", i)[:len("picoCTF{")] # after reviewing the result, found `Africa!A`
    if key == b'Africa!A':
        flag = xor(b"Africa!", i).decode()
        break

with open('flag.txt', 'w') as f:
    f.write(flag)
