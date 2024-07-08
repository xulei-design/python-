# 1. 数字和字母都表示它本身
# 2. 很多字母前面添加 \ 会有特殊含义(重点1）
# 3. 绝大多数标点符号都有特殊含义(重点2)
# 4. 如果想要使用标点符号，需要在其前面加 \
import re

# 字母 x 表示他本身
re.search(r'x','helloxdex')
re.search(r'5','23r45938')

print(re.search(r'd','good')) # 字母 d 是普通字符
print(re.search(r'\d','good')) # \d 有特殊含义，不在表示字母 d
print(re.search(r'\d', 'waobasb3i8'))

# re.search('+','1+2') 不能直接使用，+ 有特殊含义
print(re.search(r'\+', '1+2'))