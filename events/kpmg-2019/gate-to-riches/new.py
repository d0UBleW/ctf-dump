#!/usr/bin/env python3

import random

if __name__ == "__main__":
    x = random.randint(0, 0x3e8)
    print(x)
    y = x*2
    y += 10
    y = y//2
    y = y - x
    print(y)
    iris = [78, 85, 72, 66, 126, 99, 53, 53, 97, 120]
    chars = [chr(i ^ y) for i in iris]
    print(''.join(chars))
    thumb = 5
    iris = [78, 85, 72, 66, 126, 99, 53, 53, 97, 120]
    flag = ''.join(chr(i ^ thumb) for i in iris)
    print(flag)

