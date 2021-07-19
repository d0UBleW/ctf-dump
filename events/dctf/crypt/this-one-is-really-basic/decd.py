#!/usr/bin/python3

import base64

cip = open('cipher.txt').read()

while True:
	try:
		cip = base64.b64decode(cip)
	except:
		break

print(cip.decode())

open('flag.txt', 'w').write(cip.decode())
