from Crypto.Util.number import *

with open("out.txt", "r") as f:
    content = f.readlines()

#print(content)

ct_a, ct_b, d_a, d_b, e = [ int(i.strip().split("=")[-1]) for i in content ]

#print(ct_a)
#print(ct_b)
#print(d_a)
#print(d_b)
#print(e)

i_phi_a = d_a * e - 1
j_phi_b = d_b * e - 1
print(i_phi_a)
print()
print(j_phi_b)
print()

diff = j_phi_b - i_phi_a

print(diff)
