First we will try to discover the length of flag and the key by giving nothing in the input

Next we will give a length of 1 character input

Notice the difference.

Input with length of 1 resulting in a new block being created

This means that the previous combination of the flag and the key is a multiple of the block size

Next notice that the first 32 bytes of the output is the same.

This means that the flag is 32 bytes long and the key is 16 bytes long

The next thing that we need is the padding character which has been given by the source code, i.e., `0`

Next we will construct our input such that we can compare two blocks

let our guess character be `c`

let our dummy input be `z`

let the key be `ABCDEFGHIJKLMNOP`

let the flag be `block_0`

```
input:
c000000000000000 zABCDEFGHIJKLMNO P000000000000000
<---block_1----> <---block_2----> <---block_3---->

output:
<----enc_0-----> <----enc_1-----> <----enc_2-----> <----enc_3-----> 
```

After we brute force `c` and get `P`, we will move on to our next input
```
input:
cP00000000000000 zzABCDEFGHIJKLMN OP00000000000000
<---block_1----> <---block_2----> <---block_3---->

output:
<----enc_0-----> <----enc_1-----> <----enc_2-----> <----enc_3-----> 
```

We will repeat this process until we recover all the key
