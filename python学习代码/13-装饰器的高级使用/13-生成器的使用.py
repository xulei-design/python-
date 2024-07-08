# 生成器的形式就相当于一个函数

def my_gen(n):
    i = 0
    while i < n:
        i += 1
        # return i  return表示一个函数的结束
        yield i  # 使用yield 结果是一个生成器  （相当于return)
        print('我是yiled以后的代码')


m = my_gen(10)  # 获取一个生成器
print(next(m))  # 当调用next方法，获取数据时，才会调用方法
print(next(m))  # 当再次调用next方法，会从上一次yield出来的位置继续执行代码


# for x in m:
#     print(x)


def fibonacci(n):
    print('-'*50)
    num1 = num2 = 1
    count = 0
    while count < n:
        count += 1
        yield num1
        num1,num2 =num2,num1+num2



f = fibonacci(6)
for x in f:
    print(x)
