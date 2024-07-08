# 统计100-200中素数的个数，并且输出所有素数。（素数又叫质数，只能被1和他本身整除的数）
for i in range(100,201):  # 103 2~102
    for j in range(2,int(i ** 0.5) + 1):
        if i % j == 0: # i 除以某一个数，除尽了，i是合数
            # print(i,'是合数')
            break # break放在内循环，用来结束内循环
    else:
        # for...else语句：当循环里的break没有被执行的时候，就会执行else
        print(i,'是质数')