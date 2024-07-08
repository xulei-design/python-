# 求斐波那契数列中第n个数的值，n是正整数

# 求斐波那契数里的第12个数
# 1,1,2,3,5,8,13,21,34,55,89,144
n = int(input('请输入第几个数的值：'))
num1 = 1
num2 = 1

for i in range(0 , n - 2):
    a = num1
    num1 = num2
    num2 = a + num2
print(num2)