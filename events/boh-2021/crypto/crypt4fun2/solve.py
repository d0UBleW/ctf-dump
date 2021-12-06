#!/usr/bin/env python3

if __name__ == "__main__":
    out = [885, 822, 674, 33, 835, 564, 144, 856, 407, 644, 560, 160, 48, 609,
           838, 615, 412, 154, 367, 741, 703, 77]

    an = lambda x: ((x<<5)*x-~x<<8)%971
    
    # known = b'BOH21' + chr(123).encode()
    init = 823
    flag = ''
    for i in range(len(out)):
        flag += chr(out[i] ^ init)
        init = an(init)

    print(flag)
