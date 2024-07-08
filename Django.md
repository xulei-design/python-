# 初始Django

- Python知识点：函数，面向对象
- 前端开发：HTML CSS JAVASCRIPT jQuery BootStrap
- MySQL数据库
- python的WEB框架
  - Flask,短小精悍 +第三方组件
  - Django ，内部集成了很多组件+第三方组件。【主要】

# 1、安装Django

```python
pip install django
```

```
c:\python39
	- python.exe
	- scripts(安装第三方模块)
		- pip.exe
		- django-admin.exe [工具，自动创建Djangon项目中默认的文件和文件夹]
   - Lib
    - 内置模块
    - random
    - re
    - site-packages
    	-openpyxl
    	- python-docx
    	- flask
    	- django 【框架的源码】
```

# 2、创建项目

**使用django-admin.exe创建项目**

> django中项目中会有一些默认的文件和默认的文件夹

## 2.1、在终端

- 打开终端
- 进入某个目录（项目放在哪里）
- 执行命令创建项目

```
"D:\Anaconda\Scripts\django-admin.exe" startproject 项目名称
```

```
如果"D:\Anaconda\Scripts"已加入环境系统环境变量。
可以执行
django-admin startproject 项目名称
```

- 在pycharm终端中可以执行> django-admin startproject  项目名称 进行项目的创建

![image-20240611160607988](C:/Users/user/AppData/Roaming/Typora/typora-user-images/image-20240611160607988.png)

- 项目目录的介绍

```python
mysite【当前的项目名称】
	manage.py   [管理当前的项目]
    mysite      [当前项目名同名的目录]
     -settings.py [一部分项目的配置文件]jdango内置的也会有一部分的配置文件，如果重回，会将django内置配置文件覆盖掉。
     -wsgi.py
     -asfi.py
     //这两个py文件帮助我们启动django项目接收浏览器发送的请求，并且基于socket来实现网络的通信
     -url.py
     //对应关系——访问的Url和函数的对应关系      例如：访问/login/  执行python中的xxx函数
```

- 启动项目

```
>>> 进入项目目录
>>> 执行下面代码并回车
	- python manage.py runserver
```

- 关闭项目

  ```
  CTRL+C
  ```

  

## 2.2、基于Pycharm创建Django项目

注意：先在自己的pycharm解释器中安装好Django

```
pip install django
```

![image-20240627200757988](C:/Users/user/AppData/Roaming/Typora/typora-user-images/image-20240627200757988.png)

![image-20240627201516767](C:/Users/user/AppData/Roaming/Typora/typora-user-images/image-20240627201516767.png)



## 2.3、使用虚拟环境创建Django项目(自己开发项目时使用)

![image-20240627202252211](C:/Users/user/AppData/Roaming/Typora/typora-user-images/image-20240627202252211.png)

```
manage.py 【项目管理、启动项目、创建app、数据管理】【***常常用，不会修改***】

mysite
	- __init__.py
	- setting.py 【配置文件】【***常常操作、修改***】
	- urls.py 【URL和python函数的对应关系】【***常常操作、修改**】
	- asgi.py 【asgi.py和wsgi.py接收网络请求】【不要动】
	- wsgi.py
```

# 3、APP

```
- 项目










	- app、用户管理 【表结构、函数、HTML模板、CSS】
	- app、订单管理 【表结构、函数、HTML模板、CSS】
	- app、后台管理 【表结构、函数、HTML模板、CSS】
	- app、网站    【表结构、函数、HTML模板、CSS】
	- app、API    【表结构、函数、HTML模板、CSS】
	...PY
	
注意：我们开发比较简洁，用不到多app，一般情况下，项目创建一个app即可
```

- 创建app文件——在pycharm终端中运行命令

```python
 python ./mysite/manage.py startapp app01
```

```
- app01
	- __init.py__
	- admin.py			【固定，不动】Diango默认提供了admin后台管理
	- apps.py   		【固定，不动】app启动类
	- migrations		【固定，不用动】 数据库变更记录
		- __init__.py
	- models.py			【***重要***】对数据库操作
	- test.py			【固定，不动】单元测试
	- view.py			【重要】，函数。
- manage.py
- mysite
	- __init__py
	- __pycache__
	- asgi.py
	- settings.py
	- urls.py		【URL--函数】
	- wsgi.py
```

