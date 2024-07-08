# ASCII ==>  Latin1 ==> Unicode 编码
# 字符 ---> 数字编码存在一个对应关系

# 使用内置函数 chr 和 ord 能够查看数字和字符的对应关系
# ord 获取字符对应的编码； chr 根据编码回去对应的字符

print(ord('a'))  # 97
print(chr(68))  # D

print(ord('你'))
print(ord('旗'))

# GBK(国标库 占两个字节） utf-8（统一编码，汉字占三个字节）  BIG5（繁体中文）
# 使用字符串的encode方法，可以将字符串转换成为指定编码集结果
# 如果有一个编码集的结果，想把它转换成对应的字符，使用decode
# GBK编码，一个汉字占两个字节
print('你'.encode('gbk'))  # b'\xc4\xe3'  50403  0b 11000100 11100011
# utf-8编码占三个字节
print('你'.encode('utf-8'))  # b'\xe4\xbd\xa0'  14990752  0b 11100100 10111101 10100000

x = b'\xe4\xbd\xa0'
print(x.decode('utf-8'))
y = b'\xc4\xe3'
print(y.decode('gbk'))


# 把“你好” 使用 gbk 编码
y='你好'.encode('utf8')
print(y) # b'\xe4\xbd\xa0\xe5\xa5\xbd'
print(y.decode('utf8'))# 你好  txt 文本乱码，修改字符集。
print(y.decode('gbk'))  # 浣犲ソ
z = b'\xe4\xbd'
print(z.decode('gbk')) # 浣
