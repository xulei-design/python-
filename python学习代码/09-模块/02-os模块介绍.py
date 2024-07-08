# os全称 OperationSystem 操作系统
# os 模块里提供的方法就是用来调用操作系统里的方法
import os

# os.name:获取操作系统的名字     windows系列==> nt   /  非windows系列==> posix
print(os.name) # nt

print(os.sep) # 路径的分隔符    windows  \    非 windows /


# os 模块里的 path 经常使用
print(os.path) # 获取模块的路径


# abspath：获取文件的绝对路径
print(os.path.abspath('01-导入模块的语法.py'))
# isdir：判断是否是文件夹
print(os.path.isdir('02-os模块介绍.py'))
print(os.path.isdir('xxx'))

# isfile判断是否是文件
print(os.path.isfile('02-os模块介绍.py'))
print(os.path.isfile('xxx'))


# exists判断文件是否存在
print(os.path.exists('02-os模块介绍.py'))
print(os.path.exists('mmm.py'))


# splitext 拿取文件名
file_name='2021.3.5.demo.py'
# print(file_name.rpartition('.'))  # ('2021.3.5.demo', '.', 'py')
print(os.path.splitext(file_name))


# os里其他方法的介绍
import os
# os.getcwd()  # 获取当前的工作目录，即当前python脚本工作的目录
# os.chdir('test') # 改变当前脚本工作目录，相当于shell下的cd命令
# os.rename('毕业论文.txt','毕业论文-最终版.txt') # 文件重命名
# os.remove('毕业论文.txt') # 删除文件
# os.rmdir('demo')  # 删除空文件夹
# os.removedirs('demo') # 删除空文件夹
# os.mkdir('demo')  # 创建一个文件夹
# os.chdir('C:\\') # 切换工作目录
# os.listdir('C:\\') # 列出指定目录里的所有文件和文件夹
# os.name # nt->widonws posix->Linux/Unix或者MacOS
# os.environ # 获取到环境配置
# os.environ.get('PATH') # 获取指定的环境配置
#
# os.path.abspath(path) # 获取Path规范会的绝对路径
# os.path.exists(path)  # 如果Path存在，则返回True
# os.path.isdir(path)  # 如果path是一个存在的目录，返回True。否则返回False
# os.path.isfile(path) # 如果path是一个存在的文件，返回True。否则返回False
# os.path.splitext(path)  # 用来将指定路径进行分隔，可以获取到文件的后缀名


