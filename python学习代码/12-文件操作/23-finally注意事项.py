def test(a, b):
    x = a + b
    return x  # 一旦return就表示函数结束
    # finally:
    #     return 'hello' # 这段代码不会被执行，一般情况下，一个函数最多只有一个return


def demo(a, b):
    try:
        x = a / b
    except ZeroDivisionError:
        return '除数不能为0'
    else:
        return x
    finally:
        return 'good' # 如果函数里有finally,finally里的返回值会覆盖之前的返回值


# print(demo(1, 2))
print(demo(1, 0))
