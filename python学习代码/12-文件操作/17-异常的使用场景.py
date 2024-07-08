age = input('请输入你的年龄：')

# if age.isdigit():
try:
    age = float(age)
except ValueError as e:
    print('输入的不是数字')
else:
    if age > 18:
        print('欢迎来到我的网站')
    else:
        print('未成年人禁止入内')
# else:
#     print('请输入数字')
