# 在程序运行过程中，优于编码不规范等造成程序无法正常执行，此时程序会报错
# 健壮性：很多编程语言里都有异常处理机制。

def div(a, b):
    return a / b

try:
    x = div(5, 0)
    print('呵呵呵呵呵')
except Exception as e: # 如果程序出错了，会立刻跳转到 except 语句
    print('程序出错了!!!!!')
else: # 当程序运行没有出错，会执行else语句里的代码
    print('计算的结果是'+str(x))



# x += 3
# print(x)
