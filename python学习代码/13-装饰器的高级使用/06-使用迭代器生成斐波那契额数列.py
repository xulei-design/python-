class Fibonacci(object):
    def __init__(self, n):
        self.n = n
        self.num1 = self.num2 = 1
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.count += 1
        if self.count <= self.n:
            x = self.num1  # 用于一个变量保存更改之前的值
            self.num1, self.num2 = self.num2, self.num1 + self.num2
            return x
        else:
            raise StopIteration


# 1,1,2,3,5,8,13,21,34,55,89,144
f = Fibonacci(30) # 占时间,不占用空间.一时间换空间
for i in f:
    print(i)

# 既然有列表了,还要有生成器呢
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
x = range(1, 10)
