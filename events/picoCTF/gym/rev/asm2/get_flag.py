#!/usr/bin/python3

def asm2(p1, p2):
	var_0x4 = p2
	var_0x8 = p1
	while(var_0x8 <= 0x63f3):
		var_0x4 += 0x1
		var_0x8 += 0x80
	return hex(var_0x4)

print(asm2(0xb, 0x2e))
