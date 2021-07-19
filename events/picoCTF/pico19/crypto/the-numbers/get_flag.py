#!/usr/bin/python3

import string

upp = string.ascii_uppercase

enc = "16 9 3 15 3 20 6 { 20 8 5 14 21 13 2 5 18 19 13 1 19 15 14 }"
flag = ''

for i in enc.split():
	try:
		flag += upp[int(i)-1]
	except:
		flag += i

print(flag)
f = open('flag.txt', 'w')
f.write(flag+'\n')
f.close()
