#!/usr/bin/python3

scram = "jU5t_a_sna_3lpm12g94c_u_4_m7ra41"
passw = [""]*32

for i in range(32):
	if(i < 8):
		passw.pop(i)
		passw.insert(i, scram[i])
	elif(i < 16):
		passw.pop(i)
		passw.insert(i, scram[23-i])
	elif(i % 2 == 0):
		passw.pop(i)
		passw.insert(i, scram[46-i])
	else:
		passw.pop(i)
		passw.insert(i, scram[i])

print("picoCTF{"+"".join(passw)+"}")
