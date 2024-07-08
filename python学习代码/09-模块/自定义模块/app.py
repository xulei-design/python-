import random
#1.创建300名员工
"""
user_list = []
for i in range(1,301):
    item = "工号-{}".format(i)
    user_list.append(item)


"""

user_list = ['工号-{}'.format(i) for i in range(1,301)] #推导式

#2.奖项信息
data_list = [("三等奖",5),('二等奖',3),('一等奖',2),('特等奖',1)]
#3.抽奖
for item in data_list:
    text = item[0]
    count = item[1]
    #抽取count个员工，恭喜他们获奖
    luck_user_list = random.sample(user_list,count)
    user_string =",".join(luck_user_list)
    message = '荣获{}的名单:{}'.format(text,user_string)
    print(message)