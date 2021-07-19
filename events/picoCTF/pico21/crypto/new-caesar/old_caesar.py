import string

LOWERCASE_OFFSET = ord("a")
ALPHABET = string.ascii_lowercase[:16]

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

printable_char = "!"+'"'+r"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~"

# key = "a"
# assert all([k in ALPHABET for k in key])
# assert len(key) == 1

b16 = b16_encode(printable_char)
# print(b16)

# enc = input()
enc = "mlnklfnknljflfmhjimkmhjhmljhjomhmmjkjpmmjmjkjpjojgjmjpjojojnjojmmkmlmijimhjmmj"
enc_pad = ''

for i in range(0,len(enc),2):
	enc_pad += enc[i]



used_pad = sorted(list(set(list(enc_pad))))

print("Used pad:", used_pad)

cne = ''

dict_l = {}
dict_m = {}
dict_n = {}
dict_j = {}
dcit = {}

for j in ALPHABET:
	for i, c in enumerate(b16):
		if i%2==0:
			cne += shift(c, j)
	dcit[j] = sorted(list(set(list(cne))))
	cne = ''

# print(dcit)

condition = False

for i in dcit:
	for j in used_pad:
		if j in dcit[i]:
			condition = True
		else:
			condition = False
			break
	if condition == True:
		key = i
		break
else:
	print("No matching key.")
	exit()

print("Key:", key)

book = {}
for i in range(len(dcit[key])):
	book[dcit[key][i]] = {}


for i in range(0,len(b16),2):
	book[shift(b16[i], key)][shift(b16[i+1], key)] = printable_char[i//2]

	# if shift(b16[i], key) == 'l':
	# 	dict_l[shift(b16[i+1], key)] = printable_char[i//2]
	# elif shift(b16[i], key) == 'm':
	# 	dict_m[shift(b16[i+1], key)] = printable_char[i//2]
	# elif shift(b16[i], key) == 'n':
	# 	dict_n[shift(b16[i+1], key)] = printable_char[i//2]
	# elif shift(b16[i], key) == 'j':
	# 	dict_j[shift(b16[i+1], key)] = printable_char[i//2]

# print(book)

# print(dict_l)
# print(dict_m)
# print(dict_n)
# print(dict_j)

print("picoCTF{",end='')
for i in range(0,len(enc),2):
	print(book[enc[i]][enc[i+1]],end='')

	# if enc[i] == 'l':
	# 	print(dict_l[enc[i+1]],end='')
	# elif enc[i] == 'm':
	# 	print(dict_m[enc[i+1]],end='')
	# elif enc[i] == 'n':
	# 	print(dict_n[enc[i+1]],end='')
	# elif enc[i] == 'j':
	# 	print(dict_j[enc[i+1]],end='')

print("}")