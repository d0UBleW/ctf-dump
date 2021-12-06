Unzip the ppt file

use `tree -a` and found file named `hidden`

```bash
$ cat hidden | tr -d " " | base64 -d
flag: picoCTF{D1d_u_kn0w_ppts_r_z1p5}base64: invalid input
```



flag: `picoCTF{D1d_u_kn0w_ppts_r_z1p5}`
