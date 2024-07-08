# 声明一个字典保存一个学生的信息，学生信息包括：姓名，年龄，成绩（单科），电话，性别（男，女，不明）
# student ={'name':'zhangsan','age':18,'score':98,'TEL':'18438696685','sex':'男'}


# 声明一个列表，在列表中保存6个学生的信息（6个题1中的字典）
students = [{'name': 'zhangsan', 'age': 18, 'score': 98, 'TEL': '18438696685', 'sex': '男'},
            {'name': 'lisi', 'age': 28, 'score': 94, 'TEL': '18438696688', 'sex': '女'},
            {'name': 'wangwu', 'age': 21, 'score': 79, 'TEL': '18438696785', 'sex': '男'},
            {'name': 'jack', 'age': 17, 'score': 68, 'TEL': '18438696385', 'sex': '不知道'},
            {'name': 'tony', 'age': 22, 'score': 59, 'TEL': '18438696088', 'sex': '男'},
            {'name': 'chirs', 'age': 16, 'score': 25, 'TEL': '18438626685', 'sex': '不知道'}
            ]
# （1）统计不及格的学生的个数
# （2）打印不及格学生的名字和对应的成绩
# （3）统计未成年人的个数
# （4）打印手机尾号是8的学生姓名
# （5）打印最高分和对应学生的名字（重点看一下）
i = 0
count = 0
max_score = students[0]['score']  # 假设第0个学生的成绩是最高分
max_index = 0  # 假设最高分学生的下标是 0

for i, student in enumerate(students):
    if student['score'] < 60:
        i += 1
        print('%s不及格，成绩是%d' % (student['name'], student['score']))
    if student['age'] < 18:
        count += 1
    if student['TEL'][-1] == '8':
        print('%s的手机尾号是8' % student['name'])
    if student['score'] > max_score:  # 遍历时，发现一个学生的成绩大于假设的最大数
        max_score = student['score']
        # max_index = i  # 修改最高分的同时，把最高分的下标也修改

print('%d个学生不及格' % i)
print('有%d个未成年人' % count)
print('最高分是%d' % max_score)
# print('最高分的获得者是%s' % students[max_index]['name'])
# 多个并列第一时
for student in students:
    if student['score'] == max_score:
        print('最高分的获得者时%s' % student['name'])
