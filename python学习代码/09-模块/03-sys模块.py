# sys 系统相关的功能
import sys
import random

print('hello world')
print('呵呵呵呵')

#['D:\\python学习代码\\09-内置模块',
# 'D:\\python学习代码\\09-内置模块',
# 'C:\\Users\\战神\\AppData\\Local\\Programs\\Python\\Python37\\python37.zip',
# 'C:\\Users\\战神\\AppData\\Local\\Programs\\Python\\Python37\\DLLs',
# 'C:\\Users\\战神\\AppData\\Local\\Programs\\Python\\Python37\\lib',
# 'C:\\Users\\战神\\AppData\\Local\\Programs\\Python\\Python37',
# 'C:\\Users\\战神\\AppData\\Local\\Programs\\Python\\Python37\\lib\\site-packages']
print(sys.path) # 结果是一个列表，表示查找模块的路径
# sys.exit() # 程序退出，和内置函数exit功能一致

# sys.stdout 和 sys.stderr 默认都是在控制台
# sys.stdin   #  可以像input一样接受用户输入，和 input 相关（可以不断地输入）
# sys.stdout    # 修改sys.stdout 可以改变默认输出位置
sys.stderr     # 修改sys.stderr 可以改变错误输出的默认位置
print('hello')