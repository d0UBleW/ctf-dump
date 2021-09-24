#!/usr/bin/env python3

'''
Single-byte XOR cipher
'''

import string
import chall_2

def bruteXOR(byte_string):
    '''
    byte_string: string in bytes, e.g., b'abcd'

    returns a dictionary which contains key, plaintext, and ratio of the most probable english text
    '''
    out = []

    best = None

    for i in range(pow(2, 8)):
        i = i.to_bytes(1, byteorder="big")
        key_stream = i * len(byte_string)
        candidate_pt = chall_2.fixed_XOR(byte_string, key_stream)
        ratio = char_ratio(candidate_pt)

        if best == None or best < ratio:
            best = ratio
            pt = candidate_pt
            key = i

    result = {
            "key": key,
            "plaintext": pt,
            "ratio": best,
            }

    return result


    # alpha = string.ascii_lowercase + string.ascii_uppercase + ' '

    # for i in range(256):
    #     metric = 0
    #     decoded = ''
    #     for b in byte_string:
    #         c = chr(b ^ i)
    #         decoded += c
    #         if (c in alpha):
    #             metric += 1
    #     out.append((metric/len(decoded), decoded))

    # out.sort(key=lambda x: x[0])

    # return out

def char_ratio(byte_string):
    '''
    byte_string: byte string

    returns the ratio of total number of characters in english lowercase, uppercase, and space with the length of byte string
    '''

    alpha = string.ascii_lowercase + string.ascii_uppercase + ' '
    normal_ascii = [ ord(c) for c in alpha ]
    ascii_counter = sum([ char in normal_ascii for char in byte_string ])
    ratio = ascii_counter / len(byte_string)

    return ratio


def is_probably_text(byte_string):
    '''
    byte_string: byte string

    returns True if the ratio of the byte string is considered as a normal english plaintext
    '''

    ratio = char_ratio(byte_string)
    return True if ratio >= 0.7 else False


if __name__ == "__main__":
    hex_enc = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
    byt_str = bytes.fromhex(hex_enc)
    out = bruteXOR(byt_str)
    print(out)
    # for i in out:
    #     print(i)

    # print(is_probably_text(b"How are you?"))
