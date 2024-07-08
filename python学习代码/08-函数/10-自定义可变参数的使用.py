def add(a, b):
    return a + b


def add_many(iter):
    x = 0
    for n in iter:
        x += n
    return x


nums = [1, 2, 3, 4, 5, 6]
print(add_many(nums))

print(add_many((5, 8, 6, 1, 9, 2, 4)))

print(add_many({5, 6, 2, 1, 4, 7}))

print(add_many(range(9, 45)))

# 一次input只能接受一次用户输入