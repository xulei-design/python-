import json
from wsgiref.simple_server import make_server


def demo_app(environ, start_response):
    path = environ['PATH_INFO']  # 获取请求路径
    # print(environ.get('QUERY_STRING')) # QUERY_STRING ===> 获取到客户端GET请求方式传递的参数
    # POST 请求方式

    status_code = '200 OK'  # 默认状态码是200
    if path == '/':
        response = '欢迎来到我的首页'
    elif path == '/test':
        response = json.dumps({'name': 'zhangsan', 'age': 18})
    elif path == '/demo':
        with open('./pages/xxx.txt', 'r', encoding='utf8') as file:
            response = file.read()
    elif path == 'hello':
        with open('./pages/hello.html', 'r', encoding='utf8') as file:
            response = file.read()
    else:
        status_code = '404 Not Found'  # 如果页面没有配置，返回404
        response = '页面走丢了'
    print('path={}'.format(path))
    start_response(status_code, [('Content_Typw', 'text/html;charset=utf8')])
    return [response.encode('gbk')]  # 浏览器显示的内容·


if __name__ == '__main__':
    httpd = make_server('0.0.0.0', 7894, demo_app)
    sa = httpd.socket.getsockname()
    print("Serving HTTP on", sa[0], "port", sa[1], "...")
    httpd.serve_forever()  # 服务器在后台一直运行,来个死循环，不断的运行
