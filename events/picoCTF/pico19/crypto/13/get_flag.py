#!/usr/bin/python3

import string

lowerc = string.ascii_lowercase
upperc = string.ascii_uppercase

enc = "cvpbPGS{abg_gbb_onq_bs_n_ceboyrz}"

flag = ''

for i in enc:
	if i in lowerc:
		flag += lowerc[(lowerc.index(i) + 13) % 26]
	elif i in upperc:
		flag += upperc[(upperc.index(i) + 13) % 26]
	else:
		flag += i

print(flag)

f = open('flag.txt', 'w')
f.write(flag+'\n')
f.close()
