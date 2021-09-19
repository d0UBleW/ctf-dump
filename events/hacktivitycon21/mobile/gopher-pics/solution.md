```
strings gopher_pics.apk  | grep -i $(python -c 'print("flag{".encode("hex"))')
```
