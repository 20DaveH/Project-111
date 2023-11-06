import os 
import shutil

from_dir = "C:/Users/Preetesh/Downloads"
to_dir = "C:/Users/Preetesh/Desktop/VSC-Python"

list_of_files = os.listdir(from_dir)
for file_name in (list_of_files):
    name,extension = os.path.splitext(file_name)

print(list_of_files)



