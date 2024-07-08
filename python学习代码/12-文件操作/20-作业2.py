class Student(object):
    def __init__(self, student_number, name, age, gender, score):
        self.student_number = student_number
        self.name = name
        self.age = age
        self.gender = gender
        self.score = score


class Gread(object):
    def __init__(self, gread_name, student_list=None):
        if student_list is None:
            student_list = []
        self.gread_name = gread_name
        self.student_list = student_list

    def show_all_students(self):
        i = 0
        while i < len(self.student_list):
            print('班级{},学号{},姓名{},年龄{},性别{},成绩{}'.format
                  (self.gread_name, self.student_list[i].student_number, self.student_list[i].name,
                   self.student_list[i].age,
                   self.student_list[i].gender, self.student_list[i].score))
            i += 1

    def get_student_number(self, student_number):
        i = 0
        while i < len(self.student_list):
            if self.student_list[i].student_number == student_number:
                print('班级{},学号{},姓名{},年龄{},性别{},成绩{}'.format
                      (self.gread_name, self.student_list[i].student_number, self.student_list[i].name,
                       self.student_list[i].age,
                       self.student_list[i].gender, self.student_list[i].score))
                i += 1
            else:
                return
    # def get_score(self):


s1 = Student('01', '王五', '18', 'male', 98)
s2 = Student('02', '李四', '18', 'male', 88)
s3 = Student('03', 'jery', '28', 'female', 92)
c = Gread('九班', [s1, s2, s3])
c.show_all_students()
c.get_student_number('04')
