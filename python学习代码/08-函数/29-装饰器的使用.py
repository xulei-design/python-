# 产品经理：提需求 / 改需求
# 如果超过22点，不让玩游戏，如果不告诉时间，默认不让玩游戏

def can_play(fn):
    def inner(x, y, *args, **kwargs):
        # clock = kwargs['clock']
        clock = kwargs.get('clock', 23)
        if clock < 22:
            fn(x, y)
        else:
            print('太晚了，早点睡')

    return inner


# 开放封闭原则
@can_play
def play_games(name, game):
    print('{}正在玩{}'.format(name, game))


play_games('张三', '王者荣耀', clock=23)
play_games('李四', '绝地求生', clock=12)