# 4、Django知识点

## 4.1、快速编写URL和视图函数

![image-20240628134725259](C:/Users/user/AppData/Roaming/Typora/typora-user-images/image-20240628134725259.png)

## 4.2、APP的概念

APP**做业务功能的处理**

```
djangoproject1
	- app01 用户的管理功能 里面有【表结构，HTML模板，CSS，图片】
	- app02 财务管理功能
	- app03 API请求管理
	djangoproject1
		urls.py
		setting.py
		wsgi.py
	manage.py
```

- app的创建

  - 进入python终端，运行下面的语句

  ```
  >>> python manage.py startapp app01
  ```

  - app01中会默认生成一些文件

  ```
  djangoproject1
  	- app01 用户的管理功能 里面有【表结构，HTML模板，CSS，图片】
  		-view.py 【视图函数，接收请求，处理业务逻辑】URL与函数的对应关系都放到这个文件中
  		-models.py【创建数据库表结构，操作表中数据】
  		-migrations
  		-test.py 【固定，不操作】【单元测试】
  		-app.py 【固定，不操作】[app的配置]
  		-admin,py【固定，不操作】【django内置的后台管理】
  	- app02 财务管理功能
  	- app03 API请求管理
  	- djangoproject1
  		- urls.py
  		- setting.py
  		- wsgi.py
  	- manage.py
  ```

![image-20240628140707340](C:/Users/user/AppData/Roaming/Typora/typora-user-images/image-20240628140707340.png)

![image-20240628140923877](C:/Users/user/AppData/Roaming/Typora/typora-user-images/image-20240628140923877.png)



## 4.3、HTML模板

#### 1.第一种寻找HTML模板的方法

>  django寻找HTML模板的顺序，在setting.py文件中templates函数中的"DIRS": [],
>
> "DIRS": [os.path.join(BASE_DIR,'templates')],:项目根目录下的templates文件夹中寻找home.html

#### 2.第二种寻找HTML模板的方法

**去已注册的所有app里面的templates目录中寻找**

**已注册的app:**

- 在settings文件中的INSTALLED_APPS = ["app01.apps.App01Config"]表示将app01注册到django中

总结：优先去项目根目录下的templates目录中找，找不到去app01中的templates中找

![image-20240628143600783](C:/Users/user/AppData/Roaming/Typora/typora-user-images/image-20240628143600783.png)

![image-20240628143901965](C:/Users/user/AppData/Roaming/Typora/typora-user-images/image-20240628143901965.png)

![image-20240628144104903](C:/Users/user/AppData/Roaming/Typora/typora-user-images/image-20240628144104903.png)

## 4.4、模板语法

帮助我们将python中的数据和HTML进行渲染·(替换)，得到字符串，再返回给我们用户浏览器。

![image-20240628152212044](C:/Users/user/AppData/Roaming/Typora/typora-user-images/image-20240628152212044.png)

![image-20240628152239407](C:/Users/user/AppData/Roaming/Typora/typora-user-images/image-20240628152239407.png)

案例：豆瓣电影地址-展示咱们的页面





## 4.5、静态资源

静态资源：图片、css、javascript。

- settings.py

```python
STATIC_URL = "static/"
STATICFILES_DIRS =(
    os.path.join(BASE_DIR,'static'),
)
```

Django就会去项目根目录下的static目录中寻找静态文件。

![image-20240628160531416](C:/Users/user/AppData/Roaming/Typora/typora-user-images/image-20240628160531416.png)

- 去每个已注册的app的static目录下（一般用这个）

```python
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "app01.apps.App01Config"
]
```

本质：只需将app注册到配置文件中，那么以后程序在寻找静态资源，模板文件都会去每个app自己的目录下寻找。

注意事项：如果注册了多个app按照注册顺序的app目录中寻找静态资源

## 4.6、请求与响应（针对视图函数views)

