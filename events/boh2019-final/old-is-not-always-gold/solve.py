import base64
import hashlib
from Crypto.Cipher import DES3

b64_encoded_ciphertext = "U2FsdGVkX1/WxiJIr4MPE1WnT3Kb8VExq6ZuuUlHMowcVGpWUNGv85Qj2RhDbM1fU/UCeWAiSaE="
passphrase = "friend"

# base64 decode to give the raw bytes of the ciphertext
ciphertext = base64.b64decode(b64_encoded_ciphertext)

# passphrase must be raw bytes too
passphrase = passphrase.encode('utf-8')

# the 8 bytes following "Salted__" in the ciphertext are the salt
salt = ciphertext[8:16]

# we hash a couple of times
round1 = hashlib.md5(passphrase + salt).digest()
round2 = hashlib.md5(round1 + passphrase + salt).digest()
print(round1)
print(round2)

# sum the two rounds
final_hash = round1 + round2
print(final_hash)

# the key is the first 24 bytes of that final hash
key = final_hash[0:24]

# and the iv is the remaining 8
iv = final_hash[24:]

import binascii
print(binascii.hexlify(key).upper())
print(binascii.hexlify(iv).upper())
print([i for i in key])
print(','.join(str(i) for i in key))
print(','.join(str(i) for i in iv))
print(len(iv))
print(len(key))
# cipher = DES3.new(key, DES3.MODE_CTR, iv)
# print(cipher.decrypt(ciphertext))
