#!/usr/bin/python3

from pwn import *
import re


s = remote('challenges.ctfd.io', 30267)

s.recv()
s.sendline("2")

z = 0

while True:
	prompt = s.recv().decode("utf-8")
	if("STAGE" in prompt):
		if(z == 0):
			b = prompt.split("\n\n")[1].split(", ")
		else:
			b = prompt.split("\n\n")
			b = b[1].split('\n')[1].split(", ")

		lst = []

		for j in range(len(b)):
		    for i in range(1, len(b)):
		        if b[i] < b[i-1]:
		            tmp = b[i]
		            b[i] = b[i-1]
		            b[i-1] = tmp
		            lst.append(str(i-1))

		ans = " ".join(lst)

		s.sendline(ans)
	else:
		flag = re.findall(r'nactf{.*}', prompt)[0]
		print(flag)
		break
	z += 1

s.close()