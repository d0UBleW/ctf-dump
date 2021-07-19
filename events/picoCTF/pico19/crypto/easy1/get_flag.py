#!/usr/bin/python3

import string

upp = string.ascii_uppercase

def table():
	mat = []
	for i in range(26):
		mat.append([x for x in (upp[i:]+upp[:i])])
	return mat

mytable = table()

enc = "UFJKXQZQUNB"
key = "SOLVECRYPTO"

message = ''

for i in range(len(enc)):
	message += upp[mytable[upp.index(key[i % len(key)])].index(enc[i])]
	
flag = "picoCTF{{{}}}".format(message)
print(flag)

f = open('flag.txt', 'w')
f.write(flag+'\n')
f.close()
