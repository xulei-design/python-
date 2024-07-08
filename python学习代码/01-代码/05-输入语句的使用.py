# python 里使用input 内置函数接受用户的输入
# input()  ===> 括号里写提示内容
# 定义一个变量可以保存用户输入内容
#password = input('请输入输入银行卡密码:')
#print(password)

# 不管用户输入是什么，变量保存的都是字符串，字符串与数字不能作运算。
age = input('今年的年龄')
print(type(age))   #<class 'str'>
print(age)
