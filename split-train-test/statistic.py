import os
import sys

res = {}

img_file = sys.argv[1]
with open(img_file) as f:
	for ln in f:
		img_name = ln.rstrip('\n')
		img_label = img_name.split('_')[0]
		if img_label in res:
			res[img_label] += 1
		else:
			res[img_label] = 1


print(res)
