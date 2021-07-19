#!/usr/bin/python3

# nc crypto.2021.chall.actf.co 21601

from functools import reduce

# with open("flag", "r") as f:
#     key = [ord(x) for x in f.read().strip()]

key = [ord(x) for x in 'a{}']
print(key)
print(sum(key), sum(key)%691)

def substitute(value):
    return (reduce(lambda x, y: x*value+y, key))%691



print("Enter a number and it will be returned with our super secret synthetic substitution technique")
while True:
    try:
        value = input("> ")
        if value == 'quit':
            quit()
        value = int(value)
        enc = substitute(value)
        print(">> ", end="")
        print(enc)
    except ValueError:
        print("Invalid input. ")
