person={'nams':'xulei',
        'age':'20',
        'height':'183',
        'age':'19',# 会替换上一个age值
        'ispass':True, # 值可以是布尔值
        'hobbies':['唱','跳','篮球','rap'], # 也可以是列表
        4:'good',  # key 只能是不可变数据类型
        ('yes','hello'):100}

# 1.字典里的key 不允许重复，如果key重复了，后一个key对应的值会覆盖前一个
# 2.字典里的value可以是任意数据类型，但是key只能使用不可变数据类型，一般使用字符串
print(person)