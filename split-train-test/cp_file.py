import sys
import shutil


img_files = sys.argv[1]

with open(img_files) as f:
	for ln in f:
		img_file = ln.rstrip('\n')
		print(img_file)
		src_path = 'total-data/' + img_file
		dst_path = 'test-data/' + img_file
		shutil.copy(src_path, dst_path)
