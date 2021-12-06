import hashlib

inp = input("inp:")
result = ""
c = ""

for e in inp:
    e  = hashlib.md5(e.encode())
    e  = e .hexdigest()
    print(e)
    c +=str(e )

print(c)

for l in c:
    l  = hashlib.sha1(l .encode())
    l  = l .hexdigest()
    result += str(l)

print(result)
print(len(result))

f = open('test.enc','w')
f.write(result)
f.close
