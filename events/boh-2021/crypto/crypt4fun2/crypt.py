def magic(x):
	magiclist = []
	for i in range(100):
		x = ((x<<5)*x-~x<<8)%971
		magiclist.append(x)
	return magiclist
	
	
flag = open('f').read()
output = []
r = randint(0,1000)
g = magic(r)

for i in range(len(flag)):
	output.append(ord(flag[i]) ^ g[i])
	
print(output)
