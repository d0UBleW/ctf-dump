#!/usr/bin/env python3

import string


if __name__ == "__main__":
    
    alphabet = string.ascii_letters

    with open("puzzle.txt") as f:
        content = f.readlines()

    puzzle = [ i.strip() for i in content[7:] ]
    set_ = ' '.join(puzzle).split()
    freq = {}
    for i in set_:
        if i not in freq:
            freq[i] = 1
        else:
            freq[i] += 1

    edge = []
    for k, v in freq.items():
        if v == 1 and k not in alphabet:
            edge.append(k)

    puzzle = [ i.split() for i in puzzle ]



    for i in puzzle:
        if (i[0] in edge and i[2] in edge):
            up_left = i
        if (i[0] in edge and i[3] in edge):
            up_right = i
        if (i[1] in edge and i[2] in edge):
            down_left = i
        if (i[1] in edge and i[3] in edge):
            down_right = i

    print(up_left)
    print(up_right)
    print(down_left)
    print(down_right)

    arrange = []
    temp = []
    temp.append(up_left)
    arrange.append(temp)
    print(arrange[0])

    j = 0
    while j < 199:
        for pieces in puzzle:
            if pieces[0] == arrange[j][0][1]:
                arrange.append([pieces])
                break
        j += 1

    for i in range(200):
        j = 0
        while j < 199:
            for pieces in puzzle:
                if pieces[2] == arrange[i][j][3]:
                    arrange[i].append(pieces)
                    break
            j += 1
        print(i)

    passwd = []

    with open("array", 'w') as f:
        f.write(repr(arrange))

    for i in arrange:
        for j in i:
            if len(j) == 5:
                passwd.append([arrange.index(i), i.index(j), j])
                print(j[-1], end='')
        print()

    print(passwd)
    print(len(passwd))