```python
def login(request):
    # -----------接收请求
    # 1.获取请求方式 GET/POST
    print(request.method)
    # 2.获取URL中传递的参数 /login/?n1=123&n2=654&n3=666
    print(request.GET.get('n1'))

    #3.数据放在请求体中传递过来
    print(request.POST)

    #------------------返回值-----响应
    # 4.返回一个文本字符串
    # return HttpResponse("中国联通")

    # 5.返回HTML+数据渲染
    # return render(request,'login.html')

    # 6.返回重定向
    return redirect('https://www.baidu.com')
```

**案例：用户登录**

![image-20240628213254427](C:/Users/user/AppData/Roaming/Typora/typora-user-images/image-20240628213254427.png)

```HTML
login.html
{% load static %}
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
{# 以后引入静态文件，这样写#}
    <link rel="stylesheet" href="{% static 'plugins/bootstrap-3.4.1/css/bootstrap.css' %}">
</head>
<body>
    <h1>用户登录</h1>

    <form action="/login/" method="post">
        {% csrf_token %}
        <input type="text" name="username" placeholder="输入用户名">
        <input type="password" name="password" placeholder="输入密码">
        <input type="submit" value="提交">
        <span style="color: red">{{ error }}</span>
    </form>
</body>
</html>
```

```python
views.py文件
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

```

# 5、数据库操作

今天的案例使用的数据库：

- sqlite数据库，存储数据
- MySQL数据库，存储数据

![224096b9e081363da206822fe71e622e](C:/Users/user/Documents/Tencent%20Files/1134686635/nt_qq/nt_data/Pic/2024-06/Ori/224096b9e081363da206822fe71e622e.png)

settings.py

```python
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}
默认连接sqlite
```

![image-20240629000904035](C:/Users/user/AppData/Roaming/Typora/typora-user-images/image-20240629000904035.png)

## 5.1、创建表

**类--->字段命令**

![cbc9e0f11f45c5af0e333ba503fc1692](C:/Users/user/Documents/Tencent%20Files/1134686635/nt_qq/nt_data/Pic/2024-06/Ori/cbc9e0f11f45c5af0e333ba503fc1692.jpg)

```python
class UserInfo(models.Model):
    username = models.CharField(verbose_name="用户名",max_length=16)
    password = models.CharField(verbose_name='密码',max_length=64)
    age = models.IntegerField(verbose_name="年龄")
```

==表名：app01_userinfo   id:自动创建且为主键自增==\

前提：app01一定要注册·

执行命令在数据库中生成表

- 打开pycharm终端
- 在终端中输入下面两行命令

```python
python manage.py makemigrations
python manage.py migrate
```

## 5.2、操作表中的数据

增删改查

```python
def demo(request):
    from app01 import models
    #增加 类
    # models.Role.objects.create(title="管理员",count=5)
    # models.UserInfo.objects.create(username="许磊",password='123456',age=18)
    # models.UserInfo.objects.create(username="李四",password='612522',age=28)
    # models.UserInfo.objects.create(**{'username':"暑期",'password':'123','age':52})

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

    v2 = models.UserInfo.objects.filter(id=1)
    for obji in v2:
        print(obji.id,obji.username,obji.password,obji.age)

    v1 = models.UserInfo.objects.all()
    for obj in v1:
        print(obj.id,obj.username,obj.password,obj.age)

    return HttpResponse("测试")

```

## 5.3、读取数据库中的数据，并在网页上显示，进行删除操作

- url.py

  ```PYTHON
  urlpatterns = [
      path("xxx/xxx/", views.home),
      # 当访问xxx/xxx/网址的时候会执行home函数
      path('index/',views.index),
      path('douban/',views.douban),
      path('login/',views.login),
      path('demo/',views.demo),
      path('user/list/',views.user_list),
      path('user/delete/', views.user_delete)
  
  ]
  ```

- views.py

```python
def user_list(request):
    userlist = models.UserInfo.objects.all()
    print(userlist)
    return render(request,'userlist.html',{'datalist':userlist})

def user_delete(request):

    # /user/delete/?uid=6
    uid = request.GET.get('uid')
    models.UserInfo.objects.filter(id=uid).delete()

    return redirect("http://127.0.0.1:8000/user/list/")
```

- userlist.html

