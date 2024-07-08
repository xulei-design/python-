from django.shortcuts import redirect
from django.utils.deprecation import MiddlewareMixin

"""
自己定义的中间件
"""

class DemoMiddle(MiddlewareMixin):

    def process_request(self, request):
        # 无需登录的页面，给他放行
        if request.path_info == "/login/":
            return None

        # 校验用户是否已登陆
        user_info = request.session.get("userinfo")
        if not user_info:
            # 未登录，返回登陆页面
            return redirect('login/')
        request.unicom_userid = user_info['id']
        request.unicom_username = user_info['username']
        return None

    def process_response(self, request, response):

        return response
