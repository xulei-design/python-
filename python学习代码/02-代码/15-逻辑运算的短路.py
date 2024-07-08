# 逻辑与运算，只有所有的运算数都是True，结果才是True
# 只要有一个运算符是Flase,结果就是Flase
4 > 3 and print('hello world')
4 < 3 and print('你好世界')  #逻辑与运算的短路问题

# 逻辑或运算，只有所有的运算都是Flase,结果才是Flase
# 只要有一个运算数是True, 结果就是True
4 > 3 or print('哈哈哈')
4 < 3 or print('嘿嘿嘿')  # 前面正确后面就不会再走了

# 逻辑运算的结果一定是布尔值吗？ 不一定
# 逻辑与运算做取值是，取第一个为Flase的值； 如果所有的运算数都是True,去最后一个值
print(3 and 5 and 0 and 'hello')#0
print('good' and 'hello' and 'yes' and '100') #100


#逻辑或运算时，取第一个为True的值；如果所有的值都为Flase,去最后一个值

print(0 or [] or 'lisi'or 5)#lisi
print(0 or [] or {} or None) #None