#!/usr/bin/env python3

def circuit(inp):
    out = [None]*9
    out[1] = inp[5]
    out[2] = inp[6] ^ adder(inp[4], inp[3], inp[2])[1]
    out[0] = inp[8] ^ out[2]
    out[3] = adder(inp[4], inp[3], inp[2])[0]
    out[4] = inp[0] | invert(inp[5]) | out[3]
    out[5] = inp[0]
    out[6] = inp[5] ^ inp[0]
    out[7] = inp[7] & inp[1]
    out[8] = inp[8] ^ out[6]
    return out


def adder(a, b, cin):
    s = (a ^ b) ^ cin
    cout = ((a ^ b) & cin) | (a & b)
    return (s, cout)

def invert(bit):
    return 1 if bit == 0 else 0

if __name__ == "__main__":
    lookup = "a_cdefaijkltmnopwzstueabez01200067890ABCDEFGHIJKnooodtdvw000eta?T!VW00Y!ETA?*-+/{}[]=&%£\"!()abcdefghijklmnopqrsABCDEFGHIJKLNMuuuvwxipsilonnnnnnz%%/9876543210|!\"£$ohdear!%&/(((()*;:_AAAABSIDEOWabcdefghijklmnopqrstuvwxyz012345678?8?8?8?9!!!!!EGIN.CERTIFICATEa_cdefaijkltmnopwzstueabez01200067890ABCDEFGHIJKnooodtdvw000eta?T!VW00Y!ETA?*-+/{}[]=&%£\"!()abcdefghijklmnopqrsABCDEFGHIJKLNMuuuvwxipsilonnnnnnz%%/9876543210|!\"£$ohdear!%&/(((()*;:_AAAABSIDEOWabcdefghijklmnopqrstuvwxyz012345678?8?8?8?9!!!!!EGIN.CERTIFICATE"
    inp = [
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
    ]

    for i in range(10):
        inp = circuit(inp)
        addr = int(''.join(map(str, inp))[::-1], 2)
        print(lookup[addr], end='')
