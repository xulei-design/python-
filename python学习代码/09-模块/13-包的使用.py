# 可以将多个具有相似或者关联的多个模块放到一个文件夹里，便于统一管理
# 这个文件夹，我们称之为包
# python包里，会有一个 __init__.py 文件
#
# from chat import recv_msg
# from chat.send_msg import x
import json
import chat
print(chat.recv_msg.y)
print(chat.send_msg.x)