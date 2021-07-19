#!/usr/bin/python3

import string
import itertools

LOWERCASE_OFFSET = ord("a")
ALPHABET = string.ascii_lowercase[:16]

hand = open('ky.txt','w')

def deshift(c, k):
	t1 = ord(c) - LOWERCASE_OFFSET
	t2 = ord(k) - LOWERCASE_OFFSET
	return ALPHABET[(t1 + (16 - t2)) % len(ALPHABET)]

def shift(c, k):
	t1 = ord(c) - LOWERCASE_OFFSET
	t2 = ord(k) - LOWERCASE_OFFSET
	return ALPHABET[(t1 + t2) % len(ALPHABET)]


def offset(c):
    x = [ord('d'), ord('g')]
    off = []
    for i in x:
        if (ord(c) >= i):
            off.append(ALPHABET[ord(c)-i])
        else:
            off.append(ALPHABET[(16-(i-ord(c)))])
    return off

possible_padding = ['g', 'd']

crack = False

# enc = 'bkglibgkhghkijphhhejggikgjkbhefgpienefjdioghhchffhmmhhbjgclpjfkp'
enc = 'epdfglkfnbjbhbpicohidjgkhfnejeecmjfnejddgmhpndmchbmifnepdhdmhbah'
# bkglibgkhghkijphhhejggikgjkbhefgpienefjdioghhchffhmmhhbjgclpjfkp
# o d f d e e c j b 
# oedcfjdbe
#  n n n n n n l l l
# o d f d e b c j b o d f d e b c j b o d f d e b c j b o d f d b
# obdcfjdbe

# bgighhiph egigkhfpe ejighhfmh bgljk
# odfdeecjb odfdeecjb odfdeecjb odfde

# bgighhiph egigkhfpe ejighhfmh bgljk
# odfdebcjb odfdebcjb odfdebcjb odfde

enc_pad = ''

for i in range(0,len(enc),2):
    enc_pad += enc[i]
# print(enc_pad)

emp = []
comb = []
for i in enc_pad:
    emp.append(offset(i))
print(emp)

count = 0
for j in range(1,14):
    tmp = emp[:j]
    for i in itertools.product(*tmp):
        hand.write(' '.join(i)+'\n')
        count += 1
# print(count)


hand.close()

rs = []
z = open('ky.txt','r').readlines()

for i in z:
    j = ''.join(i.strip().split())
    for x, y in enumerate(enc_pad):
        mpt = deshift(y, j[x % len(j)])
        if mpt not in possible_padding:
            break
        if x == len(enc_pad)-1:
            rs.append(j)

print(rs)
fileh = open('posk.txt', 'w')
for i in rs:
    fileh.write(i+'\n')
