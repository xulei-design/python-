# # 求1-100的所有整数之和
i = 0
sum = 0 # 定义一个变量用来保存所有数字之和
while i < 100:
    i = i + 1
    sum = sum + i
print(sum)


# 求1-100的所有偶数之和
i = 0
sum = 0 # 定义一个变量用来保存所有数字之和
while i < 100:
    i = i + 1
    if i % 2 == 0:
        sum = sum + i
print(sum)