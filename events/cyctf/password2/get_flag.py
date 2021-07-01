#!/usr/bin/python3

password = "CYCTF{ju$@rcs_3l771l_@_t}bd3cfdr0y_u0t__03_0l3m"
newPass = list(password)

for i in range(0,9):
	newPass[i] = password[i]
for i in range(9,24):
	newPass[i] = password[32-i]
for i in range(24,47,2):
	newPass[i] = password[70-i]
for i in range(45,25,-2):
	newPass[i] = password[i]

password1 = "".join(newPass)

print(password1)