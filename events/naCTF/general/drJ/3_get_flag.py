#!/usr/bin/python3

from pwn import *
import re


s = remote('challenges.ctfd.io', 30267)

s.recv()
s.sendline("3")

z = 0

while True:
	prompt = s.recv().decode("utf-8")
	print(prompt)
	if("STAGE" in prompt):
		if(z == 0):
			a = prompt.split("\n\n")[1].split(", ")
			print(a)
		else:
			a = prompt.split("\n\n")
			a = b[1].split('\n')[1].split(", ")

		step = []
		n = len(a)
		
		for i in range(n-1):
			for j in range(n-1-i):
				if ( a[j] < a[j+1] ):
					step.append("c")
				else:
					tmp = a[j+1]
					a[j+1] = a[j]
					a[j] = tmp
					step.append("s")
					step.append("c")
			for k in range(i+1):
				step.append("c")

		ans = " ".join(step)
		print(ans)

		s.sendline(ans)
	else:
		flag = re.findall(r'nactf{.*}', prompt)[0]
		print(flag)
		break
	z += 1

s.close()