# 前端开发

```
目的：开发一个平台（网站）
	- 前端开发：HTML,CSS,JavaScript，JQuery,BootStrap
	- Mysql数据库
	- Web框架：接收请求并处理
	- Mysql数据库： 存储数据地方
快速上手：
	基于Flask Web框架快速搭建一个网站出来。
深入学习：
	基于Django框架（主要）
```

原理：

<img src="D:\Photo\QQ图片20231225204651.jpg" style="zoom:33%;" />

## 1.Flask项目的创建

- 创建一个Flask项目流程

- ```python
  #__name__:代表app.py这个模块
  #1.以后出现bug，它可以帮助我们快速定位
  #2.寻找模板文件，有一个相对路径
  app = Flask(__name__)
  
  #创建一个路由和视图函数的映射
  
  @app.route('/') #定义一个路由装饰器
  def hello_world():
      return "hello 中国!"
  
  if __name__ == '__main__':
      app.run()
  ```

## 2.项目配置

​	Flask项目不管是在开发中，还是部署上线到服务器上，都需要做一些配置。比如是否开启Debug模式，连接数据库参数信息等，都需要配置才能实现。本章讲解Flask项目中的几种配置方法。

### 2.1Debug模式，Host,Port配置

​	在 Flask 中，你可以通过配置来设置 Debug 模式、主机和端口。这些配置可以在创建 Flask 应用实例时或者在应用运行前进行设置。

**Debug 模式：**

在开发过程中，Debug 模式非常有用，它可以帮助你找到和解决应用程序中的错误。在 Flask 中，你可以通过将 `debug` 参数设置为 `True` 来启用 Debug 模式：

```python
python
app = Flask(__name__)
app.config['DEBUG'] = True
```

**Host 和 Port 配置：**

你也可以指定 Flask 应用运行的主机和端口。默认情况下，Flask 应用运行在 `127.0.0.1:5000`。你可以通过设置 `host` 和 `port` 参数来修改这些值：

```python
python
app.run(host='0.0.0.0', port=8080)
```

在上述代码中，`host='0.0.0.0'` 表示允许来自任何 IP 地址的请求访问你的应用程序，`port=8080` 表示应用程序运行在 8080 端口上。

​	在生产环境中，避免使用 `app.run()` 启动 Flask 应用程序。通常会使用像 Gunicorn、uWSGI 或者部署到类似 Heroku、AWS 等平台上的服务来运行 Flask 应用程序，因为它们提供更强大的性能和稳定性。在生产环境中，应该使用环境变量或配置文件来管理这些参数。

# 1.快速开发网站’

<img src="D:\Photo\QQ图片20240110173508.jpg" style="zoom:50%;" />

```python
from flask import Flask,render_template
from datetime import datetime

app = Flask(__name__)
@app.route("/union/xxx")

def index():
    #从数据库获取数据
    text = "中国北京联通分公司"
    date_string = datetime.now().strftime("%Y-%m-%d,%H:%M:%S")
    #return "中国联通<h1 style='color:red;' onclick='alert(123)'>江西分公司</h1><a href='#'>青海公司</a>"
    return render_template('index.html',n1=text,n2=date_string)
if __name__ == '__main__':
    app.run()
```

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
中国联通
<h1 style='color:red;' onclick='alert(123)'>江西分公司</h1>
<a href='#'>青海公司</a>
本年度最优秀的团队:{{n1}}
当前时间是:{{n2}}

</body>
</html>
```

<img src="C:\Users\战神\AppData\Roaming\Typora\typora-user-images\image-20240110173127636.png" alt="image-20240110173127636" style="zoom:50%;" />

<img src="C:\Users\战神\AppData\Roaming\Typora\typora-user-images\image-20240110173237333.png" alt="image-20240110173237333" style="zoom:50%;" />

# 2.前端开发

- HTML, 骨架
- CSS,点缀
- JavaScript, 动起来。

```python
jQuery,第三方的模块，很简单的实现动态的效果。
BootStrap,提供了CSS+JavaScript--->80%的功能+20%
```

# 3.HTML

HTML，超文本标记语言。浏览器能识别的标签。

```html
<html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Title</title>
    </head>
    <body>
		能看到的都要写在这里
    </body>
