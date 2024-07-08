import file_manager
import model

teacher_name = ''


def show_manager():
    # print('显示管理页面')
    # 读取的不是json文件，因此不用json模块
    # content = file_manager.read_file('students_page.txt')
    global teacher_name
    content = file_manager.read_file('students_page.txt') % teacher_name

    while True:
        print(content.rstrip())
        operate = input('请选择(1~5):')
        if operate == '1':
            add_student()
        elif operate == '2':
            show_student()
        elif operate == '3':
            modify_student()
        elif operate == '4':
            del_student()
        elif operate == '5':
            break
        else:
            print('输入有误')


def add_student():
    x = file_manager.read_json(teacher_name + '.json', {})
    if not x:
        students = []
        num = 0
    else:
        students = x['all_students']
        num = int(x['num'])
    s_name = input('请输入学生姓名：')
    s_age = input('请输入学生年龄：')
    s_gender = input('请输入学生性别：')
    s_tel = input('请输入学生电话：')

    num += 1
    # 字符串的zfill方法，在字符串的前面补 0
    s_id = 'stu' + str(num).zfill(4)
    # 创建一个Student对象

    s = model.Student(s_id, s_name, s_age, s_gender, s_tel)
    students.append(s.__dict__)  # 将数据转换成为字典
    # 拼接字典
    data = {'all_students': students, 'num': len(students)}
    file_manager.write_json(teacher_name + '.json', data)
    answer = input('添加成功!\n1.继续\n2.返回\n请选择(1-2):')
    if answer == '1':
        add_student()
    elif answer == '2':
        return
    else:
        print('你的选择有误，请重新输入')


def show_student():
    answer = input('1.查看所有学生\n2.根据姓名查找\n3.根据学号查找\n其它: 返回\n请选择:')
    data = file_manager.read_json(teacher_name + '.json', {})

    # if not data: # 如果文件不存在，data是一个空字典
    #     students = []
    # else:
    #     students = data['all_students']
    students = data.get('all_students', [])
    if not students:
        print('该老师还没有学员，请添加学员')
        return

    if answer == '1':
        for student in students:
            print('学号{},姓名{},性别{},年龄{},📞{}'.format(student['s_id'], student['name'], student['gender'], student['age'],
                                                    student['tel']))
    elif answer == '2':
        student_name = input('请输入你要查找的学生姓名：')
        # for student in students:
        #     if student_name in student['name']:
        #         # 字典拆包 **
        #         print('学号{},姓名{},性别{},年龄{},📞{}'.format(student['s_id'],student['name'],student['gender'],student['age'],student['tel']))
        #         return
        #     else:
        #         print('你要查找的学生不存在')

        # 第一种方法
        same_student_name = []
        for student in students:
            if student['name'] == student_name:
                same_student_name.append(student_name)
            print('学号:{s_id},姓名:{name},性别:{gender},年龄:{age},📞:{tel}'.format(**student))
        if not same_student_name:
            print('未找到学员')

        # 第二种方法使用filter类,他是一个可迭代对象
        # same_name_student = filter(lambda student:student['name']==student_name,students)
        #         print('学号:{s_id},姓名:{name},性别:{gender},年龄:{age},📞:{tel}'.format(**student))

    elif answer == '3':
        student_num = input('请输入你要查找的学生学号:')
        for student in students:
            if student_num in student['s_id']:
                print('学号:{s_id},姓名:{name},性别:{gender},年龄:{age},📞:{tel}'.format(**student))
                break
        else:
            print('你要查找的学生不存在')


    else:
        return


def modify_student():
    pass


def del_student():
    data = file_manager.read_json(teacher_name + '.json', {})
    # if data == {}:
    #     students = []
    #     print('该老师还没有学生，请添加学生')
    #     return
    # else:
    #     students = data['all_students']
    all_students = data.get('all_students', [])
    key = value = ''

    x = input('1.按姓名删除\n2.按学号删除\n其它: 返回\n请选择:')
    if x == '1':
        key = 'name'
        value = input('请输入你要删除的学生姓名:')

        # for student in students:
        #     if student['name'] == s:
        #         print('学号:{s_id},姓名:{name},性别:{gender},年龄:{age},电话:{tel}'.format(**student))
        #         student.clear()

        # else:
        #     print('没有找到你想要删除的学生')
    elif x == '2':
        key = 's_id'
        value = input('请输入你要删除的学生的学号:')

        # for student in students:
        #     if student['name'] == s_num:
        #         data['all_students'].pop(student)
        #         break
        # else:
        #     print('没有找到你想要删除的学生')
    else:
        return

    students = list(filter(lambda s: s.get(key, '') == value, all_students))
    if not students:
        print('没有找到对应的学生')
        return
    else:
        for i, s in enumerate(students):
            print('{x},学号:{s_id},姓名:{name},性别:{gender},年龄:{age},📞:{tel}'.format(x=i, **s))
    n = input('请输入需要删除的学生标号(0~{}),q-返回:'.format(len(students) - 1))  # len()里面不能是可迭代对像

    if not n.isdigit() or not 0 <= int(n) <= len(students) - 1:
        print('输入的内容不合法')
    else:
        # 将学生从all_students里删除
        # all_students.pop(n)
        all_students.remove(list(students)[int(n)])
        data['all_students'] = all_students  # 列表的更新
        file_manager.write_json(teacher_name + '.json', data)
