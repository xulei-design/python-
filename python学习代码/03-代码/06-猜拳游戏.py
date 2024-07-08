import random

player = int(input('请输入 (0)剪刀 (1)石头 (2)布：'))
print('用户输入的是',player)

# 电脑应该出一个随机数 [0,2]
# 需要使用到随机数模块 random
# random.randint(a,b) ==> 能够生成[a,b] 的随机数
computer = random.randint(0,2)
print('电脑出的是',computer)
if ((player == 0) and (computer == 2)) or ((player ==1) and (computer == 0)) or ((player == 2) and (computer == 1)):
    print('获胜，哈哈，你太厉害了')
elif player == computer:
    print('平局，要不再来一局')
else:
    print('输了，不要走，洗洗手接着来，决战到天亮')

