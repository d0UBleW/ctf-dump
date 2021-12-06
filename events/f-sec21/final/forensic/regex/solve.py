#!/usr/bin/env python3

if __name__ == "__main__":
    name = b"IEWIN7"
    arr = [ 47,54,16,33,126,2,61,12,57,61,38,4,27,32,48,120,61,0,59,28,52,48,44,82,59 ];
    # known = b"fs"
    # for i in range(len(known)):
    #     print(chr(known[i] ^ arr[i]))
    # trail = b"cyber"
    # tr = arr[-5:]
    # for i in range(5):
    #     print(chr(tr[i] ^ trail[i]), end='')
    for i in range(len(arr)):
        print(chr(name[i%len(name)] ^ arr[i]), end='')

