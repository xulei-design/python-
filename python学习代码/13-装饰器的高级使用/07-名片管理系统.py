import sys

# 定义一个列表，用来存储所有的名片信息（每个名片是一个字典）
user_list = [
    {'name': '许磊', 'tel': '18438696685', 'qq': '1134686635'},
    {'name': 'wangwu', 'tel': '18437561524', 'qq': '1134681235'},
    {'name': 'jack', 'tel': '12345678910', 'qq': '11346932503'},
]
def check_index():
    pass


# 1.搭结构框架
def add_user():
    # 1. 使用input获取到用户输入的信息
    name = input('请输入姓名：')
    # 1.1 接收到用户姓名以后，立刻验证用户名是否存在
    # for user in user_list:
    #     if user['name'] == name:
    #         print('用户名已存在，请重新输入')
    #         break
    # else:
    #     tel = input('请输入手机号：')
    #     qq = input('请输入QQ：')
    #     # 2.创建一个字典，保存用户输入的数据
    #     user = {'name': name, 'tel': tel, 'qq': qq}
    #     # 3.把创建好的名片放入列表里
    #     user_list.append(user)

    for user in user_list:
        if user['name'] == name:
            print('添加失败，用户名已存在')
            return  # 如果用户名已经存在直接结束整个函数
    tel = input('请输入手机号：')
    qq = input('请输入QQ：')
    user = {'name': name, 'tel': tel, 'qq': qq}
    user_list.append(user)

    print(user_list)


def del_user():
    print(user_list)
    index = input('请输入需要删除的序号:')
    if not index.isdigit():  # 另一种写法：当条件不满足时就return
        print('输入的数字不合法')
    else:
        index = int(index)
        if index < 0 or index > len(user_list) - 1:
            print('你输入的序号不在有效范围内')
        else:
            result = input('确定要删除吗? yes or no')
            if result.lower() == 'yes':
                # del   pop(根据下标删除） remove(删除指定元素）  clear (清空整个列表）
                user_list.pop(index)
                # del user_list[index]
                # user_list.remove(user_list[index])
                print(user_list)


def modify_user():
    index = input('请输入要修改的序号:')
    if not index.isdigit():
        print('你输入的不是一个序号')
        return
    if int(index) < 0 or int(index) > len(user_list) - 1:
        print('你输入的数字不在合理范围之内')
        return
    index = int(index)
    result = input('是否要进行修改~~~yes or no')
    if result.lower() == 'yes':
        user = user_list[index]
        print('你需要修改的信息是:\nname:{name},tel:{tel},qq:{qq}'.format(**user))
        new_name = input('请输入新的姓名：')
        for u in user_list:
            if u['name'] == new_name:
                print('修改失败，新的姓名已存在')
                return
        new_tel = input('请输入新的电话：')
        new_qq = input('请输入新的qq')
        user['name'] = new_name
        user['tel'] = new_tel
        user['qq'] = new_qq
    print(user_list)

def query_user():
    user_name = input('请输入你想要查询名片的姓名：')
    for u in user_list:
        if u['name'] == user_name:
            print('要查询的名片信息为\nname:{name},tel:{tel},qq:{qq}'.format(**u))
            break
    else:
        print('你查询的名片不存在')



def show_all_user():
    print('序号               姓名               手机号                QQ')
    for i, user in enumerate(user_list):
        print(i,user['name'].ljust(20),user['tel'].ljust(20),user['qq'].ljust(20))


def exit_system():
    # print('退出系统')
    answer = input('请你确定要退出吗？~~~~(yes or no)')
    # if answer.upper() == 'YES':
    #     # break # break只能用于循环语句
    #     return True  # 确定要退出了
    ##return answer.lower() == 'yes'
    # 2.第二种退出方式
    if answer.lower() == 'yes':
        # exit() # 内置函数exit可以用来结束整个程序
        # 3.第3种退出方法
        sys.exit()  # sys模块里的exit方法也能退出整个程序


def start():
    while True:
        print('''------------------------------------------\n名片管理系统  V1.0\n
1：添加名片
2：删除名片
3：修改名片
4：查询名片
5：显示所有名片
6：退出系统
    -------------------------------------------''')
        operate = input('请输入你要进行的操作(数字)')
        if operate == '1':
            add_user()
        elif operate == '2':
            del_user()
        elif operate == '3':
            modify_user()
        elif operate == '4':
            query_user()
        elif operate == '5':
            show_all_user()
        elif operate == '6':
            exit_system()
            # result = exit_system()
            # if result == True:
            #     break
            ##if exit_system():
            ##  break
        else:
            print('你输入的操作，请重新输入')


start()
