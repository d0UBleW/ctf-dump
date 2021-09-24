#!/usr/bin/python3

from sshpubkeys import SSHKey
import base64

with open('pub.pub') as f:
    c = f.read()

key = SSHKey(c, strict=True)

key.parse()

sha = key.hash_sha256().split(":")[-1]
print(sha)
