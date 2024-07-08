#按位与&  按位或| 按位异或^  按位左移<<   按位右移>>  按位取反
#按位与运算同为 1 则为 1，否则为0
#按位与运算同为 1 则为 1，否则为0

a = 23
b = 15
print(a & b)
print(a | b)
print(a ^ b)


# 按位左移
x = 5
print(x<<3) # a << n ==>a*2的n次方  5*(2**3)

# 按位右移
y = 15
print(y>>2) #a>>n  ==>a/2的n次方   15/(2**2)


color =  0xF0384E
red = 0xF0
green = 0x38
blue =0x4E