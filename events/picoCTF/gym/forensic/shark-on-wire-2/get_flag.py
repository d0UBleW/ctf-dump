#!/usr/bin/python3

with open('output.txt') as f:
	a = f.read().split("\n")

print("".join(chr(int(i)) for i in a))