</html>
```

## 3.1 编码

```html
<meta charset="UTF-8">
```

## 3.2 title

```html
<title>江西联通</title>
#网页头部标签
```

<img src="C:\Users\战神\AppData\Roaming\Typora\typora-user-images\image-20240110174819977.png" alt="image-20240110174819977" style="zoom:50%;" />

## 3.3 标题

```HTML
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>江西联通</title>
</head>
<body>
<h1>中国</h1>
<h2>上海</h2>
<h3>联通</h3>
</body>
</html>
```

## 3.4 div和span

素的标签。可塑造性极强。

- div,一个人占一整行【块级标签】

```html
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>江西联通</title>
</head>
<body>
<div>一个人</div>
<div>山东蓝翔</div>
</body>
</html>
```

- span标签，自己有多大，占多少【行内标签】

```HTML
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>江西联通</title>
</head>
<body>

<span>一个人</span>
<span>山东蓝翔</span>
<span>山东青鸟</span>

</body>
</html>
```

## 3.5 a标签

跳转页面在当前页面

```HTML
<a href="网址">点击查看详细</a>
<a href="https://3w.huanqiu.com/a/c36dc8/4G7JfZPEJQk?agt=128">点击查看详细</a>
href:跳转到的网址
```

```HTML
#新标签中打开
<a target="_blank" href="https://3w.huanqiu.com/a/c36dc8/4G7JfZPEJQk?agt=128">点击查看详细</a>
```

锚点：网址后面多了一个#,常见于小说章节

```html
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>江西联通</title>
</head>
<body>
    <a href="#i1"><div>第一章</div></a>
    <a href="#i2"><div>第二章</div></a>
    <a href="#i3"><div>第三章</div></a>
    <div id="i1" style="height:1000px;background-color:red;">
    <div>
        
    <div id="i2" style="height:1000px;background-color:blue;">
    </div>
        
    <div id="i3" style="height:1000px;background-color:green;">  
    </div>
</body>
</html>
```

## 3.6 img图片

```HTML
<img src="图片地址" />
```

```HTML
引入别人的网站图片
<img src="https://imgcps.jd.com/img-cubic/creative_server_cia_jdcloud/v2/2000366/10059918633362/FocusFullshop/CkNqZnMvdDEvMjI3NzUyLzI2LzEyMzk2LzU2MzMwLzY1OWM1NDZhRjQxNjZlODU1Lzg1NWU4NGU2YjlkMWM4YjYucG5nEgk0LXR5XzBfNTUwAjjui3pCEwoP5qix6Iqx5rK554Of5py6EAFCDQoJ5ruhMTDlh48yEAJCEAoM56uL5Y2z5oqi6LStEAZCBwoD5oqiEAdYktOBj-SkAg/cr/s/q.jpg"/>
```

```html
引入自己的图片
 - 在flask项目目录下创建static文件夹，将图片拷贝到static文件夹下
 - 在HTML中引入自己的图片
 - <img src="/static/图片名称"/>
两种设置图片的比例
-方法一
<img style="height:100px;width:100px" src="/static/批注 2020-01-01 104000.png"/>
-方法二
<body>
    <div style="height=100px;width:200px">
        <img style="width:50%" src="https://imgcps.jd.com/img-EAZCBwoD5oqiEAdYktOBj-SkAg/cr/s/q.jpg"/>
    </div>
    <img style="height:100px;width:100px" src="/static/批注 2020-01-01 104000.png"/>

</body>
</html>
```

## 小结

```html
h1
div
span
a
img
```

- 布局

```html
<div>
    <div><img /></div>
    <span></span>
</div>
```

- 嵌套

点击图片能进行跳转

```HTML
<a herf="xxx">
	<img src="xxx" />
