#!/usr/bin/python3

g = open('pos.txt', 'w')
g.close()
enc_string = "ae27eb3a148c3cf031079921ea3315cd27eb7d02882bf724169921eb3a469920e07d0b883bf63c018869a5090e8868e331078a68ec2e468c2bf13b1d9a20ea0208882de12e398c2df60211852deb021f823dda35079b2dda25099f35ab7d218227e17d0a982bee7d098368f13503cd27f135039f68e62f1f9d3cea7c"

known = b'actf{'
known_hex = known.hex()


for i in range(0, len(enc_string)-9, 2):
	tmp = int(known_hex, 16) ^ int(enc_string[i:i+10], 16)
	tmp = hex(tmp)[2:].zfill(10)
	test = tmp[-(i%10):] + tmp[:-(i%10)]

	res = ''
	for j in range(0, len(enc_string), 2):
		if ((j+2)%10 == 0):
			end = 10
		else:
			end = (j+2)%10
		mpt = int(test[j%10:end], 16) ^ int(enc_string[j:j+2], 16)
		res += hex(mpt)[2:].zfill(2)

	if (known_hex in res):
		f = open('pos.txt', 'a')
		f.write(bytes.fromhex(res).decode()+'\n')
		f.close()
        break
