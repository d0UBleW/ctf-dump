#!/usr/bin/python3

with open('msg.txt') as f:
    msg = f.read()

tx = 'rubickCTF'

key = ord(msg[0]) ^ ord(tx[0])

print("".join(chr(ord(msg[i]) ^ key) for i in range(len(msg))))

