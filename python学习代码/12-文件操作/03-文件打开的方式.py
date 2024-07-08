# mode 指的是文件的打开方式
# r: 只读模式，默认，打开文件以后只能读取，不能写入。如果文件不存在，会报错
# w：写入模式，打开文件以后，只能写入，不能读取.如果文件存在，会覆盖文件；如果文件不存在，会创建文件
# b: 以二进制的形式打开文件
# rb:以二进制读取，wb:以二进制得形式写入，可以用来操作非文本文件

# a：追加模式，会在最后追加内容。如果文件不存在，会创建文件；如果文件存在会追加
# r+: 可读可写。如果文件不存在，会报错
# w+: 可读可写。如果文件存在，会覆盖文件；如果文件不存在，会创建文件


# file = open('xxx.txt','r',encoding='utf8')
# print(file.read())
# file.write('hello') # 不能执行写入操作会报错
# file = open('xx.txt','r',encoding='utf8') #文件不存在时会报错


# file = open('xxx.txt','w',encoding='utf8')
# file.write('hello') # 可以执行写入的操作
# print(file.read()) # 不能够执行读取，会报错
# file = open('yyy.txt','w',encoding='utf8')


# file = open('xxx.txt','rb')
# print(file.read()) #读取的结果是二进制

# file = open('xxy.txt','wb') # 非文字的内容都用二进制形式读取
# file.write('大家好才是真的好'.encode('utf8')) # 报错，只能写入二进制

file = open('xxx.txt', 'w+', encoding='utf8')
file.write('哈哈哈哈')
file.seek(0, 0) # 写入之后，文件指针到最后，需要调用seek重置文件指针到开头
print(file.read())
file.close()
