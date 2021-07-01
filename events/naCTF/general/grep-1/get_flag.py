#!/usr/bin/python3




with open('flag.txt') as f:
	msg = f.read()


a = msg.split('\n')

for i in range(len(a)):
	if(len(a[i]) == 52):
		b = a[i].split('{')[1]
		lef = b[:10]
		lef = set(lef)
		rev = b[::-1]
		rig = rev[1:15]
		rig = set(rig)
		if(len(lef) == 3 and len(rig) == 3 and 'a' in lef and 'n' in lef and 'c' in rig and 't' in rig and 'f' in rig and 'c' in lef):
			print(lef, rig)
			print(a[i])
			print()

# b = a[0].split('{')[1]
# lef = b[:10]
# lef = set(lef)
# rev = b[::-1]
# rig = rev[1:15]
# print(b)
# print(lef)
# print(rig)
print(len("nactf{caancanccnxfynhtjlgllctekilyagxctftcffcfcctft}"))