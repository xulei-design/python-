import os

file_name = input('请输入一个文件路径：')
if os.path.isfile(file_name):  # 判断是否是一个文件
    # 打开旧文件
    old_file = open(file_name, encoding='utf-8')
    # xxx.txt ===> xxx.bak.txt 根据旧文件的名字，自动生成新文件名字
    # names = file_name.rpartition('.')  # ('xxx','.','txt')
    # new_file_name = names[0] + '.bak.' + names[2]

    names = os.path.splitext(file_name)  # ('xxx','.txt')
    new_file_name = names[0]+'.bak'+names[1]
    new_file = open(new_file_name, 'w', encoding='utf-8')  # 打开一个新文件用于写入

    # 把旧文件的数据读取出来写入到新文件
    new_file.write(old_file.read())

    new_file.close()
    old_file.close()
else:
    print('你输入的文件不存在')
