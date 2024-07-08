# uuid 用来生成全局唯一的id
import uuid
print(uuid.uuid1())  # 32个长度 每个字符有16个选择  32**16


# uuid3和uuid5是使用传入的字符串根据指定的算法算出来的，是固定的
print(uuid.uuid3(uuid.NAMESPACE_DNS,'zhangsan'))  # 生成固定的uuid  通过计算一个命名空间和名字的md5散列值来给出一个uuid
print(uuid.uuid5(uuid.NAMESPACE_DNS,'zhangsan'))  # 生成固定的uuid  和uuid3基本相同，只不过采用的散列算法是sha1

# 使用最多的是uuid4
print(uuid.uuid4())
