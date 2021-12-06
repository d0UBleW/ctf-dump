#!/usr/bin/python2.7

cd = '\x6f'
gh = '\x70'

print '''

 .----------------.  .----------------.  .----------------.  .----------------. 
| .--------------. || .--------------. || .--------------. || .--------------. |
| |  ___  ____   | || |   ______     | || | ____    ____ | || |    ______    | |
| | |_  ||_  _|  | || |  |_   __ \   | || ||_   \  /   _|| || |  .' ___  |   | |
| |   | |_/ /    | || |    | |__) |  | || |  |   \/   |  | || | / .'   \_|   | |
| |   |  __'.    | || |    |  ___/   | || |  | |\  /| |  | || | | |    ____  | |
| |  _| |  \ \_  | || |   _| |_      | || | _| |_\/_| |_ | || | \ `.___]  _| | |
| | |____||____| | || |  |_____|     | || ||_____||_____|| || |  `._____.'   | |
| |              | || |              | || |              | || |              | |
| '--------------' || '--------------' || '--------------' || '--------------' |
 '----------------'  '----------------'  '----------------'  '----------------' 
 
'''

import random 

ef = '\x6d'
ab = '\x63'
password = [0x68, 0x61, 0x68, 0x61, 0x68, 0x61, 0x68, 0x61, 0x68, 0x61]
iris = [78, 85, 72, 66, 126, 99, 53, 53, 97, 120]


ij = '\x65'
op = '\x74'
thumbprint = random.randint(0, 0x3e8)

thumb = thumbprint * 2

chars = []

thumb = thumb + 10

qr = '\x6f'
yz = '\x6b'
mn = '\x69'

thumb = thumb / 2

code = [0x6b, 0x65, 0x65, 0x70, 0x20, 0x74, 0x72, 0x79, 0x69, 0x6e, 0x67]
thumb = thumb - thumbprint

print 'Cybersecurity Challenge 2019'
print ''
print ''

for eye in iris:
	finger = thumb ^ eye
	chars.append(finger)
    

kl = '\x74'
wx = '\x61'	
st = '\x72'

varlent = ab + cd + ef + gh + ij + kl + mn + op + qr + st
print(varlent)


print 'Stop, Show Us Your Credentials'
print ''
user_input = raw_input('Enter your username:\n')
if user_input == varlent:
    pass

else:
    print 'Wrong username try harder'
    exit()

print''
pass_input = raw_input('Enter your Flag:\n')

res = ""
for char in chars:
    res += str(chr(char))

if pass_input == res:
	print ''
	print 'Good Job! You found the flag!'
	print ''
        
else:
	print 'Wrong flag try harder'
        exit(0)
    	
