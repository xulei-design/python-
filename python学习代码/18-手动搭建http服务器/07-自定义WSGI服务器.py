from wsgiref.simple_server import make_server

def demo_app(environ,start_response):
    # environ
    # print(environ)

    #environ 是一个字典，保存了很多的数据
    # 其中重要的一个是 PATH_INFO 能够获取用户访问的路径
    path = environ['PATH_INFO']  # 获取请求路径
    print('path={}'.format(path))
    start_response('200 ok',[('Content_Typw','text/html;charset=utf8'),('Server','BWS/1.1')])
    return ['你好'.encode('utf8')] # 浏览器显示的内容·

if __name__ == '__main__':
    httpd = make_server('', 7090, demo_app)
    sa = httpd.socket.getsockname()
    print("Serving HTTP on", sa[0], "port", sa[1], "...")
    httpd.serve_forever() # 服务器在后台一直运行,来个死循环，不断的运行