from django.shortcuts import render, redirect
from django.shortcuts import HttpResponse
import requests
from app01 import models
# Create your views here.

def home(request):
    # 1.去request中可以获取请求的数据、

    # 2.根据请求去做业务处理

    # 3. 给浏览器返回内容

    # return HttpResponse("成功")
    # django寻找HTML模板的顺序，在setting.py文件中templates函数中的"DIRS": [],

    #1.配置settings中的templates-->"DIRS": [os.path.join(BASE_DIR,'templates')],

    #2.去已注册的所有app里面的templates目录中寻找
    return render(request,'home.html')

def index(request):

    #通过某个方式，从数据库或从网络请求中获取数据
    data = "中国移动"
    userlist = ["指挥","张三",'李四']
    info = {"name":"吴佩琦","age":18,"email":"xxx@.live.com"}

    context ={
        'v1':data,
        'v2':userlist,
        'v3':info
              }
    return render(request,'index.html',context)

def douban(request):
    # 1. 获取豆瓣电影数据
    # res = requests.get(
    #     url = f"https://movie.douban.com/subject/{movie_id}/",
    #     headers={
    #         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    #     }
    # )
    # datalist = res.json()
    return render(request,'douban.html')


def login(request):

    # 浏览器上输入的地址/跳转
    if request.method == "GET":
        return render(request,'login.html')
    # 否则就是以POST方式提交
    user = request.POST.get("username")
    pwd = request.POST.get("password")

    if user == 'root' and pwd == "123":
        # 登录成功,跳转到百度
        return redirect("https://www.baidu.com/")
    else:
        # 登录失败，依然显示登录页面
        return render(request,'login.html',{"error":'用户名或密码错误'})


def demo(request):
    from app01 import models
    #增加 类
    models.Role.objects.create(title="管理员",count=5)
    models.UserInfo.objects.create(username="许磊",password='123456',age=18)
    models.UserInfo.objects.create(username="李四",password='612522',age=28)
    models.UserInfo.objects.create(**{'username':"暑期",'password':'123','age':52})

    # 删除
    # models.Role.objects.all().delete() #删除所有表
    # models.UserInfo.objects.filter(id=1).delete()
    # models.UserInfo.objects.filter(username='李四').delete()
    # models.UserInfo.objects.filter(username='许磊',age=18).delete()

    # 修改
    # models.Role.objects.all().update(title = "xxx") #将整列title的数据全部改为xxX
    # models.UserInfo.objects.all().update(age = 90)
    # models.UserInfo.objects.filter(age=90).update(age = 25)

    # 查询
    # QuerySet类型 = [obj,obj]

    # v2 = models.UserInfo.objects.filter(id=1)
    # for obji in v2:
    #     print(obji.id,obji.username,obji.password,obji.age)
    #
    # v1 = models.UserInfo.objects.all()
    # for obj in v1:
    #     print(obj.id,obj.username,obj.password,obj.age)


    # 1.获取到userinfo表中的所有数据
    # datalist = models.UserInfo.objects.all()
    # # 2.在页面中进行展示
    # for obj in datalist:
    #     print(obj.id,obj.username,obj.password,obj.age)
    #
    # return render(request,'demo.html',{'datalist':datalist})
    return HttpResponse("成功")

def user_list(request):
    userlist = models.UserInfo.objects.all()
    print(userlist)
    return render(request,'userlist.html',{'datalist':userlist})

def user_delete(request):

    # /user/delete/?uid=6
    uid = request.GET.get('uid')
    models.UserInfo.objects.filter(id=uid).delete()

    return redirect("http://127.0.0.1:8000/user/list/")