```HTML
{% load static %}
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>userlist</title>
    <link rel="stylesheet" href="{% static 'plugins/bootstrap-3.4.1/css/bootstrap.css' %}">
</head>
<body>
<div class="container">
<div><h1>用户列表</h1></div>
    <div class="bs-example" data-example-id="contextual-table">
        <table class="table">
            <thead>
            <tr>
                <th>id</th>
                <th>用户名</th>
                <th>密码</th>
                <th>年龄</th>
                <th>操作</th>
            </tr>
            </thead>
            <tbody>
             {% for obj in datalist %}
            <tr class="active">
                <th scope="row">{{ obj.id }}</th>
                <td>{{ obj.username }}</td>
                <td>{{ obj.password }}</td>
                <td>{{ obj.age }}</td>
                <td>
                    <a href="/user/delete/?uid={{ obj.id }}" type="button" class="btn btn-primary btn-sm">删除</a>
                </td>
            </tr>
            {% endfor %}
            </tbody>
        </table>
    </div>
</div>
</body>
</html>
```

![image-20240629211132555](C:/Users/user/AppData/Roaming/Typora/typora-user-images/image-20240629211132555.png)

注意点：

**通过<a>标签跳转的地址，进行GET请求获取用户ID从而进行数据库表中行的删除操作**

# 6、Django开发（新的项目）

主题：资产管理系统

功能：

- 管理员
- 部门
- 资产信息

## 6.1、创建项目

- 创建一个带有虚拟环境的新项目，解释器位置`D:\Anaconda\python.exe`
- 创建一个app，在python终端中执行语句`python manage.py startapp app01`

- 注册app01。在settings.py中的"app01.apps.App01Config"加入到INSTALLED_APPS = []中
- 在app01目录项，创建两个文件夹-templates和static
- 将static目录中的静态文件拷贝过来

## 6.2、创建表结构

### 1、在app01目录下的model.py文件中进行编码

```python
from django.db import models

class Admin(models.Model):
    """管理员表"""
    username = models.CharField(verbose_name="用户名",max_length=16)
    password = models.CharField(verbose_name="密码",max_length=64)

class DepartMent(models.Model):
    """部门表"""
    title = models.CharField(verbose_name="标题",max_length=16)


class AssetSet(models.Model):
    """资产表"""
    name = models.CharField(verbose_name="名称",max_length=32)
    price = models.IntegerField(verbose_name="价格")
    # 只适用于固定的选择
    category = models.SmallIntegerField(verbose_name="资产类型",choices=((1,'办公类'),(2,"3C类"),(3,"房产类")))
	 # 创建外键,在数据库生成的字段名depart_id on_delete=models.CASCADE:级联删除
    depart = models.ForeignKey(verbose_name="所属部门",to="DepartMent",to_field="id",on_delete=models.CASCADE)
```

注意：

- verbose_name="所属部门":对这个外键的解释
- to="DepartMent"：关联到的表的名称
- to_field="id"：关联到表中的列
- on_delete=models.CASCADE：级联删除约束
- 生成的新列名：depart_id

### 2.将创建的提交到数据库的两种方法

1. 在python终端中运行下面代码

```python
python manage.py makemigrations
python manage.py migrate
```

2. 找到工具，点击运行manage.py任务，会弹出一个新的窗口，在窗口中依次输入下面两条执行

快捷键——ctrl+alt+R

```python
makemigrations
migrate
```

![image-20240630155927667](C:/Users/user/AppData/Roaming/Typora/typora-user-images/image-20240630155927667.png)

## 6.3、用户登录

- 登录界面，输入用户名和密码
- 去数据库校验，拿着用户名和密码 跟数据库表中的用户名和密码进行匹配
- 登录成功或者登录失败

### 1、手动录入两个账户

![image-20240630160541278](C:/Users/user/AppData/Roaming/Typora/typora-user-images/image-20240630160541278.png)

### 2、登录页面展示

![image-20240630164630511](C:/Users/user/AppData/Roaming/Typora/typora-user-images/image-20240630164630511.png)

### 3、BUG

- 正常情况下：登录成功以后，才能看到/depart/list/页面
- 我们的项目：之际浏览器上访问`/depart/list`可以看到页面。
- 目的：使得其它浏览器不能直接访问`/depart/list/`页面

如何来解决？cookie和session

