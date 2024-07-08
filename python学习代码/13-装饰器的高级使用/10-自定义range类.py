# 作为一个迭代器，需要实现两个魔法方法 __iter__ 和 __next__ 方法
class My_range(object):
    def __init__(self, *args):
        self.step = 1 # 步长默认是 1
        # 如果只有一个参数 count 是结束
        if len(args) == 1:
            self.count = args[0]
        elif len(args) == 2:
            self.n = args[0]
            self.count = args[1]
        elif len(args) == 3:
            self.n = args[0]
            self.count = args[1]
            self.step = args[2]


    def __iter__(self):
        return self

    def __next__(self):
        if self.n < self.count:

            self.n += self.step
            print(self.n - 1)
            return self.n - 1

        else:
            raise StopIteration


y = My_range(10, 20,4)
for i in y: # for...in循环调用__next__方法
    print(y)
