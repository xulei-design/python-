user_permission = 6 # 0b0110  # 4 + 2 有读写权限 共有7种权限

# 权限因子
# 用户权限 & 权限因子 != 0 那么用户就有这种权限
DEL_PERMISSION = 8 # 0110 & 1000 == 0000
READ_PERMISSION = 4  # 0110 & 0100 ==0100
WRITE_PERMISSION = 2 # 0110 & 0010 == 0010
EXE_PERMISSION = 1 # 0110 & 0001 == 0000


def check_permission(x, y):


    def handle_action(fn):

        def do_action():
            if x & y != 0:  # 有权限可以执行
                print('正在执行相应的权限')
                fn()
            else:
                print('对不起你没有相应的权限')

        return do_action

    return handle_action


@check_permission(user_permission, READ_PERMISSION)
def read():
    print('我正在读取内容')


@check_permission(user_permission, WRITE_PERMISSION)
def write():
    print('我正在写入内容')


@check_permission(user_permission, EXE_PERMISSION)
def excute():
    print('我正在执行内容')

@check_permission(user_permission, DEL_PERMISSION)
def delect():
    print('我正在删除内容')


read()
write()
delect()
excute()