'''1.用户名匹配
要求：1.用户名只能包含数字 字母 下划线
      2.不能以数字开头
      3.长度在6~16位范围内'''
import re
#
# user_name = input('请输入你所创建的用户名：')
#
# # x = re.match(r'^[a-zA-Z_][a-zA-Z0-9_]{5,15}$',user_name)
# x = re.fullmatch(r'[a-zA-Z_][a-zA-Z0-9_]{5,15}', user_name)
# if x is None:
#     print('输入的用户名不符合规范')
# else:
#     print(x)
#
# '''
# 2.密码匹配
#     要求：1.不能包含 ! @#&*^%这些符号
#           2.必须以字母开头
#           3.长度在 6 到 12 位之间
# '''
# password = input('请输入你的密码：')
# # y = re.match(r'^[a-zA-z][^!@#&*^%]{5,11}$',password)
# y = re.fullmatch(r'[a-zA-z][^!@#&*^%]{5,11}', password)
# if y is None:
#     print('密码不符合规范')
# else:
#     print(y)

# 查找demo文件以1000phone开头的语句，并保存到列表中
# z = []
# try:
#     with open('demo.txt', 'r', encoding='utf8') as file:
#         while True:
#             content = file.readline().strip()
#             if not content:
#                 break
#             if re.match(r'^1000phone',content):
#                 z.append(content)
#
# except FileNotFoundError:
#     print('文件打开失败')
# print(z)


'''
4.ipv4格式的ip地址匹配
'''
# ip地址检测 0.0.0.0~255.255.255.255

num = input('请输入一个数字：')
x = re.fullmatch(r'\d{,2}|1',num)
print(x)
