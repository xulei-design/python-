class Singleton(object):
    __instance = None
    __is_first = True

    @classmethod
    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            # 申请内存，创建一个对象，并把对象的类型设置为cls,将这个申请的地址赋值给这个对象
            cls.__instance = object.__new__(cls)
            print(cls.__instance)

        return cls.__instance

    def __init__(self, a, b):
        if self.__is_first:
            self.a = a
            self.b = b
            self.__is_first = False


# 1. 调用 __new__ 方法申请内存空间
# 如果不重写 __new__ 方法，会调用 object 的 __new__ 方法
# object 的__new__ 方法会申请内存空间
# 如果重写了 __new__方法，需要自己手动申请内存空间
s1 = Singleton('呵呵', '嘿嘿嘿')

print(s1)
print(hex(id(Singleton)))
# s2 = Singleton('哈哈哈', '嘤嘤嘤')
# # print(type(s1))
# print(s1.a, s2.a)  # 哈哈哈 哈哈哈
# print(s1.b, s2.b)  # 嘤嘤嘤 嘤嘤嘤
#
# # print(s1 is s2) # True
# print(s1, s2)
