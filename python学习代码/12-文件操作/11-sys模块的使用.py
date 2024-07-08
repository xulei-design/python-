import sys
# sys.stdin # 标准输入，可以像input一样，接受用户的输入，就是读取键盘里输入的数据

# 默认都是控制台
# sys.stdout # 标准输出，
# sys.stderr # 错误输出
s_in = sys.stdin
# while True:
#     content = s_in.readline().rstrip('\n')  # hello\n
#     if content=='':
#         break
#     print(content)


# 控制台的输出，输出到了指定文件
sys.stdout = open('stdout.txt','w',encoding='utf8')
print('hello')
print('yes')
sys.stderr = open('stderr.txt','w',encoding='utf8')
print(1 / 0)