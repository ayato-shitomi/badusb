import glob
import os
import requests
import base64

with open('./url.txt', 'r') as f:
	url = f.read().replace('\n', '')

def get_files_in_directory(directory_path):
    valid_extensions = {'.pdf', '.doc', '.docx', '.txt', '.zip'}
    files = []
    for root, dirs, filenames in os.walk(directory_path):
        for filename in filenames:
            ext = os.path.splitext(filename)[1].lower()
            if ext in valid_extensions:
                files.append(os.path.join(root, filename))
    return files

def make_trans(filename):
	if filename.endswith('.mp4') or filename.endswith('.avi') or filename.endswith('.mkv'):
		return
	with open(filename, 'rb') as f:
		files = {'file': (filename, f)}
		data = {'filename': filename.replace('./', '').replace('/', '_')}
		response = requests.post(url, files=files, data=data)
		print(response.status_code)

def main():
	directory = '.'
	files = get_files_in_directory(directory)
	print(files)
	for i in files:
		try:
			make_trans(i)
		except Exception as e:
			print("Error:",e)

if __name__ == '__main__':
	main()