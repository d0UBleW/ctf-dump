#!/usr/bin/env python3

import chall_3
import binascii

with open('4.txt') as f:
    # content = [bytes.fromhex(i.strip()) for i in f.readlines()]
    content = [binascii.unhexlify(i.strip()) for i in f.readlines()]

output = list(map(chall_3.bruteXOR, content))

best = None

result = None

for i in output:
    for k, v in i.items():
        if k == 'ratio':
            if best == None or best < v:
                best = v
                result = i

print(result)

# output = [ i for lst in output for i in lst ]

# output.sort(key=lambda x: x[2])

# for i in output:
#     print(i)


# mx = []

# for i in output:
#     m = max([ metric for metric, out in i ])
#     mx.append(m)
            
# # m = [ metric for i in output for metric, out in i ]

# new = []

# for m, s in [ (met, s) for i in output for met, s in i if met in mx ]:
#     new.append((m, s.encode()))

# new.sort(key=lambda x:x[0])

# for i in new:
#     print(i)
