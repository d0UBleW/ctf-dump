import string

def encrypt(text, key):
 
    w = [['\n' for i in range(len(text))]
                  for j in range(key)]
    print(w)
     
    dir_down = False
    r, c = 0, 0
     
    for i in range(len(text)):
         
        if (r == 0) or (r == key - 1):
            dir_down = not dir_down
         
        w[r][c] = text[i]
        c += 1
         
       
        if dir_down:
            r += 1
        else:
            r -= 1

    print(w)
   
    result = []
    for i in range(key):
        for j in range(len(text)):
            if w[i][j] != '\n':
                result.append(w[i][j])
    return("" . join(result))
    
def replace(text):
    text = [x.replace(' ', '_') for x in text]
    return ("" . join(text))
   
# t = open(**keys**).read()
t = open('merged').read()
t = "ABCDEFGH"
k = 3
res = replace(encrypt(t, k))
print(res)
