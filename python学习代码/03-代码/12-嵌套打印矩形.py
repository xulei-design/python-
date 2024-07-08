# python 里可以使用一层循环直接打印三角形
i = 0
while i < 5:
    i += 1
    print('*' * i,end='\n')



#总结：外循环用来控制行数，内循环控制列数
# 这一大段代码，用来打印五行五列星星的
j = 0
while j < 10:
    j += 1

    # 本段代码是打印五个星星并且换行
    i = 0
    while i < 8:
        i += 1
        print('*',end=' ')# 打印一个星星不换行
# print('*',end=' ')
# print('*',end=' ')
# print('*',end=' ')
# print('*',end=' ')
    print('') #用来换行
