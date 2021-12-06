from hashlib import md5
with open('msg.enc', 'r') as f:
    content = [ i.strip().split(": ")[-1] for i in f.readlines() ]
    x0, y0 = content[0][1:len(content[0])-1].split(", ")
    x0 = int(x0)
    y0 = int(y0)
    coeff = int(content[1])
    msg = content[2]
    n = 18
    k = 10

c = [0, coeff]

def next_coeff(val):
    return int(md5(val.to_bytes(32, byteorder="big")).hexdigest(), 16)

for i in range(2, n+1):
    c.append(next_coeff(c[i-1]))

c = c[:k]
prime = 92434467187580489687

known = 0
for i, cf in enumerate(c):
    known += cf * x0**i

print(known)
print(y0)

ori_y0 = y0
diff = known - y0
ori_y0 += prime*(diff//prime)

# print(ori_y0 - known)
# print(ori_y0 + prime - known)

if (ori_y0 < known):
    ori_y0 += prime

secret = ori_y0 - known
found_c = [secret]
for i in range(1, n+1):
    found_c.append(next_coeff(found_c[i-1]))

print(found_c[1:10] == c[1:])

from Crypto.Cipher import AES
from random import randint, randbytes,seed
from Crypto.Util.number import bytes_to_long
from binascii import unhexlify

msg = unhexlify(msg)
seed(secret)
key = randbytes(16)
cipher = AES.new(key, AES.MODE_ECB)
dec_FLAG = cipher.decrypt(msg)
print(dec_FLAG)
