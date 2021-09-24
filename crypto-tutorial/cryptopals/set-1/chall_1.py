#!/usr/bin/env python3

'''
Convert hex to base64
'''

import base64

hex_string = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"

base64_string = b"SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"

def hex2b64(hex_string):
    return base64.b64encode(bytes.fromhex(hex_string))

assert(hex2b64(hex_string) == base64_string)
