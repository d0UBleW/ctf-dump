```
- Volatility with Win10x64_19041 profile
- Based filescan plugin, we can see that there's Users\congon4tor\Desktop\flag.ods
- Unfortunately, it has no physical offset when we tried to dump it using dumpfiles plugin
- For cleaner memory dump, we need to dump soffice.exe (LibreOffice) process
- Since ods file has the same header with zip, we can try to bulk-extract it using tools like foremost
- Unzip spreasheet, the flag is located on content.xml

$ vol.py -f  image.bin --profile=Win10x64_19041 memdump -p 5332 -D
$ foremost 5332.dmp
$ cd output/zip
$ 7z x 00113200.zip
$ cat content.xml  | grep -oP '(?<=>).(?=<)' | tr -d '\n'

flag{4b02ee4e7b62139152e8d0d4373a7c3d}
```
