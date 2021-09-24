#!/usr/bin/python3

'''
Fermat's Little Theorem

for every prime number `n` with `a` as the coprime of n
a ^ (n-1) ≡ 1 mod n
a * a ^ (n-2) ≡ 1 mod n



3 * d ≡ 1 mod 13
Since 13 is prime and 3 is a coprime of 13, therefore d = 3 ^ (13-2) = 3 ^ 11

Now, we need to represent 3 ^ 11 in smaller number of mod 13

3 ^ 11  mod 13
((3 ^ 3) ^ 3) * 3 ^ 2  mod 13 
by multiplication property (ab) mod n ≡ [ (a mod n) * (b mod n) ] mod n
-> (3 ^ 3) ^ 3 mod 13 (since 3 ^ 3 mod 13 equals 1 we can rewrite it to 1)
   1 mod 13

-> (9) mod 13

Therefore, 3 ^ 11 mod 13 ≡ [ (1 mod 13) * (9 mod 13) ] mod 13 ≡ 9 mod 13
d = 9
'''