1. 将用户登录信息写进session，同时会生成随机字符串作为验证码返回给浏览器

![image-20240701153228759](C:/Users/user/AppData/Roaming/Typora/typora-user-images/image-20240701153228759.png)

2. 当浏览器访问时，浏览器会拿到校验码，跟Django进行比对验证，验证成功读取session中的用户数据，如果读取成功，通过验证。

![image-20240701153341103](C:/Users/user/AppData/Roaming/Typora/typora-user-images/image-20240701153341103.png)

#### 3.1、BUG优化

### 4、cookie和session

![6b9f28f53614e1bd1867022cec5779e3](C:/Users/user/Documents/Tencent%20Files/1134686635/nt_qq/nt_data/Pic/2024-06/Ori/6b9f28f53614e1bd1867022cec5779e3.jpg)

- 写入

```
request.session['name'] = "张三"
```

![image-20240701153228759](C:/Users/user/AppData/Roaming/Typora/typora-user-images/image-20240701153228759.png)

- 读取--其它网页需要验证

```
data = request.session.get('name')
```

![image-20240701153341103](C:/Users/user/AppData/Roaming/Typora/typora-user-images/image-20240701153341103.png)

## 6.4、中间件

在浏览器发送请求后，会经过中间件才会到Django——视图函数，然后经过中间件返回给浏览器——3种形式

返回给浏览器的三种形式：

- 字符串——HttpResponse
- HTML页面——render(request,'login.html')
- 网址——redirect('/asset/list/')

在Django中默认的中间件，在Settings.py文件中的类

![image-20240701161238219](C:/Users/user/AppData/Roaming/Typora/typora-user-images/image-20240701161238219.png)

浏览器与Django后端的运行流程

![09cef2b32ee2b20458a988406de1f497](C:/Users/user/Documents/Tencent%20Files/1134686635/nt_qq/nt_data/Pic/2024-07/Ori/09cef2b32ee2b20458a988406de1f497.png)

### 1、 定义自己的中间件

- 创建一个类——类中有`def process_request(self, request):`和`def process_response(self, request, response):`函数

![image-20240701162322194](C:/Users/user/AppData/Roaming/Typora/typora-user-images/image-20240701162322194.png)

对于`process_request`方法

- 无返回或者返回NONE，请求继续向后走
- 有返回值`return render`,`return HttpResponse`,`return redirect`不会继续向后走，直接执行process_response

### 2、中间件的应用场景

请求过来想统一做什么动作，都可以用

应用场景：

- 日志，获取访问时，请求的IP地址并记录到文件中
- 权限校验，有权限就返回None，无权限就返回无权访问
- 登录判断， 判断用户的session信息
  - ![image-20240701164159729](C:/Users/user/AppData/Roaming/Typora/typora-user-images/image-20240701164159729.png)

## 6.5、用户管理

### 1、用户列表

- 页面搞出来
- 显示表格数据

#### 1.导航和注销

![image-20240701183332669](C:/Users/user/AppData/Roaming/Typora/typora-user-images/image-20240701183332669.png)

![image-20240701183527059](C:/Users/user/AppData/Roaming/Typora/typora-user-images/image-20240701183527059.png)

![image-20240701183739497](C:/Users/user/AppData/Roaming/Typora/typora-user-images/image-20240701183739497.png)

![image-20240701183847249](C:/Users/user/AppData/Roaming/Typora/typora-user-images/image-20240701183847249.png)

#### 2、将表格在页面上展示







## 6.7、模板的继承

显示不同数据库表格，需要多个显示HTML页面，而这些HTML页面中有大多数的显示都是一样的，因此需要使用模板的继承。

- 公共的部分拿到母版中，方便让其它的HTML文件继承

### 1、母版的创建

创建一个母版的HTML文件

![image-20240701192243221](C:/Users/user/AppData/Roaming/Typora/typora-user-images/image-20240701192243221.png)

### 2、继承母版HTML文件

![image-20240701192607423](C:/Users/user/AppData/Roaming/Typora/typora-user-images/image-20240701192607423.png)

上面存在的问题，自己自定义的CSS和JS，子版没办法添加

改进：

- 母版改进

![image-20240701195305855](C:/Users/user/AppData/Roaming/Typora/typora-user-images/image-20240701195305855.png)

