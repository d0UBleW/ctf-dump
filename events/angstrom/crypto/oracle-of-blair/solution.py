from pwn import *

# nc crypto.2021.chall.actf.co 21112

def ctx(i):
    return ''.join([hex(ord(j))[2:] for j in i])

p = remote("crypto.2021.chall.actf.co", 21112)
z16 = '00' * 16
padding = '00' * 31
letters = []

alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890{}_+-'
for i in range(40):
    p.recvuntil(": ")
    p.sendline(z16 + padding + ctx("{}"))
    print(z16 + padding + ctx('{}'))
    ans = p.recvuntil("\n")[64:96]
    print(ans)
    for c in alphabet:
        p.recvuntil(": ")
        #print(z16 + padding + ctx(c))
        # print(z16 + padding + ''.join([ctx(a) for a in letters]) + ctx(c))
        p.sendline(z16 + padding + ''.join([ctx(a) for a in letters]) + ctx(c))
        cr = p.recvuntil('\n')[64:96]
        #print(cr)
        if cr == ans:
            letters.append(c)
            print(padding + ''.join([ctx(a) for a in letters]))
            print(''.join(letters))
            padding = padding[2:]
            if letters[-1] == '}':
                p.interactive()
            break
    #print("failed lel")
    #break
p.interactive()
