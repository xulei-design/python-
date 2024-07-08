import re

# 在python的正则表达式里，默认是贪婪模式，尽可能多的匹配
# 在贪婪模式后面添加问号，可以将贪婪模式转换为非贪婪模式
m = re.search(r'm.*a', 'ajagb3mfhaiha')
print(m.group())

n = re.search(r'm.*?a', 'ajagb3mfhaiha')
print(n.group())

x1 = re.match(r"aa(\d+)", "aa2343ddd")
print(x1.group())  # aa2343
print(x1.group(1))

x2 = re.match(r"aa(\d+?)", "aa2343ddd")
print(x2.group())  # aa2
print(x2.group(1))  # 2
#
x3 = re.match(r"aa(\d+)ddd", "aa2343ddd")
print(x3.group())  # aa2343ddd
print(x3.group(1))  # 2343

x4 = re.match(r"aa(\d+?)ddd", "aa2343ddd")
print(x4.group())  # aa2343ddd
print(x4.group(1))  # 2343

# 先保证能全部匹配，然后在保证尽可能少的匹配
x5 = re.match(r"aa(\d+?)(.*)", "aa2343ddd")
print(x5.group())  # aa2343ddd
print(x5.group(1))  # 2
print(x5.group(2))  # 343ddd

x6 = re.match(r"aa(\d??)(.*)", "aa2343ddd")
print(x6.group())  # aa2343ddd
print(x6.group(1))  # 空
print(x6.group(2))  # 2343ddd

src = '<img data-original="https://rpic.douyucdn.cn/appCovers/2016/11/13/1213973_201611131917_small.jpg" src="https://rpic.douyucdn.cn/appCovers/2016/11/13/1213973_201611131917_small.jpg" style="display: inline;">'
x6 = re.search(r'https://.*?\.jpg', src)
print(x6.group())