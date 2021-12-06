#!/usr/bin/env python3

if __name__ == "__main__":
    alpha = "abcdefg"
    enc = "fbccdfbfdeebgcbfbcfbgcedf"

    for i in range(7):
        for j in enc:
            print(alpha[(alpha.index(j)+i)%7], end='')
        print()

