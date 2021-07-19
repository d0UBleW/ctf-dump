#!/usr/bin/python3
import binascii
from random import choice

class Cipher:
	BLOCK_SIZE = 16
	ROUNDS = 3
	def __init__(self, key):
		assert(len(key) == self.BLOCK_SIZE*self.ROUNDS)
		self.key = key

	def __block_encrypt(self, block):
		enc = int.from_bytes(block, "big")
		# print(enc)
		for i in range(self.ROUNDS):
			k = int.from_bytes(self.key[i*self.BLOCK_SIZE:(i+1)*self.BLOCK_SIZE], "big")
			# print(k)
			enc &= k
			# print("round-" + str(i) + " " + str(enc))
			print(binascii.unhexlify(hex(enc)[2:].zfill(32)))
			enc ^= k
			print(binascii.unhexlify(hex(enc)[2:].zfill(32)))
			print()
		return hex(enc)[2:].rjust(self.BLOCK_SIZE*2, "0")


	def __pad(self, msg):
		if len(msg) % self.BLOCK_SIZE != 0:
			return msg + (bytes([0]) * (self.BLOCK_SIZE - (len(msg) % self.BLOCK_SIZE)))
		else:
			return msg
	
	def encrypt(self, msg):
		m = self.__pad(msg)
		print(m)
		e = ""
		for i in range(0, len(m), self.BLOCK_SIZE):
			e += self.__block_encrypt(m[i:i+self.BLOCK_SIZE])
		return e.encode()

# key = binascii.unhexlify("".join([choice(list("abcdef0123456789")) for a in range(Cipher.BLOCK_SIZE*Cipher.ROUNDS*2)]))
# print(key)
# with open("flag", "rb") as f:
#     flag = f.read()

key = b'\x0b\x83\x91\xa7|\x83\xa1\xe4b\x9d\xd8\xac+\xa8\xd9:\xed\xdbq>R~\xfbZ\xe2\xe9|*\xe3di\xe2\x91\xed\xf2\xf8#\xf6*C\xdb\xc0p\xd6\xe3/B\x87'
print(binascii.hexlify(key))
print(len(key))
print(key[:16])
print(key[16:32])
print(key[32:])

cipher = Cipher(key)

# with open("nullbyte", 'rb') as f:
# 	payload = f.read()



while True:
	a = input("Would you like to encrypt [1], or try encrypting [2]? ")
	if a == "1":
		p = input("What would you like to encrypt: ")
		# p = binascii.hexlify(key).decode()[:32] + '00000000000000000000000000000000'
		# p = '00000000000000000000000000000000'
		# p = 'ffffffffffffffffffffffffffffffff'
		# 0000000000000000ffffffffffffffff
		# 102482c021800001190000d4000b0205
		# try:
		print(cipher.encrypt(binascii.unhexlify(p)).decode())
		# except:
			# print("Invalid input. ")
	elif a == "2":
		for i in range(10):
			p = "".join([choice(list("abcdef0123456789")) for a in range(64)])
			print("Encrypt this:", p)
			e = cipher.encrypt(binascii.unhexlify(p)).decode()
			c = input()
			if e != c:
				print("L")
				exit()
		print("W")
		print(flag.decode())            

	elif a.lower() == "quit":
		print("Bye")
		exit()
	else:
		print("Invalid input. ")
