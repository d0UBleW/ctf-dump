import subprocess
import re

charset = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

flag = ''

for i in range(19):
    for j in charset:
        cmd = "printf {} | python3 ./challenge.py".format(j*19)
        result = subprocess.check_output(cmd, shell=True)
        r1 = re.findall(r"\d", str(result))
        # print(cmd)
        print(result)
        # print(r1)
        # print(i, j)
        if r1[i] == '1':
            flag = flag + j
            print("Flag: " + str(flag))
            break