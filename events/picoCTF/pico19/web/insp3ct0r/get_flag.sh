#!/bin/bash

curl -s https://jupiter.challenges.picoctf.org/problem/41511/ https://jupiter.challenges.picoctf.org/problem/41511/mycss.css https://jupiter.challenges.picoctf.org/problem/41511/myjs.js | grep -oE "flag: .*" | awk '{print $2}' | tr -d "\n"; echo
