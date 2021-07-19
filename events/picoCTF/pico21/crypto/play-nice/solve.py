#!/usr/bin/python3

from pwn import *

# nc mercury.picoctf.net 6057

SQUARE_SIZE = 6

def get_index(letter, matrix):
	for row in range(SQUARE_SIZE):
		for col in range(SQUARE_SIZE):
			if matrix[row][col] == letter:
				return (row, col)

def generate_square(alphabet):
	assert len(alphabet) == pow(SQUARE_SIZE, 2)
	matrix = []
	for i, letter in enumerate(alphabet):
		if i % SQUARE_SIZE == 0:
			row = []
		row.append(letter)
		if i % SQUARE_SIZE == (SQUARE_SIZE - 1):
			matrix.append(row)
	return matrix

def decrypt_pair(pair, matrix):
	p1 = get_index(pair[0], matrix)
	p2 = get_index(pair[1], matrix)

	if p1[0] == p2[0]:
		return matrix[p1[0]][(p1[1] - 1)  % SQUARE_SIZE] + matrix[p2[0]][(p2[1] - 1)  % SQUARE_SIZE]
	elif p1[1] == p2[1]:
		return matrix[(p1[0] - 1)  % SQUARE_SIZE][p1[1]] + matrix[(p2[0] - 1)  % SQUARE_SIZE][p2[1]]
	else:
		return matrix[p1[0]][p2[1]] + matrix[p2[0]][p1[1]]


s = remote('mercury.picoctf.net', 6057)

tmp = s.recv().decode('UTF-8').split()

alphabet = tmp[4]
enc = tmp[-1]

m = generate_square(alphabet)

enc_pair = []

for i in range(0, len(enc), 2):
	enc_pair.append(enc[i]+enc[i+1])

res = ''

for i in enc_pair:
	res += decrypt_pair(i, m)

s.recv()

s.sendline(res)

flag = s.recv().decode('UTF-8').strip().split()[-1]

f = open('flag.txt', 'w').write(flag)

s.close()