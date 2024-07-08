file = open('../003.mp4','rb')

try:
    while True:
        m = file.read(1024)

        if not m:
            break
        print(m)
finally: # 最终都会被执行的代码
    print('文件被关闭了')
    file.close()
