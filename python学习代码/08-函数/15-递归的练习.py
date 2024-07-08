# 使用递归求 n! n!=n*(n-1)!    0!=1
# def fac(n):
#     if n == 1:
#         return 1
#
#     return fac(n - 1) * n
#
#
# print(fac(6))
#

# 使用递归求斐波那契额数列的第 n 个数字
def fibonacci(n):
    if n == 2 or n == 1:
        return 1
    return fibonacci(n - 2) + fibonacci(n - 1)


print(fibonacci(9))


# 练习：使用递归函数求n!

def fac(n):

    return fac(n-1)*n