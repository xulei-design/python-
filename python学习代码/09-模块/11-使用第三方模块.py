# pip是下载/删除 第三方软件包，python中没有所需功能的模块，
# pip install flask  下载第三方模块 flask

# python在查找模块的时候，在那些路径下查找
from flask import Flask
import sys
# ['D:\\python学习代码\\09-内置模块',
#  'D:\\python学习代码\\09-内置模块',
#  'C:\\Users\\战神\\AppData\\Local\\Programs\\Python\\Python37\\python37.zip',
#  'C:\\Users\\战神\\AppData\\Local\\Programs\\Python\\Python37\\DLLs',
#  'C:\\Users\\战神\\AppData\\Local\\Programs\\Python\\Python37\\lib',
#  'C:\\Users\\战神\\AppData\\Local\\Programs\\Python\\Python37',
#  'C:\\Users\\战神\\AppData\\Local\\Programs\\Python\\Python37\\lib\\site-packages']

print(sys.path)