#!/usr/bin/env python3

'''
Fixed XOR
'''

def fixed_XOR(byte_string_1, byte_string_2):
    '''
    byte_string_1: python byte string, e.g., b_str = b'abcd'
    byte_string_2: python byte string, e.g., b_str = b'abcd'

    both byte_string_1 and byte_string_2 should have the same length

    returns the output of byte_string_1 XOR-ed with byte_string_2 in byte form
    '''
    
    assert len(byte_string_1) == len(byte_string_2), "Strings are not the same length"

    return bytes([ a^b for (a,b) in zip(byte_string_1, byte_string_2) ])

    # int_str1 = int.from_bytes(byte_string_1, "big")
    # int_str2 = int.from_bytes(byte_string_2, "big")

    # out = int_str1 ^ int_str2

    # out = "{:x}".format(out)
    # out = "0" * (len(out) % 2) + out

    # return out


if __name__ == "__main__":
    str1 = bytes.fromhex("1c0111001f010100061a024b53535009181c")
    str2 = bytes.fromhex("686974207468652062756c6c277320657965")
    result = bytes.fromhex("746865206b696420646f6e277420706c6179")
    out = fixed_XOR(str1, str2)

    assert(out == result)