</a>
```

- 块级标签和行内标签

  ```python
  -块级标签
  	h1
      <div></div>
  -行内标签
  	<span></span>
      <a></a>
      <img />
  ```

  

## 练习题：博客列表

<img src="C:\Users\战神\AppData\Roaming\Typora\typora-user-images\image-20240112164229104.png" alt="image-20240112164229104" style="zoom:50%;" />

```HTML
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>江西联通</title>
</head>
<body>
    <div>
        <div><a href="https://www.cnblogs.com/ComputerTech/p/17958081"><h4>String类和STL</h4></a></div>
        <div>
            <a href="https://www.cnblogs.com/ComputerTech/"><img 			src="/static/dangqian.png" /></a>
            <span>目录一. string 类1. 构造字符串2. string类输入3. 使用字符串4. </span>
        </div>
        <div>
            <span><a href="https://www.cnblogs.com/ComputerTech/">ComputerTech</a>				</span>
            <span>{{n2}}</span>
        </div>

    </div>

</body>
</html>
```

实现效果

<img src="C:\Users\战神\AppData\Roaming\Typora\typora-user-images\image-20240112170153534.png" alt="image-20240112170153534" style="zoom:50%;" />

## 3.7 列表

```html
<Ul>
    <li>打发斯蒂芬</li>
</Ul>
```

程序

```HTML
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>江西联通</title>
</head>
<body>
    <h3>三大运营商</h3>
    <ul>
        <li>中国联通</li>
        <li>中国电信</li>
        <li>中国移动</li>
    </ul>
    <h3>一线城市</h3>
    <ol>
        <li>北京</li>
        <li>上海</li>
        <li>深圳</li>
    </ol>
</body>
</html>
```

效果：

<img src="C:\Users\战神\AppData\Roaming\Typora\typora-user-images\image-20240112170926058.png" alt="image-20240112170926058" style="zoom:50%;" />

## 3.8 表格

```HTML
<table>
    <thead>
    	<tr>  <th>ID</th> <th>姓名</th> <th>年龄</th> </tr>
    </thead>
    <tbody>
    	<tr>  <td>1</td> <td>许磊</td> <td>19</td>    </tr>
    </tbody>
</table>
```

程序

```HTML
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>江西联通</title>
</head>
<body>
   <table border="1">
    <thead>
    	<tr>  <th>ID</th> <th>姓名</th> <th>年龄</th> </tr> #加粗
    </thead>
    <tbody>
    	<tr>  <td>1</td> <td>许磊</td> <td>19</td>    </tr>
        <tr>  <td>2</td> <td>王四</td> <td>22</td>    </tr>
        <tr>  <td>3</td> <td>王四</td> <td>22</td>    </tr>
    </tbody>
    </table>
</body>
</html>
```

效果：

<img src="C:\Users\战神\AppData\Roaming\Typora\typora-user-images\image-20240112171729877.png" alt="image-20240112171729877" style="zoom:50%;" />

## HTML知识点回顾

- HTML知识

```
div
span
h系列
a
img
ul/li ol/li
table tr/td
input 
	text
	password
	file
	radio
	checkbox
	button
	submit
select/option
textarea
form
```

- flask框架

```
GET方式发送数据
	request.args
	
POST方式发送数据
	request.form

```

```
return "xxxx"
return render_template("xxx.html")

