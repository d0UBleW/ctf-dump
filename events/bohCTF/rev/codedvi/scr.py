#!/usr/bin/python3

inp = "a"*12
string = 'Tranqulat3d'
raw_byte = b"\x02\x03\x02\x03\x05\x02\x00\x00\x00\x00\x00"
flag = ''


# print(raw_byte[0] + ord(string[0]))
i = 0

while True:
	try:
		if ( inp[i] != chr(ord(string[i]) + raw_byte[i]) ):
			flag += chr(ord(string[i]) + raw_byte[i])
		else:
			flag += inp[i]
		i += 1
	except:
		break

# print(i)
# print(len(flag))
print("apuboh{%s}" % flag)