#!/usr/bin/python3

known = "fs"
last = "cyberx"

alpha = "abcdefghijklmnopqrstuvwxyz"

with open('What_is_Vinegar.txt') as f:
    content = f.read()
    print(content)

cip_last = content[-6:]

key = ''


for i in range(len(last)):
    shift = (ord(cip_last[i]) - ord(last[i])) % 26
    key += alpha[shift]

print(key)

key = "cyber"

flag = ''
counter = 0

for i in range(len(content)):
    if content[i] in alpha:
        flag += alpha[(alpha.index(content[i]) - alpha.index(key[i % len(key) - counter])) % 26]
    else:
        counter += 1
        flag += content[i]

print(flag)
