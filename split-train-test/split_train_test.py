import sys
import random


total_img_file = sys.argv[1]
res = {}   # stastic label and the numbers of the label
ratio = 0.8  # the ratio of train and test is 8:2


with open(total_img_file) as f:
	for ln in f:
		img_name = ln.rstrip('\n')
		img_label = img_name.split('_')[0]
		if img_label in res:
			res[img_label].append(img_name)
		else:
			res[img_label] = [img_name]


train_data = open('train_data.txt', 'w')
test_data = open('test_data.txt', 'w')


for k, v in res.items():
	total_nums = len(v)
	train_nums = int(total_nums * ratio)
	test_nums = total_nums - train_nums
	# random choice train_nums example from img_name list
	train_imgs = random.sample(v, train_nums)
	test_imgs = list(set(v) - set(train_imgs))
	for train_img in train_imgs:
		print(train_img, file=train_data)
	for test_img in test_imgs:
		print(test_img, file=test_data)


train_data.close()
test_data.close()
