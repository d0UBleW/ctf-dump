#!/usr/bin/env python3


if __name__ == "__main__":
    with open('boh21_blank.txt', 'rb') as f:
        content = f.read()


    new1 = []
    new2 = []

    for i in content:
        if i == 32:
            new1.append("0")
            new2.append("1")
        else:
            new1.append("1")
            new2.append("0")

    str1 = ''.join(new1)
    str2 = ''.join(new2)

    flag1 = ''
    flag2 = ''

    for i in range(0, len(str1), 8):
        flag1 += chr(int("0b"+str1[i:i+8], 2))

    for i in range(0, len(str2), 8):
        flag2 += chr(int("0b"+str2[i:i+8], 2))

    print(flag1)
    print(flag2)

    print(''.join(chr(int(i)) for i in flag2.split(' ')))
