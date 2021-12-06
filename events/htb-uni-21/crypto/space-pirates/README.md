Shamir's Secret Sharing Scheme uses a polynomial to compute the shares

the function `calc_y` is the calculation of the polynomials

the defined value of `k` is 10 and the polynomials only take the first 10 computed coefficients

the first coefficient is the SECRET

the coefficients is calculated from the last computed coefficients
since we know the second coefficient, we would be able to compute all the rest 8 coefficients using `calc_coeff` function

```
f(x) = SECRET(c0) * x**0 + c1 * x**1 + c2 * x**2 + ... + c9 * x**9
```

since we know the value of (x0, y0) or in other words (x0, f(x0)) and all the coefficients
we are able to compute c0 (SECRET) by computing
```
known = c1 * x**1 + c2 * x**2 + c3 * x**3 + ... + c9 * x**9
```

we get the value `known` but it is bigger than the y0 since y0 is the original y0 % prime
therefore, we can find out the original y0 by keep adding the prime into it until it is larger than `known`

we can do that by taking a simple solution
```
how many time should we add 3 into 2 such that it is bigger than 27?
27 - 2 = 25
25 / 3 = 8.333... (get the quotient)
2 + 3 * 8 = 26 (still < 27)
2 + 3 * (8+1) = 29
```

with the same concept we can calculate the original y0 by
```
diff = known - y0
times = diff // prime
ori = y0 + times*prime
if ori < known, add the prime one more time
```

after we get the original y0, we can simply subtract y0 with `known` to get the SECRET since
```
original y0 = SECRET + known
```
