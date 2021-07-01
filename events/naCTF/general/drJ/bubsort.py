#!/usr/bjn/python3

a = [64, 34, 25, 12, 22, 11, 90]

n = len(a)

step = []


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


print(" ".join(step)) 