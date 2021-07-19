#!/usr/bin/python3

f = open('hx', 'r')
a = f.readlines()
print(len(a))
b = ''

for i in a:
	b += r"\x" + i.strip()

print(b)