def can_play(clock):
    print('最外层函数被调用了，clock={}'.format(clock))

    def handle_action(fn):
        print('handle_action被调用了') # 一下会调用两层
        def do_action(name,game):
            print(hex(id(do_action)))
            if clock <= 21:
                fn(name,game)
            else:
                print('太晚了，别玩了，早点休息')

        return do_action

    return handle_action

# 装饰器函数带参数
# 1.调用can_play函数,将参数12传递给clock.
# 2.调用handule_action函数,将play_game传递给fn,
# 3.此时在调用play_game其实就是调用的是 do_action
@can_play(12)
def play_game(name, game):
    print(name + "正在玩" + game)
    print('play_game地址是0x%X'%id(play_game))

play_game('张三', '王者荣耀') # 此时在调用play_game其实就是调用的是 do_action
