first={'李白','白居易','李清照','杜甫','王昌龄','王维','孟浩然','王安石'}
second={'李商隐','杜甫','李白','白居易','岑参','王昌龄'}


# set 支持很多算数运算，但不支持加法运算
print(first - second)  # A-B运算，A减去A和B的交集
print(first & second)  # A&B运算，A和B的交集
print(first | second)  # A|B运算，A和B的并集
print(first ^ second)  # A^B运算，A和B并集减去A和B的交集