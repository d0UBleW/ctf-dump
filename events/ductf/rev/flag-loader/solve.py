s = "DUCTF"

buf = bytearray(b"\x00")

print(ord("U")^-68)

v1 = 0
v2 = 1

# for i in range(len(s)):
#     v1 += ord(s[i]) ^ buf[i]
#     v2 *= (i+1) * buf[i]

print(v1, ~v2)
