persons = [{'name': 'zhangsan', 'age': 18},
           {'name': 'lisi', 'age': 20},
           {'name': 'wangwu', 'age': 19},
           {'name': 'jerry', 'age': 21}
           ]
# 让用户输入姓名，如果用户姓名已存在，提示用户：如果姓名不存在，继续输入年龄，并存入列表
name1 = input('请输入你的姓名：')
for person in persons:
    # if name1 in person.values(): # in 运算符，如果用在字典上，是用来判断key是否存在，而不是value
    if person['name']==name1:
        print('你输入的用户名已存在')
        break
else: # 跳出for循环
    # print('你输入的用户名不存在')
    #创建一个新的字典 new_person
    new_person = {'name':name1}
    age1 = int(input('请输入你的年龄：'))
    new_person['age']=age1
    persons.append(new_person)
    print('用户添加成功')
print(persons)
#     else:
#         age1 = int(input('请输入你的年龄：'))
#         person['name'] = name1
#         person['age'] = age1
# print(persons)
