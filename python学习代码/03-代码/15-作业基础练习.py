# score = float(input('请输入你的成绩：'))
# if score < 60:
#     print('不及格')
# else:
#     print('及格')


# age = int(input('请输入你的年龄：'))
# if 0 < age < 18:
#     print('未成年')
# elif  18 <= age <= 150:
#     print('成年')
# else:
#     print('这不是人')


# a = int(input('请输入一个数字：'))
# b = int(input('请再输入一个数字：'))
# sum = a - b
# if sum % 2 != 0:
#     print(sum)
# else:
#     print('结果不是奇数')
#

# for y in range(0 , 101):
#     if y % 2 != 0:
#         print(y)

# 用while 循环输出0到100内的所有偶数
# i = 0
# while i < 101:
#     if i % 2 ==0:
#         print(i)
#     i += 1


# 使用循环计算出1到100求和的结果
# i = 0
# sum = 0
# while i < 100:
#     i += 1
#     sum = i + sum
# print(sum)

# 统计100以内个位数是2并且能够被3整除数的个数
# count = 0 # 定义一个变量来表示个数
# # for num in range(0,101):
# #     if num % 3 == 0 and num % 10 == 2:
# #         count += 1
# # print('满足条件的个数是',count,'个')


#输入一个正整数，求它是几位数
# num = int(input('请随机输入一个正整数：'))#32458.
# count = 0
# while True:
#     num //= 10
#     count += 1
#     if num == 0:
#         break
# print('你输入的数字是',count,'位数')


#打印水仙花数。
# 说明：水仙花是一个三位数，其各位数字的立方和等于该数本身。
# 例如：153是水仙花数，因为 153 = 1**3+5**3+3**3
# for num in range(100,1000):
#     a = num % 10
#     b = num // 10 % 10
#     c = num // 100
#     if num == a**3+b**3+c**3:
#         print(num,'是水仙花数')


#写一个程序可以不断地输入数字，如果数字是0，打印程序结束后结束该程序

# while True:
#     num = int(input('请输入一个数字：'))
#     if num == 0:
#         print('程序结束')
#         break


# 统计100-200中素数的个数，并且输出所有素数。（素数又叫质数，只能被1和他本身整除的数）
for num in range(100,201):
    for i in range(2,10):
        if num // i != 0:
            print(num,'是素数')
