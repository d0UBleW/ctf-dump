#!/usr/bin/env python3

import zlib

wbits = -zlib.MAX_WBITS

# do = zlib.decompressobj(16+wbits)
fh = open('e0', 'rb')
cdata = fh.read()
fh.close()
# data = do.decompress(cdata)

zlib.decompress(cdata, zlib.MAX_WBITS | 32)
