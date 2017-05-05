#! /usr/bin/env python3

from recommendations import critics
from sys import argv

mov = argv[1]

arr = []
for k, v in critics.items():
	for x, y in v.items():
		if x == mov:
			arr.append(y)

print("{} total ratings: {}, {}".format(mov, len(arr), arr))
print("{} average rating: {}".format(mov, sum(arr)/float(len(arr))))
