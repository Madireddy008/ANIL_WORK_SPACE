#scandir() to count all files in the directory
import os

count = 0
dir_path = r'D:\myVideos\Training Videos\Python for Devops\Videos'
for path in os.scandir(dir_path):
    if path.is_file():
        count += 1
print('file count:', count)