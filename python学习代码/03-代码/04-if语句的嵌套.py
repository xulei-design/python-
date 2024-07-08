# if 语句里在嵌套if


# python语言里使用强制缩进来表示语句之间的结构
tickt = input('是否买票了?Y/N')
if tickt == 'Y':
    print('买票了，可以进站')
    safe = input('安检是否通过？Y/N')
    if safe == 'Y':
        print('安检通过了，可以候车室')
    else:
        print('进站了，安检未通过')
else:
    print('没有买票，滚蛋')