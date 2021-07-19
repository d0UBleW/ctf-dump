#!/usr/bin/python3

key = b'\x0b\x83\x91\xa7|\x83\xa1\xe4b\x9d\xd8\xac+\xa8\xd9:\xed\xdbq>R~\xfbZ\xe2\xe9|*\xe3di\xe2\x91\xed\xf2\xf8#\xf6*C\xdb\xc0p\xd6\xe3/B\x87'
# print(binascii.hexlify(key))
# print(len(key))
k1 = int.from_bytes(key[:16], 'big')
k2 = int.from_bytes(key[16:32], 'big')
k3 = int.from_bytes(key[32:], 'big')

# b"\x0b\x83\x11'\\\x03\xa1\xe4b\x9d\xd8(+\xa0\xd9:"

s = b'\x10$\x82\xc0!\x80\x00\x01\x19\x00\x00\xd4\x00\x0b\x02\x05'
s = int.from_bytes(s, 'big')

# print((~k2&k3) == s)


v = b'\x11\xa5\x92\xe0!\x82 A[\x80P\xd4#+B\x07'
v = int.from_bytes(v, 'big')

# print((k3&(k1|~k2)) == v)

# print((v&s) == (k3&~k2))

b = s | v

# print(b == (k3&(k1|~k2)))

c = b & s
print((v&~s) == (k1&k2&k3))
print((((((v&~s)^k1)&k2)^k2)&k3)^k3 == k3&~(k2&(~k1|k3)))

print(c == ((k3&~k2&k1)|(k3&~k2)))

# nk2_and_k3 = bin(s)[2:].zfill(128)
# r = bin(v)[2:].zfill(128)

# k1_and_k3 = []
# count = 0
# for i in range(len(r)):
# 	if (nk2_and_k3[i] == '0' and r[i] == '0'):
# 		k1_and_k3.append('0')
# 	elif(nk2_and_k3[i] == '0'):
# 		k1_and_k3.append('1')
# 	elif(nk2_and_k3[i] == r[i]):
# 		k1_and_k3.append('01')
# 		count += 1
# 	else:
# 		k1_and_k3.append('n')

# print(k1_and_k3)
# print(count)
# print(len(k1_and_k3))

# print('v&s', hex(v&s)[2:].zfill(32))
# print('v&~s', hex(v&~s)[2:].zfill(32))
# print('~v&s', hex(~v&s)[2:].zfill(32))
# print('~v&~s', hex(~v&~s)[3:].zfill(32))
# print('v|s', hex(v|s)[2:].zfill(32))
# print('v|~s', hex(v|~s)[2:].zfill(32))
# print('~v|s', hex(~v|s)[3:].zfill(32))
# print('~v|~s', hex(~v|~s)[3:].zfill(32))

print(~(v|s))