- 子版继承改进

![image-20240701195521579](C:/Users/user/AppData/Roaming/Typora/typora-user-images/image-20240701195521579.png)

## 6.8、添加数据

![image-20240701195937309](C:/Users/user/AppData/Roaming/Typora/typora-user-images/image-20240701195937309.png)

- 点击添加
- 页面：导航+form表单+提交
- 接受数据+写入数据库
- 跳转回资产信息表

1. 在添加按钮中添加了一个链接

![image-20240701210303672](C:/Users/user/AppData/Roaming/Typora/typora-user-images/image-20240701210303672.png)

2. 根据请求不同返回不同页面

<img src="C:/Users/user/AppData/Roaming/Typora/typora-user-images/image-20240701210843586.png" alt="image-20240701210843586" style="zoom:200%;" />

## 6.9、删除数据

从网址中获取id

```HTML
<button type="button" class="btn btn-danger"><a href="/depart/delete/?id={{ obj.id }}">删除</a></button>
```

获取完id后，将数据库中对应id的数据删除

```PYTHON
def depart_delete(request):
    id = request.GET.get("id")
    models.DepartMent.objects.filter(id=id).delete()
    return redirect('/depart/list/')
```

## 6.10、编辑数据

- 编辑按钮绑定网址

![image-20240701215926539](C:/Users/user/AppData/Roaming/Typora/typora-user-images/image-20240701215926539.png)

- 创建对应的URL和视图函数

![image-20240701220221963](C:/Users/user/AppData/Roaming/Typora/typora-user-images/image-20240701220221963.png)

- 传过来id，依据id更改数据

![image-20240701220421920](C:/Users/user/AppData/Roaming/Typora/typora-user-images/image-20240701220421920.png)

## 6.11、完成增删改查中出现的小问题

- 增加数据时，数据为空也加入了
- 编辑数据时，数据为空也能提交
- 删除时，应该给出删除提示

# 7、资产管理

## 7.1、资产管理

- 数据库获取资产信息
- 页面循环表格展示(类似于部门列表)

![image-20240702202826711](C:/Users/user/AppData/Roaming/Typora/typora-user-images/image-20240702202826711.png)

## 7.2、chioce字段显示中文

问题：展示数据不友好——对于分类，显示的是数字，我们希望是中文信息chioce

```python
class AssetSet(models.Model):
    """资产表"""
    name = models.CharField(verbose_name="名称", max_length=32)
    price = models.IntegerField(verbose_name="价格")
    # 只适用于固定的选择
    category = models.SmallIntegerField(verbose_name="资产类型", choices=((1, '办公类'), (2, "3C类"), (3, "房产类")))

    # 创建外键,在数据库生成的字段名depart_id on_delete=models.CASCADE:级联删除
    depart = models.ForeignKey(verbose_name="所属部门", to="DepartMent", to_field="id", on_delete=models.CASCADE)
```

![image-20240702203036906](C:/Users/user/AppData/Roaming/Typora/typora-user-images/image-20240702203036906.png)

- 想要拿到chioce的中文——python中

```python
# QuerySet = [obj,obj,obj]
queryset = models.AssetSet.obj.all()
for obj in queryset:
    obj.name obj.price obj.category 
    #获取chioce中的中文
    obj.get_category_display()
    obj.get_字段名_display()
```

- 在html模板中显示——html中

```html
<tbody>
    {% for obj in assetinfo %}
    <tr>
        <th scope="row">{{ obj.id }}</th>
        <td>{{ obj.name }}</td>
        <td>{{ obj.price }}</td>
        <td>{{ obj.get_category_display }}</td>
        <td>{{ obj.depart_id }}</td>
        <td>
            <a href="#" type="button" class="btn btn-danger">删除</a>
            <a href="#" type="button" class="btn btn-primary">编辑</a>
        </td>
    </tr>
    {% endfor %}
</tbody>
```

![image-20240702203740549](C:/Users/user/AppData/Roaming/Typora/typora-user-images/image-20240702203740549.png)

## 7.3、外键关联数据

![image-20240702203955408](C:/Users/user/AppData/Roaming/Typora/typora-user-images/image-20240702203955408.png)

