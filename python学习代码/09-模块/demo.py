__all__ = ['m', 'test']

m = 'yes'
n = 100


def test():
    print('我是demo模块里的test方法')


def foo():
    print('我是demo模块里的foo方法')


def division(a, b):
    return a / b


# __name__:当直接运行这个py文件时，值是 __name__
# 如果这个py文件作为一个模块导入的时候，值是文件名
# 应用于一些输出只想在本模块输出，不想在其他模块输出
if __name__=='__main__':
    print('demo里的name是：',__name__)
    print('测试一下division函数，结果是%d' % division(4, 2))
print('demo里的name是：',__name__)
