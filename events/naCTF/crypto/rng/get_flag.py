#!/usr/bin/python3

from pwn import *
import random, time

random.seed(round(time.time() / 100, 5))

print(round(time.time()/100, 5))
# while True:
# 	inp = input("Input: ")
# 	print(inp)
# 	if ( inp == "r" ):
# 		print("r")
# 		print(random.randint(1, 100000000))
# 	elif ( inp == "g" ):
# 		if ( input("> ") == str(random.randint(1, 100000000)) ):
# 			print("Yes")
# 		else:
# 			print("nO")


# s = remote("challenges.ctfd.io", 30264)
# print(s.recv().decode("utf-8"))
# s.sendline("g")
# print(s.recv().decode("utf-8"))
# s.sendline(str(ans))
# print(s.recv().decode("utf-8"))
# # s.sendline(ans)
# # print(s.recv().decode("utf-8"))
# s.close()