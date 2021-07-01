#!/usr/bin/python3

import base64

base64_string = "FgwWARMuF2UhPQotZScKFTsxCjcVJmYKY2FqCiE9FSEmCjJlMTksKA=="
base64_bytes = base64_string.encode('ascii')
passBytes = base64.b64decode(base64_bytes)
finalPass = passBytes.decode("ascii")
newPass = []

for i in range(40):
	newPass.append(chr(ord(finalPass[i])^0x55))

print("".join(newPass))