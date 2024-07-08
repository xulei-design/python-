# 递归简单来说，就是函数内部自己调用自己
# 递归最重要的就是找到出口(停止条件）
# 一般结束：没有返回值，循环限制出口，有返回值 return 出口
count = 0


def tell_story():
    global count  # 对函数内部变量进行声明，改变全局变量
    count += 1
    print('从前有座山')
    print('山上有座庙')
    print('庙里有个老和尚')
    print('老和尚再给小和尚讲故事')
    print('故事的内容是')
    if count < 5:
        tell_story()


tell_story()


# 求 1-n 的和（使用递归函数）
def get_sum(n):
    if n == 0:
        return 0
    return get_sum(n - 1) + n # 调用函数，形成递归函数
print(get_sum(9))