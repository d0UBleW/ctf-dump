#!/usr/bin/python3

import matplotlib.pyplot as plt
import numpy as np

first = plt.imread("scrambled1.png")
second = plt.imread("scrambled2.png")

first = (first*255).astype(np.uint8)
second = (second*255).astype(np.uint8)

plt.imshow(first^second)
plt.savefig("xor_output.png")

plt.imshow(first&second)
plt.savefig("and_output.png")

plt.imshow(first|second)
plt.savefig("or_output.png")

plt.imshow(first+second)
plt.savefig("add_output.png")
