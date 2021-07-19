#!/usr/bin/python3

with open('num.txt', 'r') as f:
    num = f.readline().split()
    for i in num:
        print(chr(int(i)),end='')
