# 将数据到写入到内存涉及到 StringIO 和 BytesIO 两个类
from io import StringIO,BytesIO

s_io = StringIO()
s_io.write('hello') # 把数据写入到内存里缓存起来了
s_io.write('good')
s_io.close()


# file 需要的是一个文件流对象(作用：是的打印结果不输出到控制台，输出到指定文件中）
print(s_io.getvalue(),file=open('sss.txt','w'))

print('good',file=s_io)# 把数据写入到内存 s_io 里缓存起来了
print('yes',file=s_io)
print('world',file=s_io)

print(s_io.getvalue()) # 获取内存 s_io 中的数据

b_io = BytesIO()
b_io.write('你好'.encode('utf8'))
print(b_io.getvalue().decode('utf8'))
b_io.close()