return redirect("网址")
```

- 打开和展示HTML
  - 基于WEB框架【项目开发】
  - 基于本地文件
  - pycharm右上角【学习】

## 内容回顾

- 知识点分类

  - 前端开发
  - Mysql数据库
  - Flask框架、django框架

- 前端

  - html

    - ```html
      h1,h2....h6-->标题【块级】
      div 【块级】
      span
      a,超链接和锚点 <a href=""></a>
      img,图片  <img src=""/>
      列表标签【块级标签】
      	<ul>
              <li>111</li>
              <li>222</li>
      	</ul>
      	<ol>
              <li>111</li>
              <li>222</li>
      	</ol>
      表格
      	<table>
              <th></th>
              <td> </td>
      	</table>
      input系列 <input type='text' />
      	text
      	password
      	file
      	radio
      	checkbox
      	button
      	submit
      下拉框
      	<select>
              <option value>xxxxx</option>
      	</select>
      多行文本框
      	<textarea>评论</textarea>
      
      表单
      	(网络搜索)
      	<form action="提交的地址" method="get">
              <input type="text" name="mobile" />
              #单选
              <input type='radio' name='gender' value="11" />
              <input type='radio' name='gender' value="12" />
              
          	<input type='submit' value="提交" />    
      	</form>
      ```

  - css

  - JavaScript-->js

  - jQuery,BootStrap

- flask框架

  - 写网站

    - ```python
      app = Flask(__name__)
      
      @app.route("/xxxx")
      
      def index():
          pass
      
      if __name__ == "__main__":
          app.run()
      ```

  - 返回HTML

    - ```html
      <html>
          <head>
              
          </head>
          <body>
              <h1>
                  欢迎使用
                  ....
              </h1>
          </body>
      </html>
      ```

      

    - ```python
      app = Flask(__name__)
      
      @app.route("/xxxx")
      
      def index():
          return render_template("xxx.html") #templates目录中找xxx.html文件
      
      if __name__ == "__main__":
          app.run()
      ```

    - HTML+“占位符=模板语言”=>渲染(替换)

    ```html
    <html>
        <head>
            
        </head>
        <body>
            <h1>
                欢迎使用
            </h1>
            <span>{{info}}</span>
        </body>
    </html>
    ```

    ```python
    app = Flask(__name__)
    
    @app.route("/xxxx")
    
    def index():
        #1.去templates目录中找xxx.html文件
        #2.渲染=替换
        #3.得到替换之后的结果，再将结果返回给用户浏览器
        return render_template("xxx.html",info="哈哈哈哈") #
    
    if __name__ == "__main__":
        app.run()
    ```

    - 获取不同方式的请求数据

      - 以get方式传入参数

      ```python
      from falsk import Flask,request
      
      app = Flask(__name__)
      @app.route("/xxxx",method=["GET"])
      
      # 请求是以GET方法传入的参数
      # 提交的网址？mobile=手机号&pwd=密码
      
      def index():
          m = request.args.get('mobile')
          p = request.args.get("pwd")
          ...
      
      if __name__ == "__main__":
          app.run()
      ```

      ```python
      from falsk import Flask,request
      
      app = Flask(__name__)
      @app.route("/xxxx",method=["POST"])
      
      # 请求是以POST方法传入的参数
      # 提交的网址？
      # mobile=手机号&pwd=密码
      
      def index():
          m = request.form.get('mobile')
          p = request.form.get("pwd")
          ...
      
      if __name__ == "__main__":
          app.run()
      ```

    - 关于Flask的返回值

      - ```
        -返回字符串 return "xxx"
        -返回HTML  return render_template("xxx.html",info="哈哈哈哈")
        -返回网址   return redirect("http://www.xxx.com")
        ```

      ```python
      from falsk import Flask,request
      
      app = Flask(__name__)
      @app.route("/xxxx",method=["GET"])
      
      
      def index():
          ...
          #return "xxx" #返回一个字符串
      	#return render_template("xxx.html",info="哈哈哈哈")
          return redirect("http://www.xxx.com")
      
      if __name__ == "__main__":
          app.run()
      ```

## 知识点复习

### 常见基础语法

- 输入和输出

```python
print
v1 = input("<<<")
```

- 变量

```python
变量命名规则
- 字母，数字，下划线
- 不能以数字开头
- 不能使用python内置关键字
	def/class    
```

- 条件语句

```python
if 值:
    pass
else:
    pass
#哪些转换成布尔值Flase
#None、0、空字符串、空列表、空字典、空元组、空集合
#         ""      []      {}    ()    set()
#          str() list() dict() tuple() 
```

- 循环语句

```python
while
for
```

```python
break  #退出循环
continue #结束本次循环，开始下次循环
```

```python
while True:
    print(123)
    break
```

- 注释

```python
#...       单行注释
"""3333""" 多行注释
```

- pass

```python
if True:
    pass 
