#! /usr/bin/env python3

from recommendations import critics
mov = 'Lady in the Water'

arr = []
for k, v in critics.items():
	for x, y in v.items():
		if x == mov:
			print(x, y)
			arr.append(y)

print("{} total ratings: {}, {}".format(mov, len(arr), arr))
print("{} average rating: {}".format(mov, sum(arr)/float(len(arr))))