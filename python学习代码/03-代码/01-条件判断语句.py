# python里的条件判断语句 if / if else / if elif elif else
# python里不支持 switch...case 条件语句

# if 条件判断:
#   条件成立时，执行的代码
# age = int(input("请输入你的年龄:"))
# if age < 18: # 字符串和数字做比较运算的规则：字符串==数字，输出Flase,字符串 != 数字，输出 True。不支持其他格式。
#     print('未满十八岁，禁止入内')

# if...else语句
if 判断条件:
  条件满足执行的代码
else:
  条件不满足时执行的代码
age = int(input('请输入你的年龄：'))
if age < 18:
    print('未成年人禁止入内')
else:
    print('欢迎光临')
