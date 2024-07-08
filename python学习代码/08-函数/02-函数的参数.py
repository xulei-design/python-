# def 函数名(参数)：
#   函数体
# 调用函数： 函数名(参数)


# 在函数声明时，在括号里的参数我们称之为形式参数，简称形参（需要改变的量）
# 形参的值是不确定的，只是用来占位
def tell_story(place, person1, person2):
    print('从前有座山')
    print('山里有座' + place)
    print('庙里有个' + person1)
    print('还有一个' + person2)
    print(person1 + '再给' + person2 + '讲故事')
    print('故事的内容同是')


# 调用函数时传递数据
# 函数调用时传入的参数，才是真正参与运算的数据，我们称之为实参

tell_story('道观', '老观', '道童')  # 会把实参一一对应的传递，交给形参处理
tell_story('尼姑庵', '师太', '小尼姑')
tell_story(place='河', person1='禅师', person2='青年') # 可以通过变量赋值的方式给形参提供参数
