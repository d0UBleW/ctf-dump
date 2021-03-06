#!/usr/bin/env python3

if __name__ == "__main__":

    '''
    Since we know input[27] value, i.e., '1', we can look for the index in
    SHUFF which results in 27. In this case, it is SHUFF[6]. Thus, we get:
    input[6] = input[27] ^ XOR[6]
    '''

    XOR = [0x56, 0x06, 0x06, 0x01, 0x09, 0x52, 0x06, 0x03, 0x51, 0x04, 0x57,
           0x07, 0x52, 0x07, 0x50, 0x06, 0x06, 0x06, 0x07, 0x54, 0x57, 0x56,
           0x02, 0x55, 0x06, 0x01, 0x52, 0x53, 0x54, 0x0f, 0x54, 0x03]
    SHUFF = [ 0x07, 0x04, 0x15, 0x12, 0x1d, 0x13, 0x1b, 0x08, 0x1f, 0x16, 0x0f,
             0x06, 0x0a, 0x19, 0x18, 0x11, 0x01, 0x03, 0x02, 0x17, 0x0d, 0x14,
             0x05, 0x00, 0x0c, 0x1c, 0x0b, 0x1a, 0x0e, 0x1e, 0x09, 0x10 ]

    known = b"15963"
    string = bytearray(b'\x00'*27) + bytearray(b"15963")
    zero = True

    while (zero):
        for i in range(len(string)):
            if string[i] != 0:
                for j in range(len(SHUFF)):
                    if i == SHUFF[j]:
                        string[j] = string[i] ^ XOR[j] 
                        break
            zero = 0 in string

    print(string)
