The author made a mistake in XOR-ing the flag

`flag[i] ^ key[i % 1]` which should be `flag[i] ^ key[ i % len(key) ]`

The results is a `JSFUCK` esolang
