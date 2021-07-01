#!/usr/bin/python3

with open("output.txt") as f:
	tx = f.read().split("\n")


print("picoCTF{%s}" % ("".join(chr(int(i)) for i in tx)))