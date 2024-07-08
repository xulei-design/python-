import socket


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind(('192.168.1.3', 8090))
server_socket.listen(128)
while True:
    client_socket, addr = server_socket.accept()
    data = client_socket.recv(1024)
    print('接收到来自客服端{}ip地址的{}端口发送的:{}'.format(addr[0], addr[1], data.decode('utf8')))
    '''
    #GET 请求方式，GET/POST/PUT/DELETE... ...
    # /index/html?name=jack&age=18 请求路径以及请求参数
    # HTTP/1.1 版本号
    GET /index/html?name=jack&age=18 HTTP/1.1
    
    Host: 192.168.1.3:8090  # 请求的服务器地址
    
    Connection: keep-alive
    Pragma: no-cache
    Cache-Control: no-cache
    # UA 用户代理，最开始设计的目的是，是为了能从请求头里辨识浏览器的类型
    User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36
    Accept: image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8
    Referer: http://192.168.1.3:8090/
    Accept-Encoding: gzip, deflate
    Accept-Language: zh-CN,zh;q=0.9

    '''



    client_socket.send('HTTP/1.1 200 ok\n'.encode('utf8'))
    client_socket.send('content-type:text/html\n'.encode('utf8'))


    client_socket.send('\n'.encode('utf8'))

    client_socket.send('helloworld'.encode('utf8'))
