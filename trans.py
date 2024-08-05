import glob
import os

def get_files_in_directory(directory_path):
    return glob.glob(os.path.join(directory_path, '*'))

directory = '.'
files = get_files_in_directory(directory)
print(files)