from math import sqrt

with open('output.txt', 'r', encoding='utf-8') as f:
    content = f.read().strip()

val = []

for i in content:
    val.append(ord(i))

def solve(a, b, c, y):
    x1 = (-b + sqrt(b**2 - 4*a*(c-y)))/(2*a)
    x2 = (-b - sqrt(b**2 - 4*a*(c-y)))/(2*a)
    return (x1, x2)

a = 13
b = 3
c = 7

out = []

for i in val:
    x1, x2 = solve(a, b, c, i)
    out.append(x1 if x1 > x2 else x2)

print(''.join(chr(int(i)) for i in out))
