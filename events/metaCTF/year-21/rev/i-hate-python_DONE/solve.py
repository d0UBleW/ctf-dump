import random
import string

def do_thing(a, b):
    return ((a << 1) & b) ^ ((a << 1) | b)

random.seed(997)

x = 'MetaCTF{this_is_fak_flag}'

k = [random.randint(0, 256) for _ in range(len(x))]

b = list(range(len(x)))
random.shuffle(b)
a = { b: do_thing(ord(c), d) for (b, c), d in zip(enumerate(x), k)}

c = [a[i] for i in b[::-1]]

kn = [47, 123, 113, 232, 118, 98, 183, 183, 77, 64, 218, 223, 232, 82, 16, 72, 68, 191, 54, 116, 38, 151, 174, 234, 127]

mapping = {k: v for k, v in zip(b[::-1], list(range(len(x))))}
mapping = {k: v for k, v in sorted(mapping.items(), key=lambda x: x[0])}

flag = 'MetaCTF{'
for i in range(8, 24):
    for byt in string.printable:
        if do_thing(ord(byt), k[i]) == kn[mapping[i]]:
            flag += byt

flag += '}'
print(flag)
