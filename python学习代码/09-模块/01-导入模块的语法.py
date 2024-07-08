# 模块：在python里一个 py 文件，就可以理解为模块
# 不是所有的py文件都能作为一个模块来导入
# 如果想要一个py文件能够被导入，模块名字必须遵守命名规则
# python为了方便我们开发，提供了很多内置模块


import time  # 1.使用 import 模块名  直接导入一个模块
from random import randint # 2.from 模块名 import 函数名，导入一个模块的或者变量
# (将randint方法导入random模块）
from math import *  # 3. from 模块名 import *   导入这个模块的“所有”方法和变量
# （将math模块里的所有方法导入到math模块中）
import datetime as dt  # 4.导入一个模块并给这个模块起一个别名
# (导入datetime模块，同时给这个模块起个别名 dt)
from copy import deepcopy as dp  # 5.from 模块名 import 函数名 as 别名
# （给copy模块导入deepcopy方法，同时给deepcopy方法起一个别名 dp)

# 导入这个模块以后，就可以使用这个模块里的方法和变量
print(time.time())


randint(0,2) # 生成[0,2]的随机整数
# import math
# print(math.pi)
print(pi)
print(dt.MAXYEAR)

dp(['hello','good',[1,2,3],'hi'])