![image-20240702204009850](C:/Users/user/AppData/Roaming/Typora/typora-user-images/image-20240702204009850.png)

目的：想显示关联的外键——部门，而不是显示数字

- models.py

```python
class AssetSet(models.Model):
    """资产表"""
    name = models.CharField(verbose_name="名称", max_length=32)
    price = models.IntegerField(verbose_name="价格")
    # 只适用于固定的选择
    category = models.SmallIntegerField(verbose_name="资产类型", choices=((1, '办公类'), (2, "3C类"), (3, "房产类")))

    # 创建外键,在数据库生成的字段名depart_id on_delete=models.CASCADE:级联删除
    depart = models.ForeignKey(verbose_name="所属部门", to="DepartMent", to_field="id", on_delete=models.CASCADE)
```

- views.py

```python
# QuerySet = [obj,obj,obj]
queryset = models.AssetSet.obj.all()
for obj in queryset:
    obj.name obj.price obj.category obj.depart_id 
    obj.depart #得到一个对象，这个对象的内容是关联表中同一个id的内容，同一行的数据都能拿到
    obj.depart.id #获得主表的id
    obj.depart.title #获得主表中的部门名称，前端同样
```

![image-20240702204848529](C:/Users/user/AppData/Roaming/Typora/typora-user-images/image-20240702204848529.png)

![image-20240702205108587](C:/Users/user/AppData/Roaming/Typora/typora-user-images/image-20240702205108587.png)

## 7.4、添加资产

  



## 1、Form组件

- 自动生成HTML标签 + 半自动读取关联数据
- 表单验证 + 错误提示

如果想要用这个组件，需要一下步骤：

- 创建类

  ```python
  class AssetForm(forms.Form):
      name = forms.CharField(required=True,widget=form.Input)
      price = forms.CharField(required=True,widget=form.Input)
  ```

- 视图函数

```python
def asset_add(request):
    form = AssetForm()
    return render(request,'xxx.html',{"form":form})

```

- html页面中

```htmL
<form>
    {{form.name}}
    {{form.price}}
</form>
```

```html
<form>
    {% for item in form %}
    	{{item}}
    {% endfor %}
</form>
```

## 2、ModelForm组件（主要）

- 自动生成HTML标签 + 半自动读取关联数据（美化）
- 表单验证 +保留之前提交的数据+ 错误提示
- 数据库进行：新建、修改

### 2.1、ModelForm的行为与属性

`ModelForm` 是 Django 中的一个表单类，用于将模型实例映射到表单上。它继承自 Django 的 `forms.ModelForm`，并提供了与模型实例交互的便捷方法。以下是 `ModelForm` 的一些主要行为和属性：

- 行为

1. **验证数据（Validation）**：
   - `ModelForm` 会根据模型定义的字段及其验证规则来验证输入的数据。
   - 可以通过调用 `is_valid()` 方法来验证表单数据。
2. **保存数据（Save Data）**：
   - 调用 `save()` 方法可以将表单数据保存到数据库中，对应的模型实例也会随之更新或创建。
   - 可以通过 `commit=False` 参数获取一个未保存的模型实例，然后对其进行额外处理。
3. **实例化表单（Form Instantiation）**：
   - 可以通过提供 `instance` 参数来使用现有的模型实例填充表单。
   - 可以通过 `initial` 参数来设置表单字段的初始值。
4. **处理文件上传（Handle File Uploads）**：
   - `ModelForm` 支持文件字段，可以处理文件上传并自动保存到指定的目录中。

-  属性

1. **Meta**：
   - `Meta` 类用于定义与表单相关的元数据。
   - 主要属性包括：
     - `model`：指定与表单关联的模型。
     - `fields`：指定要包含在表单中的模型字段。
     - `exclude`：指定要从表单中排除的模型字段。
     - `widgets`：自定义表单字段的显示小部件。
2. **fields**：
   - 一个包含表单字段的字典，键是字段名，值是字段实例。
3. **cleaned_data**：
   - 包含表单中验证后的数据的字典，仅在调用 `is_valid()` 方法后可用。
4. **errors**：
   - 包含表单验证错误信息的字典。
