#!/usr/bin/python3

# Due to the key is bitwise `and`ed with 0x1F, the 3 MSB of the result value after the plaintext is xored will be the same as the plaintext

enc = open('output.bin').read()

lst = []
idx = []
n = 1
for i in enc:
	tmp = bin(ord(i))[2:].zfill(8)
	if (tmp[:3] == '001'):
		lst.append((n, tmp[3:]))
		idx.append(n)
	n += 1

print(lst)

length = 8

chk = []
while (length < 33):
	for ind, j in lst:
		if (ind <= length):
			i = 1
			while (ind+length*i <= len(enc)):
				if (ind+length*i in idx):
					if (j == lst[idx.index(ind+length*i)][1]):
						print(ind, ind+length*i, length)
				i += 1
		else:
			break
	
	length += 1
	
# guess length = 32

get_id = []
for i in idx:
	if (i%32 not in get_id):
		get_id.append(i%32)

get_id.sort()
print(get_id)
print(len(get_id))
