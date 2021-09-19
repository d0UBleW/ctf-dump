# the_library (ret2libc)

Attached: `the_library`, `libc-2.31.so`

```
$ ./the_library
Welcome to The Library.

Books:
1. Sandworm
2. Little Brother
3. Breaking and Entering: The Extraordinary Story of a Hacker Called Alien
4. Hacking: The Art of Exploitation
5. Countdown to Zero Day
6. Practical Malware Analysis

I am thinking of a book.
Which one is it?
> 1
Wrong :(
```

```
$ checksec ./the_library
[*] '/home/kali/Documents/ctf/events/hacktivitycon21/pwn/the-library/the_library'
    Arch:     amd64-64-little
    RELRO:    Full RELRO
    Stack:    No canary found
    NX:       NX enabled
    PIE:      No PIE (0x400000)
```

Use gdb to disassemble the binary and locate function which read our input

```
(gdb) disas main
--<omitted>--
   0x00000000004013af <+262>:	lea    rax,[rbp-0x220]
   0x00000000004013b6 <+269>:	mov    rdi,rax
   0x00000000004013b9 <+272>:	mov    eax,0x0
   0x00000000004013be <+277>:	call   0x401140 <gets@plt>
--<omitted>--
```

Our input is stored in `[rbp-0x220]`. Thus, to overwrite the return address, we will need to fill out the entire `0x220` buffer, plus `0x8` for the saved ebp.

Looking at the output of `checksec`, we can see that `NX` is enabled which suggest a return-oriented solution. Another thing to look for is `PIE (Position Independent Executable)` which is not enabled. This means that the relative address of the functions in PLT and GOT is always the same.

With `PIE` being disabled, we can try to leak the address of libc
