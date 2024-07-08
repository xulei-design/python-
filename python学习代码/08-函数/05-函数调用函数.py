def test1():
    print('test1开始了')
    print('test1结束了')


# 函数只要不调用就不会执行
def test2():
    print('test2开始了')
    test1()
    print('test2结束了')


test2()


# 定义一个函数，求[n,m)之间所有整数之和
def add(n, m):
    sum1 = 0
    for x in range(n, m):
        sum1 += x
    return sum1


result = add(0, 101)
print(result)


# 求n的阶乘
def factorial(n):
    sum = 1
    for b in range(1, n + 1):
        sum *= b
    return sum


a = factorial(5)
print(a)


# 计算m阶乘和
def summm(m):
    x = 0
    for a in range(1, m + 1):
        x += factorial(a)
    return x


we = summm(5)
print(we)


# # 求n的阶乘
# def fac(n):
#     sum = 1
#     for x in range(1, n + 1):
#         sum *= x
#     return sum
#
#
# print(fac(5))
#
#
# # 求m阶乘和
# def summm(m):
#     sum = 0
#     for b in range(m+1):
#         x = fac(b)
#         sum += x
#     return sum
#
#
# print(summm(5))
