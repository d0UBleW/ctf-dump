import os
import time
import zlib
def keystream(key):
	index = 0
	while 1:
		index+=1
		if index >= len(key):
			key += zlib.crc32(key).to_bytes(4,'big')
		yield key[index]

with open('enc', 'rb') as f:
	ciphertext = f.read()

plain = []
for j in range(65536):
	kb = j.to_bytes(2, 'big')
	k = keystream(kb)
	for i in ciphertext:
		plain.append(i ^ next(k))
	
	m = bytes(plain)
	if (b'acf{' in m):
		print(m)
		break
	plain = []
