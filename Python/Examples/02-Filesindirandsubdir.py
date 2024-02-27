#Count all files in the directory and its subdirectories
import os

count = 0
for root_dir, cur_dir, files in os.walk(r'D:\myVideos\Training Videos\Python for Devops'):
    count += len(files)
print('file count:', count)