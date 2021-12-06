#!/bin/bash

echo -n pico; \
    curl -s https://jupiter.challenges.picoctf.org/problem/37821/ | \
    grep -E "if.*split" | \
    awk -F", " '{print $2}' | \
    tr -d ")" | \
    cut -d " " -f1,3 | \
    sort -k1 | \
    awk '{print $2}' | \
    head -7 | \
    tr -d "'" | \
    tr -d "\n"
