# break和continue在python里只能用在循环语句

# break: 用来结束本轮循环
# continue: 用来结束本轮循环，开启下一轮循环,continue一旦执行就回到判断条件

i = 0
while i < 5:
    if i == 3:
        i += 1
        continue
    print(i)
    i += 1

i = 0
while i < 5:
    if i == 3:
        i += 1
        break
    print(i)
    i += 1

# 不断地询问用户，我爱你，你爱我吗？只要答案不是爱，就一直问，知道答案是爱
answer = input('我爱你，你爱我吗？')
while answer != '爱':
    answer = input('我爱你，你爱我吗？')
# 不断的让用户输入用户名和密码，只要用户名不是zhangsan，密码不是123，就一直问。

user_name = input('请输入用户名')
password = input('请输入密码')
while not(user_name == 'zhangsan' and password == '123'):
    user_name = input('请输入用户名')
    password = input('请输入密码')


while True:
    user_name = input('请输入用户名')
    password = input('请输入密码')
    if user_name == 'zhangsan' and password == '123':
        break