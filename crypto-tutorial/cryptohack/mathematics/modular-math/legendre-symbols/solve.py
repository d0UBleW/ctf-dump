#!/usr/bin/python3

with open("output.txt") as f:
    p, _, ints = f.readlines()

p = int(p.split("=")[-1].strip())
ints = list(map(int, ints.split("=")[-1].strip().lstrip("[").rstrip("]").split(', ')))

qr = [ x for x in ints if pow(x, (p-1)//2, p) == 1 ]

for i in qr:
    exp = (p+1)//4 # https://www.rieselprime.de/ziki/Modular_square_root
    print(pow(i, exp, p))

# https://crypto.stackexchange.com/questions/20993/significance-of-3mod4-in-squares-and-square-roots-mod-n/20994#20994
