[write-up](https://ctftime.org/event/1444/tasks/)

```shell
find . -type f | \
    while read line; do \
        p=$line; \
        n=$(echo $p | cut -d "?" -f1);\
        mv $p $n; \
    done
```
