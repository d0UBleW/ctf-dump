#!/usr/bin/env python3

from factordb.factordb import FactorDB
from Crypto.Util.number import inverse, long_to_bytes, GCD
import itertools

if __name__ == "__main__":
    with open("public_keys.txt") as f:
        content = [i.strip() for i in f.readlines() if len(i) > 1]

    pair = [(content[i], content[i+1]) for i in range(0, len(content), 2)]

    # for n, e in pair:
    #     n = int(n.split()[-1], 16)
    #     e = int(e.split()[-1], 16)
    #     print(n)
    #     print(e)
    #     print()
    #     f = FactorDB(n)
    #     f.connect()
    #     factor = f.get_factor_list()
    #     p, q = factor
    #     phi = (p-1)*(q-1)
    #     d = inverse(e, phi)
    #     print(long_to_bytes(d))
    #     break

    common_moduli = list(itertools.combinations(pair, 2))

    for a, b in common_moduli:
        a_n = int(a[0].split()[-1], 16)
        b_n = int(b[0].split()[-1], 16)
        common_divisor = GCD(a_n, b_n)
        if common_divisor != 1:
            a_p = common_divisor
            a_q = a_n // a_p
            a_e = int(a[1].split()[-1], 16)
            a_phi = (a_p - 1) * (a_q - 1)
            a_d = inverse(a_e, a_phi)
            print(long_to_bytes(a_d))

            b_p = common_divisor
            b_q = b_n // b_p
            b_e = int(b[1].split()[-1], 16)
            b_phi = (b_p - 1) * (b_q - 1)
            b_d = inverse(b_e, b_phi)
            print(long_to_bytes(b_d))
