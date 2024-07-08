score = float(input('请输入你的分数：'))

# 多个if语句，语句和语句之间，不存在关联，断点的使用
if 60 > score >= 0:
    print('你是个垃圾')

if 80 > score >= 60:
    print('一般般')

if 90 > score >= 80:
    print('还不错')

if 100 >= score >= 90:
    print('你好棒棒幺')

# 一个 if...elif...elif 语句
if 60 > score >= 0:
    print('你个垃圾')
elif 80 > score >= 60:
    print('一般般')
elif 90 > score >= 80:
    print('还不错')
elif 100 >= score >= 90:
    print('你好棒棒哟')
else:
    print('输入有误')