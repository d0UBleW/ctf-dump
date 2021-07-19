import time
import random
import os

class Generator():
    DIGITS = 8
    def __init__(self, seed):
        self.seed = seed
        assert(len(str(self.seed)) == self.DIGITS)

    def getNum(self):
        self.seed = int(str(self.seed**2).rjust(self.DIGITS*2, "0")[self.DIGITS//2:self.DIGITS + self.DIGITS//2])
        return self.seed


r1 = Generator(32912891).getNum()
r2 = Generator(69428770).getNum()
print(r1)
print(r2)
print(r1*r2)
c = Generator(r1).getNum()
d = Generator(r2).getNum()
print(c*d)
# a = Generator(c)
# b = Generator(d)
# print(a*b)
