#!/usr/bin/python3

import string

LOWERCASE_OFFSET = ord("a")
ALPHABET = string.ascii_lowercase[:16]

possible_padding = ['g', 'd']

enc = "epdfglkfnbjbhbpicohidjgkhfnejeecmjfnejddgmhpndmchbmifnepdhdmhbah"

# enc = 'bkglibgkhghkijphhhejggikgjkbhefgpienefjdioghhchffhmmhhbjgclpjfkp'


def deshift(c, k):
	t1 = ord(c) - LOWERCASE_OFFSET
	t2 = ord(k) - LOWERCASE_OFFSET
	return ALPHABET[(t1 + (16 - t2)) % len(ALPHABET)]

decd = ''
lst = []

# key = ['oedcfjdbe','obdcfjdbe']
key = ['bgabajepk', 'bgnbajepk']


# enc = "epdfglkfnbjbhbpicohidjgkhfnejeecmjfnejddgmhpndmchbmifnepdhdmhbah"
#		 bgabajepkbgabajepk

for n in range(len(key)):
	for i, c in enumerate(enc):
		tmp = deshift(c, key[n][i % len(key[n])])
		decd += tmp
	lst.append([key[n],decd])
	decd = ''

final = []

flag = ''
for j in range(len(lst)):
	for i in range(0,len(lst[j][1]),2):
		if lst[j][1][i] == 'g':
			flag += deshift(lst[j][1][i+1],'b')
		else:
			flag += str(ALPHABET.index(lst[j][1][i+1]))
	final.append([lst[j][0],flag])
	flag = ''


file = open('result.txt','w')
for i,j in final:
	print(f"key: {i}" + ", flag: picoCTF{" + f"{j}" + "}")
	file.write(f"key: {i}" + ", flag: picoCTF{" + f"{j}" + "}\n")

file.close()
