# 一个模块本质上就是一个py文件
# 自己定义一个模块，其实就是写一个py文件
# import 13-我的模块    如果一个py文件想要当作一个模块被导入，文件名一定要遵守命名规范()

# 导入了一个模块，就能使用这个模块里的变量和函数
import my_module

print(my_module.a)
my_module.test()

print(my_module.add(5, 6))

# 使用from <module_name> import * 导入这个模块里的"所有"的变量和函数
# 本质是读取模块里的 __all__ 属性，看这个属性里定义了哪些变量和函数
# 如果这个模块里没有定义 __all__才会导入所有 _ 开头的变量和函数，只适用于下面这种情况
from demo import *

# 使用from demo import * 写法，不再需要写模块名
print(m)
test()
# print(n)  此时n能用

import demo

print(demo.n)


from hello import *

print(x)
print(y)
# print(_age) # 以一个下划线开始的变量读取不到


