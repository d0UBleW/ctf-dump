#!/usr/bin/python3

import string

lowerc = string.ascii_lowercase
upperc = string.ascii_uppercase

f = open('ciphertext')
enc = f.read()[8:-1]


for offset in range(26):
	flag = ''
	for i in enc:
		if i in lowerc:
			flag += lowerc[(lowerc.index(i) + offset) % 26]
		elif i in upperc:
			flag += upperc[(upperc.index(i) + offset) % 26]
		else:
			flag += i
	print(flag)

# offset 25 is the ansewr

flag = "picoCTF{{{}}}".format(flag)
print("\nFlag:", flag)

f = open('flag.txt', 'w')
f.write(flag+'\n')
f.close()
