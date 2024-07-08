# 序列化：将数据从内存持久保存到硬盘的过程
# 反序列化：将数据和硬盘加载到内存的过程

# write 只能写入字符串或者二进制
# 字典，列表，元组，数字，等都不能直接写入到文件中

# 将数据装换成为字符串（使用repe或则 str)   但是用更多是使用json模块
# json 本质就是字符串，区别在于json里要使用双引号表示字符串
# 将数据转换成为二进制写入：使用pickle模块
import json
# file = open('name.txt','w',encoding='utf8')
# names = ['zhangsan','lisi','jack','xulei']
# # file.write(json.dumps(names)) #  '["zhangsan", "lisi", "jack", "xulei"]' dumps需要手动写入
# # json.dump(names,file) # 不需要手动写入
#
#
# file.close()


# json 将数据持久化有两个方法
# dumps 的作用是将数据装换成为json字符串，不会将数据保存到文件里。
# dump  的作用是将数据装换成为字符串的同时写入到指定文件。


# json 反序列化也有两个方法：
# loads:将json字符串加载为python里的数据
# load: 读取文件，把读取的内容加载成为python里的数据
m = '{"name":"zhangsan","age":18}'  # 符合json规则的字符串
p = json.loads(m)
print(p)
print(type(p))

# 读取一个文件，将文件里的json字符串加载成一个对象
file1 = open('name.txt','r',encoding='utf8')
y = json.load(file1)
print(y)
print(type(y))
file1.close()