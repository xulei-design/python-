#基础类型注解
from typing import Union

var1: int = 10
var2: str = '黑马'
var3: bool = True
my_list = [1,2,3]

def add(x:int,y:int)->int:
    return x + y

add(3,4)

def func(data:list) -> list:
    return data