5. **instance**：
   - 当前表单对应的模型实例，通常在表单保存时使用。
6. **initial**：
   - 包含表单字段初始值的字典。

如果想要用这个组件，需要一下步骤：

- 创建类

  ```python
  class AssetModelForm(forms.ModelForm):
      class Meta:
          # 会看创建表中字段的语句
          model = models.AssetSet
          # fileds = ['name','price','category','depart'] #展示想要显示的字段
          fields = '__all__'
          # 加入css样式，使其更美观
          # widgets = {
          #     'name':forms.Select(attrs={'class':"form-control"}),
          #     'price':forms.Select(attrs={'class':"form-control"}),
          #     'category':forms.Select(attrs={'class':"form-control"}),
          #     'depart':forms.Select(attrs={'class':"form-control"}),
          # }
  
      # 上面这种方法太麻烦，还需要一个个写，下面是其简便方法
      def __init__(self, *args, **kwargs):  # 定义 __init__ 初始化方法，重载 ModelForm 的构造函数。
          super().__init__(*args, **kwargs) # 调用父类的 __init__ 方法，初始化表单
          for name, field in self.fields.items(): # 遍历表单中的每个字段
              field.widget.attrs['class'] = "form-control" # 为每个字段的widget添加 class="form-control" 属性，使其应用Bootstrap的样式。
  ```

  **`class AssetModelForm(forms.ModelForm):`**: 定义一个名为 `AssetModelForm` 的表单类，继承自Django的 `ModelForm`。

  **`class Meta:`**: 定义 `Meta` 子类，提供表单的元数据。

  **`model = models.AssetSet`**: 指定该表单对应的模型类是 `AssetSet`。

  **`fields = '__all__'`**: 指定表单应包含模型中的所有字段。

- ‘视图函数

```python
def asset_add(request):
    form = AssetModelForm
    return render(request,'assetadd.html',{"form":form})
```

这里的 `form` 是 `AssetModelForm` 的一个实例。`AssetModelForm` 继承自 `django.forms.ModelForm`，所以 `form` 的类型是 `AssetModelForm`，这是一个 Django 的 `ModelForm` 对象。

#### 主要属性和方法

- **`form.fields`**: 包含表单中的所有字段，是一个字典，键是字段名称，值是字段对象。
- **`form.is_valid()`**: 检查表单提交的数据是否符合模型字段的要求。
- **`form.cleaned_data`**: 在表单验证通过后，包含表单的干净数据。
- **`form.errors`**: 如果表单无效，包含表单的错误信息。
- **`form.save()`**: 在表单有效的情况下，将表单数据保存到数据库中。

- HTML页面上

  ```html
   <form action="">
       {% for filed in form %}
       {{ filed }}
       {% endfor %}
  
    </form>
  ```

- 这样展示外键下拉框会显示主表的对象——需要在主表中修改一下

![image-20240702215543525](C:/Users/user/AppData/Roaming/Typora/typora-user-images/image-20240702215543525.png)

## 7.5、编辑资产

![image-20240704202457350](C:/Users/user/AppData/Roaming/Typora/typora-user-images/image-20240704202457350.png)

![image-20240704202653273](C:/Users/user/AppData/Roaming/Typora/typora-user-images/image-20240704202653273.png)

## 7.6、删除资产

- 通过URL传参

```pyt
http://127.0.0.1:8000/asset/edit/?aid=3
```

- url.py

```python
urlpatterns = [
    path('asset/delete/',views.asset_delete),
]
```

- views.py

```python
def asset_delete(request):
    did = request.GET.get('did')
    models.AssetSet.objects.filter(id=did).delete()
    return redirect('/asset/list/')
```

- 另一种URL传参数

  - url.py

  ```python
  urlpatterns = [
      path('asset/<int:aid>/delete/',views.asset_delete),
  ]
  ```

  - URL

  ```PYTHON
  http://127.0.0.1:8000/asset/111/edit/
  <a href="/asset/{{ obj.id }}/edit/"  class="btn btn-primary">编辑</a>
  ```

  - views.py

  ```python
  def asset_delete(request,aid):
      
      pass
  ```

# 8、员工管理(案例)

## 8.1、表结构

字段有：id , name,mobile,email,gender,depart_id
