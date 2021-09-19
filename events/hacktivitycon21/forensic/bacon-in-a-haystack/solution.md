```shell
$ 7z x logs.7z
$ cd 2021-09-08
$ ls | xargs gzip -d

# Get any url from HTTP/HTTPS(ssl) log
$ grep -RPho '([a-z]+\.)+[a-z]+(/\w+)*' http.0* ssl.0* | sort | uniq -c | grep github
     10 api.github.com
     20 avatars.githubusercontent.com
      3 camo.githubusercontent.com
     20 collector.githubapp.com
     13 github.com
     26 github.githubassets.com
     48 sketchysite.github.io

$ curl sketchysite.github.io -Ls | grep -oP 'flag{.*}'
flag{8626fe7dcd8d412a80d0b3f0e36afd4a}
```
