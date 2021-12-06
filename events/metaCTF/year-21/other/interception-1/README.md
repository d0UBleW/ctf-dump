```sh
ip addr add 192.168.0.2/24 dev eth0
ip addr del 192.168.0.3/24 dev eth0
ping -c 4 192.168.0.1
tcpdump -Ai eth0
```



Create sub interface

```sh
ifconfig eth0:1 192.168.0.2 netmask 255.255.255.0 up
arping -c 4 -U -I eth0 -s 192.168.0.2 192.168.0.1
tcpdump -Ai eth0 # tcpdump -Xi eth0
```
