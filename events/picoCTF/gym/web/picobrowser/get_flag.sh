#!/bin/bash

curl -s -A "picobrowser" "https://jupiter.challenges.picoctf.org/problem/13759/flag" | grep --color=none -oE "picoCTF{.*}"
