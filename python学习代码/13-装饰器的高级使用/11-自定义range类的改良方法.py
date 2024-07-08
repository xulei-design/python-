class Range(object):
    def __init__(self, end, start=0, setp=1):
        if start != 0:
            start, end = end, start
        self.end = end
        self.start = start
        self.step = setp

    def __iter__(self):
        return self

    def __next__(self):
        x = self.start # 判断以及返回的值，应该是上一个·start 的值
        self.start += self.step
        if x < self.end:
            return x
        raise StopIteration


for i in Range(10, 20, 4):
    print(i)
