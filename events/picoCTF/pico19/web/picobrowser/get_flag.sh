#!/bin/bash

curl -s -H "User-Agent: picobrowser" https://jupiter.challenges.picoctf.org/problem/26704/flag | \
    grep -oE 'picoCTF{.*}'
