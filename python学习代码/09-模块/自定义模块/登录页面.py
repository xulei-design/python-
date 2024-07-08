import hashlib

def md5(data_string):
    salt = "asjaohgnbdfjioan"
    obj = hashlib.md5(salt.encode('utf-8'))
    obj.update(data_string.encode('utf-8'))
    res = obj.hexdigest()
    return res

def login():
    """
    登录
    :return:
    """
    print("用户登录")
    user = input("请输入用户名:")
    pwd = input("请输入密码:")
    encrypt_pwd = md5(pwd)
    #逐行读取文件中的内容，来进行比较
    is_sucess = False
    with open('db.txt',mode='r',encoding='utf-8') as file_object:
        for line in file_object:
            data_list = line.strip().split(',')
            if data_list[0] == user and data_list[1] == encrypt_pwd:
                if is_sucess:
                    print("登录成功")
                else:
                    print("登录失败")
def register():
    """
    注册
    :return:
    """
    print("用户注册")
    user = input("请输入用户名:")
    pwd = input("请输入密码:")
    encrypt_pwd = md5(pwd)
    line = "{},{}\n".format(user,encrypt_pwd)
    with open('db.txt',mode='a',encoding='utf-8') as file_object:
        file_object.write(line)

def run():
    func_dict = {
        "1":register,
        "2":login
    }
    print("1.注册：2.登录")
    chioce = input("选择序号：")
    func = func_dict.get(chioce)
    if not func:
        print("序号选择错误")
        return
    func()

run()