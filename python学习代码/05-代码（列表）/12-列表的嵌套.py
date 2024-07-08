# nums = [1, 2, [100, 200, 300], 3, 4, 5]
import random

# 一个学校，有3个办公室，现在有8位老师等待工位的分配，请编写程序，完成随机的分配
teachers = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
rooms = [[], [], []]

for teacher in teachers:
    room = random.choice(rooms)  # chioce 从列表里随机选择一个数据
    room.append(teacher)

print(rooms)
# 第0个房间里有3个人，分别是...


# 带下标一般都是用while循环
# for 循环也可以带下标，格式如下：
# 获取房间下标
for i, room in enumerate(rooms):
    print('房间%d里一共还有%d个老师，分别是:' % (i, len(room)),end='')
    for teacher in room:
        print(teacher,end=' ')
    print()