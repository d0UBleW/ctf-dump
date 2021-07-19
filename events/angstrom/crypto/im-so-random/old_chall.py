import time
import random
import os

class Generator():
    DIGITS = 8
    def __init__(self, seed):
        self.seed = seed
        assert(len(str(self.seed)) == self.DIGITS)

    def getNum(self):
        print(self.seed)
        self.seed = int(str(self.seed**2).rjust(self.DIGITS*2, "0")[self.DIGITS//2:self.DIGITS + self.DIGITS//2])
        return self.seed


r1 = Generator(random.randint(10000000, 99999999))
r2 = Generator(random.randint(10000000, 99999999))


query_counter = 0
while True:
    query = input("Would you like to get a random output [r], or guess the next random number [g]? ")
    if query.lower() not in ["r", "g"]:
        print("Invalid input.")
        break
    else:
        if query.lower() == "r" and query_counter < 3:
            a = r1.getNum()
            b = r2.getNum()
            print(a, b, a*b)
            # a = 34813943
            # b = 73904944
            c = Generator(a).getNum()
            d = Generator(b).getNum()
            print(c*d)
            e = Generator(c).getNum()
            f = Generator(d).getNum()
            print(e*f)
            query_counter += 1;
        elif query_counter >= 3 and query.lower() == "r":
            print("You don't get more random numbers!")
        else:
            for i in range(2):
                guess = int(input("What is your guess to the next value generated? "))
                if guess != r1.getNum() * r2.getNum():
                    print("Incorrect!")
                    exit()
            # with open("flag", "r") as f:
            #     fleg = f.read()
            print("Congrats! Here's your flag: ")
            # print(fleg)
            exit()