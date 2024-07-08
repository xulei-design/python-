# 写出判断一个数是否能同时被3和7整除的条件语句，并打印相应的结果
# a = int(input('请输入一个数字'))
# b = (a % 3)or(a % 7)
# if b == 0:
#     print('True')
# else:
#     print('Flase')

# 写出判断一个数是否能够被3或者7整除，但是不能同时被3或则7整除的条件语句，并打印相应的结果。
# a = int(input('请输入一个数字'))
# if (a % 3== 0 or a % 7 == 0 )and (a % 21 != 0):
#     print('能够被3或者7整除')


# 输入年，写代码判断输入的是否是闰年，并打印相应的结果。
# new_year = int(input('请输入今年的年份：'))
# if (new_year % 4 == 0 and new_year % 100 != 0) or (new_year % 400 == 0):
#     print('今年是闰年')

# 假设今天的上课时间为15678秒，编程今天上课时间是多少小时，多少分钟，多少秒，以“xx时xx分xx秒”，的方式表达出来
# time = int(input('请输入今天上课的时间：'))
# hour = time // 3600
# minute = (time - hour * 3600) // 60
# second = time % 60
# print(hour,'小时',minute,"分钟",second,"秒")


# 定义两个变量保存一个人的身高和体重，编程实现这个人的身材是否正常！
# 公式： 体重(kg)/身高(m)的平方值在18.5~ 24.9之间属于正常。
weight = float(input('请输入你的体重(kg):'))
height = float(input('请输入你的身高(m):'))
square = weight / height**2
if   18.5 < square < 24.9:
    print('身材正常')
else:
    print('身材异常')