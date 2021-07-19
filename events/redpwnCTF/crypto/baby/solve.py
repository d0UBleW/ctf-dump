from Crypto.Util.number import inverse

with open('output.txt', 'r') as f:
    content = f.readlines()
    content = [ i.strip() for i in content ]

n = int(content[0].split(": ")[-1])
e = int(content[1].split(": ")[-1])
c = int(content[2].split(": ")[-1])
p = 12546190522253739887
q = 18207136478875858439

totient = (p-1) * (q-1)
d = inverse(e, totient)

m = pow(c, d, n)
print(bytearray.fromhex(hex(m)[2:]).decode())
