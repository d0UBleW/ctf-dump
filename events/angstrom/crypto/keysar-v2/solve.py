#!/usr/bin/python3

import string

stdalph = string.ascii_lowercase

with open("script.txt", 'r') as f:
	sample = f.read().strip()

with open("out.txt", 'r') as f:
	enc = f.read()

diction = {}

for i in range(len(sample)):
	if (sample[i] in stdalph):
		diction[enc[i]] = sample[i]

diction['e'] = 'q'
diction['l'] = 'j'
diction['n'] = 'x'
diction['p'] = 'z'

with open("enc_flag.txt", 'r') as f:
	flag = f.read()

for i in flag:
	if i in stdalph:
		print(diction[i],end='')
	else:
		print(i,end='')
