# Fixing BMP

[Docs](http://www.ue.eti.pg.gda.pl/fpgalab/zadania.spartan3/zad_vga_struktura_pliku_bmp_en.html)



## Metadata

```
ExifTool Version Number         : 12.16
File Name                       : tunn3l_v1s10n
Directory                       : .
File Size                       : 2.8 MiB
File Modification Date/Time     : 2021:07:19 12:36:42+07:00
File Access Date/Time           : 2021:08:07 10:44:11+07:00
File Inode Change Date/Time     : 2021:07:19 12:36:42+07:00
File Permissions                : rw-r--r--
File Type                       : BMP
File Type Extension             : bmp
MIME Type                       : image/bmp
BMP Version                     : Unknown (53434)
Image Width                     : 1134
Image Height                    : 306
Planes                          : 1
Bit Depth                       : 24
Compression                     : None
Image Length                    : 2893400
Pixels Per Meter X              : 5669
Pixels Per Meter Y              : 5669
Num Colors                      : Use BitDepth
Num Important Colors            : All
Red Mask                        : 0x27171a23
Green Mask                      : 0x20291b1e
Blue Mask                       : 0x1e212a1d
Alpha Mask                      : 0x311a1d26
Color Space                     : Unknown (,5%()
Rendering Intent                : Unknown (826103054)
Image Size                      : 1134x306
Megapixels                      : 0.347
```



## Header (14 bytes)

```
00000000: 424d 8e26 2c00 0000 0000 bad0 0000 bad0  BM.&,...........
00000010: 0000 6e04 0000 3201 0000 0100 1800 0000  ..n...2.........
[...]
```

* Signature (2 bytes): 0x424d (BM)

* File Size (4 bytes, Little-Endian): 0x8e262c00 -> 0x002c268e (2893454/2.8MiB)

* Reserved (4 bytes, Little-Endian): 0x00000000

* Data Offset (4 bytes, Little-Endian): 0x0000d0ba



## Info Header (40 bytes)

```
                                    Starting Point (0x0E)
                                             v
00000000: 424d 8e26 2c00 0000 0000 bad0 0000 bad0  BM.&,...........
00000010: 0000 6e04 0000 3201 0000 0100 1800 0000  ..n...2.........
00000020: 0000 5826 2c00 2516 0000 2516 0000 0000  ..X&,.%...%.....
00000030: 0000 0000 0000 231a 1727 1e1b 2920 1d2a  ......#..'..) .*
00000040: 211e 261d 1a31 2825 352c 2933 2a27 382f  !.&..1(%5,)3*'8/
[...]
```

Starting Offset = 0x0E



* Size (4 bytes, Little-Endian): Size of Info Header (40 bytes) 0x0000d0ba (not 40 bytes), change into 0x00000028 (in proper order 2800 0000)</br>
Viewing the file still does not show the flag. The picture seems to have a false dimension (changing the width destroys the image, changing the height shows the flag)

```
00000000: 424d 8e26 2c00 0000 0000 bad0 0000 2800  BM.&,.........(.
00000010: 0000 6e04 0000 3201 0000 0100 1800 0000  ..n...2.........
00000020: 0000 5826 2c00 2516 0000 2516 0000 0000  ..X&,.%...%.....
00000030: 0000 0000 0000 231a 1727 1e1b 2920 1d2a  ......#..'..) .*
00000040: 211e 261d 1a31 2825 352c 2933 2a27 382f  !.&..1(%5,)3*'8/
[...]
```

![preview](/home/kali/Documents/ctf/events/picoCTF/pico21/forensic/tunn3l-v1s10n/first_output.bmp "Fixed Info Header Size")



* Width (4 bytes, Little-Endian): 0x0000046e (1134)

* Height (4 bytes, Little-Endian): 0x00000132 (306) change into 0x00000332 (818)

```
00000000: 424d 8e26 2c00 0000 0000 bad0 0000 2800  BM.&,.........(.
00000010: 0000 6e04 0000 3203 0000 0100 1800 0000  ..n...2.........
00000020: 0000 5826 2c00 2516 0000 2516 0000 0000  ..X&,.%...%.....
00000030: 0000 0000 0000 231a 1727 1e1b 2920 1d2a  ......#..'..) .*
00000040: 211e 261d 1a31 2825 352c 2933 2a27 382f  !.&..1(%5,)3*'8/
[...]
```

![preview](/home/kali/Documents/ctf/events/picoCTF/pico21/forensic/tunn3l-v1s10n/output.bmp "Fixed Info Header Size and Height Dimension")



* Planes (2 bytes, Little-Endian): 0x0001

* etc.



## Flag: `picoCTF{qu1t3_a_v13w_2020}`
