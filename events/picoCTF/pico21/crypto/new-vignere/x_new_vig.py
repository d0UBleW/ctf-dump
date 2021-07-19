import string

LOWERCASE_OFFSET = ord("a")
ALPHABET = string.ascii_lowercase[:16]

# let char = 'c' with bin = '01100011'
# encoded char will be lowercase alphabet index 4 MSB ('0110' = 6) and index 4 LSB ('0011' = 3) with a being index 0
# encoded char = fc
# due to the allowed alphabet in the flag is only limited to a through f the 4 MSB of these characters are the same
# which is '0110' and will be translated to 'g', the remaining 4 LSB is simply their index in the alphabet plus 1
# as for numeric char, the 4 MSB is '0011', which is 'd' and the same goes to the 4 LSB
def b16_encode(plain):
	enc = ""
	for c in plain:
		binary = "{0:08b}".format(ord(c))
		enc += ALPHABET[int(binary[:4], 2)]
		enc += ALPHABET[int(binary[4:], 2)]
	return enc

def shift(c, k):
	t1 = ord(c) - LOWERCASE_OFFSET
	t2 = ord(k) - LOWERCASE_OFFSET
	return ALPHABET[(t1 + t2) % len(ALPHABET)]


flag = "f71c24afc4893622361e9c47e9273a3d" # enc will be gbgcgdgegfgg
assert all([c in "abcdef0123456789" for c in flag]) # flag is in hex format

key = "apmibpckbe"
assert all([k in ALPHABET for k in key]) and len(key) < 15
# key is combination of letters starting from a up to p with the length less than 15

b16 = b16_encode(flag)
print(b16)
enc = ""
for i, c in enumerate(b16):
	# print(i,c)
	enc += shift(c, key[i % len(key)])
print(enc)

# the shifting is only capped in range 0 to the length of the key

# enc = "bkglibgkhghkijphhhejggikgjkbhefgpienefjdioghhchffhmmhhbjgclpjfkp"
# f71c24afc4893622361e9c47e9273a3d
# fpaoehfakcfpaoehfakcfpaoehfakcfp