```

- 字符串格式化

```python
v1 = "我是{}xxx".format("联通")
print(v1)
```

```python
v1 = "我是{0}xxx".format("联通")
print(v1)
```

```python
v1 = "我是{n1}xxx".format(n1="联通")
print(v1)
```

### 数据类型

- None

- 整型

- 布尔类型

- 字符串

  ```python
  v1="123"
  v2="999"
  注意：字符串相加就是拼接
  ```

  ```python
  #字符串中的方法
  class str():
      def upper(self,...):
          pass
  ```

  ```python
  upper/lower/strip/split/join/replace
  ```

  ```python
  字符串是不可变类型
  v1 = "root"
  new = v1.upper()
  print(new) #ROOT
  ```

  ```python
  V1 = ["中国","上海","联通"]
  data = "*".join(v1)
  print(data) #中国*上海*联通
  print(v1)
  #注意：想要使用join的话，列表内部元素必须是字符串。v1 = [11,22,33]不可join
  ```

  ```python
  可哈希类型，可以作为字典的键
  info = {
      "name":"许磊"
  }
  ```

```python
公共方法
len
切片
索引
for
in
```

- 列表

```python
v1 = [11,22,33]
```

```python
class list:
    def insert(self,...):
        pass
    
    def append(self,...):
        pass
```

```python
append/insert/remove/reverse
```

```python
可变类型
v1 = [11,22,33]
v1.insert(0,123)
print(v1)#[123, 11, 22, 33]

v1 = [11,22,33]
v1.append(56)
print(v1) #[11, 22, 33, 56]

v1 = [11,22,33]
v1.remove(22)
print(v1) #[11, 33]

v1 = [11,22,33]
v1.reserve()
print(v1) #[33, 22, 11]
```

```python
不可哈希类型，不能作为字典的键
```

公共方法

```python
公共方法
len
切片
索引
for
in #判断某个元素是否在里面
```

- 元组

```python
v1 = (11,22,33,44)
```

```python
v1 = (11,) #元组只有一个元素要加,
```

```python
不可变类型
```

```python
公共方法
len
切片
索引
for
in #判断某个元素是否在里面
```

```python
可哈希，可以作为字典的键，但是不能嵌套不可哈希的值
```



- 字典

```python
info = {"键":"值"}
```

```python
class dict:
    def get(self,...):
        pass
    def key(self,...):
        pass
```

```python
可变类型
get/keys/items/values
```

```python
不可哈希类型
```

```python
公共方法
len
切片
索引
for
in #判断某个元素是否在里面
```

- 推导式

```python
v1 = {i for i in range(5)} #range前取后不取
```



### 函数

- 定义函数

```python
def xxx():
    pass
xxx()
```

- 参数

```python
def xxx(v1,v2):
    pass
xxx(11,22)       #位置传参
xxx(v1=11,v2=22) #关键字传参
```

```python
def xxx(v1,v2=99):
    pass
```

```python
def xxx(*args): #*args:只能接受位置传参的参数,将所有的位置传参变成一个元组
    pass
def xxx(**kwargs): #**kwargs:只能接受关键字传参的参数,kwargs将所有的关键字参数变为一个字典
    pass
```

```python
def xxx(*args,**kwargs):
    print(args)  args=(12, 1224, 124, 456)
    print(kwargs) kwargs = {'k': 123}

xxx(12,1224,124,456,k=123)
#(12, 1224, 124, 456)
#{'k': 123}
```

- 返回值

```python
函数没写返回值，默认返回:None
函数中出现return,立即终止函数
```

- 匿名函数

```python
v1 = lambda x:x+100

res = v1(123)
print(res) #223
```

- 内置函数

```python
分组的函数，快速过一遍
```

```python
排序
```

### 模块

- 自定义模块

```python
自己代码划分到不同文件/文件夹中。
```

```python
sys.path
```

```python
import xxx #在sys.path提供的路径找xxx
```

注意：项目目录下不要写有与内置模块同名的文件

- 内置模块

```python
random
hashlib
time/datatime
json
os
	os.path.join
    os.listdir/os.walk
sys
re 
	- 正则
    	\d \w
        ? + *{8}
        \d+ \d+?
        分组()
    - re模块
    	re.findall
        re.match
        re.search
        re.split
shutil
```

- 第三方模块

```python
pip install 模块名
```

```python
requests
bs4
openpyxl
python-docx
```

### 面向对象

- 三大特性

  ```python
  封装，继承，多态
  ```

- 类，对象，self

- 成员

  - ```python
    实例变量，类变量
    绑定方法，静态方法，类方法
    属性
    ```

- 特殊成员

  - ```python
    __new__
    __init__
    __call__
    __dict__
    ```

### 并发编程

- 进程，厂房
- 线程，员工
- 协程，“微线程”不是真实存在的
