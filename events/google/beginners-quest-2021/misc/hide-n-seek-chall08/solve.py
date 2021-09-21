import re
import struct

with open("hideandseek.png", "rb") as f:
    image = bytearray(f.read())

with open("report.txt") as f:
    out = f.readlines()

offset = re.findall("offset: (0x[0-9A-F]*)", "".join(out))
actual = re.findall("actual length:([0-9A-F]*)", "".join(out))

for off, val in zip(offset, actual):
    off = int(off, 16)
    val = f"0x{val}"
    val = struct.pack(">I", int(val, 16))
    image[off:off+4] = val

with open("fix.png", "wb") as f:
    f.write(image)
