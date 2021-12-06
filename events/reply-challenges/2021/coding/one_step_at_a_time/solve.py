#!/usr/bin/env python3

import re

if __name__ == "__main__":
    with open("maze.txt") as f:
        maze = f.readlines()

    with open("map.txt") as f:
        maps = f.read()
        

    decrypted = ''

    maps = maps.split("\n\n")
    for i in maps:
        i = i.split()
        for j in maze:
            if (i[0] in j):
                line = maze.index(j)
                line += int(i[1])
                offset = j.find(i[0])
                offset += int(i[2])
                decrypted += maze[line][offset]

    pattern = re.compile("\{FLG:.+?\}")
    print(pattern.findall(decrypted))
    print()

    for i in maps:
        i = i.split()
        for j in maze:
            if (i[4] in j):
                line = maze.index(j)
                line -= int(i[3])
                offset = j.find(i[4])
                offset += int(i[2])
                print(maze[line][offset],end='')
