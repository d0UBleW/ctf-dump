#!/usr/bin/python3

flag = open('enc', 'r').read()

for i in flag:
	c1 = str(hex(ord(i)))[2:4]
	c2 = str(hex(ord(i)))[4:]
	print(chr(int(c1, 16)) + chr(int(c2, 16)), end='')

'''
Encryption: ''.join([chr((ord(flag[i]) << 8) + ord(flag[i + 1])) for i in range(0, len(flag), 2)])
Given a pair of characters, the first character is shifted 8 bits to the left then it is added with the second characters ascii value
normal ASCII character is 8-bit long, 0110 0001 = 'a', shifted 8 bits to the left, resulting in
0110 0001 0000 0000. Then, added with the ASCII value of another character. Hence, forming 16-bit long character,
with 8 MSB representing first character and 8 LSB representing the second character
'''