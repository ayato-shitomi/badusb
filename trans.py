import glob
import os
import requests
import base64

def get_files_in_directory(directory_path):
    return glob.glob(os.path.join(directory_path, '*'))

def trans(data, name):
	res = requests.get(
		"http://localhost:4242/?name=" + name + "&data=" + data,
		timeout=3
	)
	return res.status_code

def make_trans(i):
	with open(i, 'br') as f:
		data = f.read()
		print(data)
		data = base64.b64encode(data)
		i = base64.b64encode(i)
		print(data, i)
		print(trans(data, i))

def main():
	directory = '.'
	files = get_files_in_directory(directory)
	print(files)
	for i in files:
		make_trans(i)

if __name__ == '__main__':
	make_trans("./arms.webp")