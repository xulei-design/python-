import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind(('0.0.0.0', 9090))

while True:
    server_socket.listen(128)
    client_socket, addr = server_socket.accept()

    data = client_socket.recv(1024).decode('utf8')
    # print('接收到来自客服端{}ip地址的{}端口发送的:{}'.format(addr[0], addr[1], data))
    path = '/'
    if data:  # 浏览器发送过来的数据有可能是空的
        path = data.splitlines()[0].split(' ')[1]
        print('请求路径是{}'.format(path))

    # 响应头
    response_header='HTTP/1.1 200 OK\n'  # (200 OK 成功了）
    response_body = 'hello world'

    if path == '/login':
        response_body = '欢迎来到登录页面'
    elif path == '/register':
        response_body = '欢迎来到注册页面'
    elif path == '/':
        response_body = '欢迎来到首页'
    else:
        # 页面未找到  404 Page Not Found
        response_header = 'HTTP/1.1 404 Page NOT Found\n'
        response_body = '对不起，你要查看的页面不存在!!!'

    # 响应头
    response_header += 'content-type:text/html;charset=utf8\n '# 网页要使用utf8编码格式进行读取
    response_header += '\n'
    # client_socket.send(response_header.encode('utf8'))

    # 响应体
    # response_body = 'hello world'

    # 响应
    response = response_header + response_body

    # 发送给客服端
    client_socket.send(response.encode('utf8'))

    # client_socket.send('helloworld'.encode('utf8'))
