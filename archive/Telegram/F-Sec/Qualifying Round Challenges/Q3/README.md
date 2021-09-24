Convert the `.MSG` file

```bash
msgconvert Q3
```

Output: `Q3.eml`

Found encrypted flag: `AohEiF(I<gASu!rA7]7r@V'Q`

Keyword: `base`

Run [basecrack.py](https://github.com/mufeedvh/basecrack)

```

██████╗  █████╗ ███████╗███████╗ ██████╗██████╗  █████╗  ██████╗██╗  ██╗
██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝██╔══██╗██╔══██╗██╔════╝██║ ██╔╝
██████╔╝███████║███████╗█████╗  ██║     ██████╔╝███████║██║     █████╔╝ 
██╔══██╗██╔══██║╚════██║██╔══╝  ██║     ██╔══██╗██╔══██║██║     ██╔═██╗ 
██████╔╝██║  ██║███████║███████╗╚██████╗██║  ██║██║  ██║╚██████╗██║  ██╗
╚═════╝ ╚═╝  ╚═╝╚══════╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝ v3.0
    
		python basecrack.py -h [FOR HELP]

[>] Enter Encoded Base: AohEiF(I<gASu!rA7]7r@V'Q             


[>] Decoding as Ascii85: fsbase85encodecyber

[-] The Encoding Scheme Is Ascii85

```

flag: `fsbase85encodercyber`
