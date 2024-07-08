# split splitlines partition  rpartition

# 字符串数据类型
x = 'zhangsan*lisi*wangwu-jerry-henry-merry-jack-tony'
# ['zhangsan','lisi','wangwu','jerry','henry','merry','jack','tony']
# 使用split 方法，可以将一个字符串切割成一个列表
x.split('-')
m = x.split('*')
print(x) # 字符串是不可变数据类型!!!
print(m) # 切割以后的结果就是一个列表 ['zhangsan', 'lisi', 'wangwu', 'jerry', 'henry', 'merry', 'jack', 'tony']


z = x.rsplit('-')
print(z)

y = x.split('-',2)
print(y) # ['zhangsan', 'lisi', 'wangwu-jerry-henry-merry-jack-tony']
n = x.rsplit('-',2)
print(n) # ['zhangsan-lisi-wangwu-jerry-henry-merry', 'jack', 'tony']


# partition 指定一个字符串作为分割符，分为三部分
# 前面 分隔符 后面
print('abcdefXmpqrst'.partition('X')) # ('abcdef', 'X', 'mpqrst')
print('abcdefXmpqXrst'.partition('X')) # ('abcdef', 'X', 'mpqXrst')
print('abcdefXmpqXrst'.rpartition('X')) # 后面的X来分

# 获取文件名和后缀名
file_name = '2020.2.14不要打开.mp4'
print(file_name.rpartition('.'))

