#!/usr/bin/python3

v18 = 'ABCDEFGHIJKLMNOPQRSTUVW'
v12 = '\'1r7v/*&\'%x(?)(c51*60$/'

flag = ''

for i in range(len(v18)):
    flag += chr(ord(v12[i]) ^ ord(v18[i]))

print(flag)
