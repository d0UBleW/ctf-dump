#!/usr/bin/env python3

target = [
    52037,
    52077,
    52077,
    52066,
    52046,
    52063,
    52081,
    52081,
    52085,
    52077,
    52080,
    52066,
]

for i in target:
    print(chr(i - 0xcafe), end='')
