Gathering information for each character a-z0-9{}

input `a`: `000102030405060708090a0b0c0d0e0f`
input `b`: `101112131415161718191a1b1c1d1e1f`
input `c`: `202122232425262728292a2b2c2d2e2f`

then input `abacabacabacabab`: `001102230415062708190a2b0c1d0e1f`

basically if the `a` is in index `n` of the input, it will return the value of `a[n]`
example `cba`, it will return `c[0] + b[1] + a[2]` where `c[0] = 20; b[1] = 11; a[2] = 02`
