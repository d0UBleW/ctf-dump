#!/usr/bin/env python3

if __name__ == "__main__":
    for x in range(1, 6):
        filename = "key" + str(x) + ".enc"
        f = open(filename)
        enc = f.read().strip()
        f.close()
        key = 3
        w = [ ["\xff" for i in range(len(enc))] for j in range(key) ]
        idx = 0

        dir_down = False
        r, c = 0, 0
         
        for i in range(len(enc)):
             
            if (r == 0) or (r == key - 1):
                dir_down = not dir_down
             
            w[r][c] = c
            c += 1
             
           
            if dir_down:
                r += 1
            else:
                r -= 1

        position = []
        for i in range(len(w)):
            for j in range(len(w[i])):
                if (w[i][j] != '\xff'):
                    position.append(w[i][j])

        # print(position)
        dec = ["\xff" for i in range(len(enc))]

        for i in range(len(position)):
            dec[position[i]] = enc[i]

        print(''.join(dec))
        
        out = 'dec_key' + str(x)
        with open(out, 'w') as f:
            f.write(''.join(dec)+"\n")

