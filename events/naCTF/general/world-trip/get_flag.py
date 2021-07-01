#!/usr/bin/python3

from geopy.geocoders import Nominatim
from functools import partial

geolocator = Nominatim(user_agent="a")
reverse = partial(geolocator.reverse, language="en")


with open('enc.txt') as f:
	s = f.read().replace(")(", ")_(").split("_")


lst = []

print("nactf{", end='')

for i in range(len(s)):
	coordinates = str(s[i].replace("(", '').replace(")", ''))
	cnt = reverse(coordinates)
	countries = cnt[0].split(", ")[-1]
	print(countries[0], end="")

print("}")


