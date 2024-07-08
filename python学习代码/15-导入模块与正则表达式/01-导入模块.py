# 怎么使用demo模块里的方法呢？

from demo import Person
p = Person('lisi')
p.eat('西红柿盖饭')
p.sleep()

import random
random.randint(2,10)

# 为什么 random 能够使用类名加方法名调用，而demo就不行呢？
# 通过起别名的方法可以实现
demo.eat('西红柿盖饭')