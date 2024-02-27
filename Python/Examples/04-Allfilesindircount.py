#fnmatch module to count all files in the directory
import fnmatch
import os

dir_path = r'D:\myVideos\Training Videos\Python for Devops\Videos'
count = len(fnmatch.filter(os.listdir(dir_path), '*.*'))
print('File Count:', count)