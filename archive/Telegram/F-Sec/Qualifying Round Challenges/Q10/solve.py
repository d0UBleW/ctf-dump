cip = "ube~d~snuGk7wXc4#u4qbUta"
key = 7

print(''.join([ chr(ord(c) ^ key) for c in cip ][::-1]))
