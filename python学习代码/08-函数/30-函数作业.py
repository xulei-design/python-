# 1.编写一个函数，求1-n的和
def sum_add(n):
    sum = 0
    for x in range(1, n + 1):
        sum += x
    return sum


print(sum_add(9))


# 法二：递归函数求1~n的和
def add(n):
    if n == 1:
        return 1
    return add(n - 1) + n


print(add(9))

# 编写一个函数，求多个属中的最大值
nums = [9, 5, 6, 4, 12, 2, 7, 1]


def max_num(nums):
    index = 0
    for i, num in enumerate(nums):
        print('nums列表中的{}个数时{}'.format(i, num))
        if num > nums[0]:
            index = i
    return nums[index]


print(max_num(nums))

# 3.编写一个函数，实现摇筛子的功能，打印n个骰子的点数和
from random import randint

print(randint(1, 6))


def m():
    return randint(1, 6)


def sum_pointcount(n):
    i = 0
    sum = 0
    while i < n:
        sum += m()
        print('本次骰子投掷的点数时{}'.format(m()))
        i += 1
    return sum


x = sum_pointcount(6)
print(x)

# 4.编写一个函数，交换字典的'key'和'value'
dicts = {'name': 'xulei', 'age': 18}


def exchange(dicts):
    print('dicts={}'.format(dicts))
    for k, v in dicts.items():
        print('k={},v={}'.format(k, v))
        v = k

    return x


print(exchange(dicts))

# 5.编写一个函数，提取指定字符串中所有的字母，然后拼接在一起产生一个新的字符串
strs = '123456ophyk%od'


def zifu(strs):
    x = ''
    for str in strs:
        if str.isalpha():
            x += str
    return x


print(zifu(strs))

# 6.写一个函数，求多个数的平均值
nums = [9, 5, 6, 4, 12, 2, 7, 1]
def advantage(nums):
    sum = 0
    for num in nums:
        sum+=num
    return sum/(len(nums)+1)


print(advantage(nums))

# 7.写一个函数，默认求10的阶乘，也可以求其它数的阶乘
def fac(n=10):
    if n==0:
        return 1
    return fac(n-1)*n


print(fac())

# 8.写一个自己的capitalize,能够指定字符串的首字母变成大写
l='helloworld'
def uper(word):
    c = word[0]
    if c.isalpha():
        new_str=word[1:]
        return c.upper()+new_str
    return word


print(uper('hello'))

# 写一个自己的isdigit函数，判断一个字符串是否是纯数字
# 写一个自己的rjust函数，创建一个字符串长度时指定长度，源字符串在新字符串中左右对齐，剩下的部分用指定的数字填充
# 写一个自己的index函数，统计指定列表中指定元素的所有下标，如果列表中没有指定元素返回-1
# 写一个自己的len函数，统计指定序列中元素的个数