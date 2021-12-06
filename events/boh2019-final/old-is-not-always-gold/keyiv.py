import base64
import hashlib

#inputs
# openssloutputb64='U2FsdGVkX1+Fqn+TvPF3Yk0Sjlcnd0YhML0EVDa+6Zg='
openssloutputb64='U2FsdGVkX1/WxiJIr4MPE1WnT3Kb8VExq6ZuuUlHMowcVGpWUNGv85Qj2RhDbM1fU/UCeWAiSaE='
password='friend'

#convert inputs to bytes
openssloutputbytes=base64.b64decode(openssloutputb64)
passwordbytes=password.encode('utf-8')
salt=openssloutputbytes[8:16]   #salt is bytes 8-15 of the ciphertext

#key derivation
D1=hashlib.md5(passwordbytes + salt).digest()
D2=hashlib.md5(D1 + passwordbytes + salt).digest()
D3=hashlib.md5(D2 + passwordbytes + salt).digest()
print(D1)
print(D2)
key=D1+D2
iv=D3
print(len(iv))

print('password:', password)
print('salt:', salt.hex().upper())
print ('key:', key.hex().upper())
print ('iv:', iv.hex().upper())
