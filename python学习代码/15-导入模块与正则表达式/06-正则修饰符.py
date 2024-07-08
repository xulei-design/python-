import re

# pattern: 正则表达式
# flags: 正则修饰符


# 正则修饰符是对正则表达式进行修饰
# re.S: 让点 . 匹配换行
# re.I: 忽略大小写
# re.M: 让 $ 匹配到换行


# . 表示除了换行以外的任意字符
x = re.search(r'm.*a', 'snamsji\naohgal',re.S)
print(x.group()) # msji

y =  re.search(r'x','good Xyz',re.I)
print(y.group())  # X


# \w:表示的是字母数字和_ +:出现一次以上  $:以指定的内容结尾
'''
i am boy
you are girl
he is man
'''
z = re.findall(r'\w+$','i am boy\n you are girl\n he is man',re.M)# ['boy', 'girl', 'man']
print(z) # ['boy', 'girl', 'man']