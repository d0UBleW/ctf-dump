from pwn import *
from base64 import b64decode
from Crypto.Cipher import AES

# nc pwn-2021.duc.tf 31914

p = remote("pwn-2021.duc.tf", 31914)

p.recvuntil(b"Enter plaintext:\n")

key = b""
# key = b"!_SECRETSOURCE_!"

# enc_flag = b'\xf0\xc0*\xde\x91\xac\xef\xf2\x93r\xfd\x1c\xde(\xeaL\x98o\xff?U\xf1\x00;\x97\xd4\xe42E;\xd9\x82'

# cipher = AES.new(key, AES.MODE_ECB)
# pt = cipher.decrypt(enc_flag)
# print(pt)

while len(key) < 16:
    for i in range(32, 127):
        print(i, key)
        guess = i.to_bytes(1, "big")
        msg = guess + key
        pad = b'0'*(16-len(msg))
        dummy = b'a'*(1+len(key))
        payload = msg + pad + dummy
        print(guess, payload)
        p.sendline(payload)
        p.clean()
        out = p.recvuntil(b"Enter plaintext:\n").split(b"\n")[-3]
        out = b64decode(out)
        print(out[32:48], out[64:])
        print()
        if out[32:48] == out[64:]:
            key = msg
            break

# p.close()

# for i in out:
#     print(b64decode(i))
