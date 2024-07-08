def can_play(fn):
    print('can_play外部函数被调用了')

    def inner(name, game, **kwargs):  # kwargs = {'clock':20}
        clock = kwargs.get('clock', 21)  # 如果不传关键字参数，默认是21点
        if clock >= 21:
            print('太晚了，禁止玩游戏')
        else:
            fn(name, game)

    return inner


@can_play
def play_game(name, game):
    print(name + "正在玩" + game)


play_game('张三', '王者荣耀', clock=20)
