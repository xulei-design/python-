# CSS

css,层叠样式表，美化页面。

- 核心CSS样式，听懂&看懂&改
- 别的框架+CSS样式编程。

```html
<h1 style="color:red;height:300px">中国联通</h1>
<img src="xxx" />
```

- 以前
- <img src="C:\Users\战神\AppData\Roaming\Typora\typora-user-images\image-20240118211923911.png" alt="image-20240118211923911" style="zoom:50%;" />

```python
from flask import Flask,render_template

app = Flask(__name__)

@app.route("/home")
def home():
    return render_template("home.html")

if __name__ == "__main__":
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
    <h1 style="color:red;height:300px">中国联通</h1>
</body>
</html>
```

- 接下来为了开发和学习方便，直接在浏览器上打开编写的HTML+CSS

<img src="C:\Users\战神\AppData\Roaming\Typora\typora-user-images\image-20240118212218027.png" alt="image-20240118212218027" style="zoom:50%;" />

![image-20240118212336640](C:\Users\战神\AppData\Roaming\Typora\typora-user-images\image-20240118212336640.png)

接下来，不在将页面嵌套到flask程序中

## 1.css应用位置

#### 1. 在标签上

```python
<div style="background-color:rebeccapurple;color: green">大多数法</div>
```

#### 2. 在head的style中定义，在当前页面中可以被复用

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <style>
        .xxx{
            background-color: pink;
            color: green;
        }
    </style>
</head>
<body>
    <div class="xxx">大多数法</div>
    <div class="xxx">大多数法</div>
    <div class="xxx">大多数法</div>
</body>
</html>
```

#### 3. 定义在一个CSS文件中，一个样式被多个HTML文件使用，多页面都使用同一个CSS样式

- <img src="C:\Users\战神\AppData\Roaming\Typora\typora-user-images\image-20240119094733091.png" alt="image-20240119094733091" style="zoom:50%;" />

```css
 .xxx{
            background-color: pink;
            color: green;
        }
```

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <link rel="stylesheet" href="utils.css"/> #快捷键：写上link，按Tab键会自动补齐
</head>
<body>
    <div class="xxx">大多数法</div>
    <div class="xxx">大多数法</div>
    <div class="xxx">大多数法</div>
</body>
</html>
```

<img src="C:\Users\战神\AppData\Roaming\Typora\typora-user-images\image-20240119095158353.png" alt="image-20240119095158353" style="zoom:50%;" />

## 2.选择器

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <style>
        .xxx{
            background-color: pink;
            color: green;
        }
        #m1{
            height: 100px;
        }
    </style>
</head>
<body>
    <div class="xxx">大多数法</div> .与class相对应
    <div id="m1"></div>            #与id相对应
</body>
</html>
```

### 1. ID选择器

```html
#m1{
	height:100px;
}
<div id='m1'></div>
```

id在html中一般都是唯一的。

### 2.class选择器（最多）

```html
.xxx{
            background-color: pink;
            color: green;
        }
<div class="xxx">大多数法</div>
```

### 3.标签选择器

```HTML
a{
	color:red;
}
#所有的a标签都是这个样式，字体是红色的

<div>sdf</div>
<div>
    <a>阿斯提夫</a>
</div>
<div>sdf</div>
<a>sdga</a>
<a>afag</a>
<span>ajg</span>
<span>5846464</span>
```

### 4.后代选择器

```css
.yy li{
    color:pink;
}
#去yy找到li标签的字体全为粉色
.yy > a{
    color:red;
}#去yy找它儿子中标签为a标签的
.yy > div a{
    color:bule;
}
```

总结：空格去子子孙孙中找，>去儿子中找

```html
<div class="yy">
    <a>百度</a>
    <div>
        <a>谷歌</a>
    </div>
    <ul>
        <li>美国</li>
        <li>日本</li>
        <li>韩国</li>
    </ul>
</div>
```

### 5.属性选择器

```css
input[type='password']{

}
.v1[xxx='456']{

}
```



```html
<input type="text">
<input type="password">

<div class="v1" xx="123">s</div>
<div class="v1" xx="456">f</div>
<div class="v1" xx="999">m</div>
```

### 6.应用多个样式

```HTML
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <style>
        .c1{
            background-color: pink;
            color: green;
        }
        .c2{
            height: 100px;
            color:red;
        }
    </style>
</head>
<body>
    <div class="c1 c2">大多数法</div> .与class相对应
   
</body>
</html>
```

 #最终应用c2样式中的颜色覆盖了c1样式中的颜色。总样式是background-color: pink;height: 100px;color:red;

```HTML
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <style>
        .c1{
            background-color: pink;
            color: green !important;
        }
        .c2{
            height: 100px;
            color:red;
        }
    </style>
</head>
<body>
    <div class="c1 c2">大多数法</div> .与class相对应
   
</body>
</html>
```

#如果不想让下面的样式覆盖某一样式，在后面加`!impotant`

## 3.样式

### 1.高度和宽度

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
  <div style="height: 100px;width: 200px;background-color: pink"></div>
  <div style="height: 100px;width: 200px;background-color: green"></div>
  <span style="height: 100px;width: 200px;background-color: pink">中国</span>
</body>
</html>
```

- 块级标签，生效(块级霸道，右边空白区域会占据)
- 行内标签，无效

- 可以使用百分比

```HTML
-百分比的宽度，一定根据他的父亲。
-百分比的高度，固定的父亲高度才可以设置。
<body>
  <div style="height: 100px;width: 20%;background-color: pink">ahg</div>
  <div style="width: 500px;height: 100px;border: 1px solid red;">
    <div style="width: 50%;height: 80%; background-color: rebeccapurple">544</div>
  </div>

</body>
```

### 2.块级or行内

- display:inline;
- display:block;
- display:inline-block;

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
  <div style="background-color: pink;display: inline">中国联通</div> #块级标签变行内标签
  <span style="background-color: red">江西联通</span>
  <a style="background-color: aquamarine;display: block">百度</a>#行内标签变块级
</body>
</html>
```

```html
<body>
  <div style="display: inline-block;background-color: red;width: 500px">中国</div>
  <div style="display: inline-block;background-color: green;height: 120px">河南</div>
  <div style="display: inline-block;background-color: blue">驻马店</div>
</body>
```

点击跳转的菜单

<img src="C:\Users\战神\AppData\Roaming\Typora\typora-user-images\image-20240119110323644.png" alt="image-20240119110323644" style="zoom:50%;" />

```HTML
<body>
  <div style="border: 1px solid red;height: 500px;width: 180px">
    <a href="http://baidu.com" style="display: block;background-color: pink">订单管理</a>
    <a href="http://baidu.com"style="display: block;background-color: red">员工管理</a>
    <a href="http://baidu.com"style="display: block;background-color: green;">财务管理</a>
  </div>
</body>
```

### 3.字体设置

- 颜色
- 大小
- 加粗
- 字体格式

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <style>
      .xx{
        color:red;
        font-size: 30px;
        font-weight: 100;
        font-family: "Adobe 宋体 Std L";
      }
    </style>
</head>
<body>
  <div class="xx">江西联通</div>
</body>
</html>
```

## 4.CSS常见样式

#### 1.文字对齐方式

- 水平方向的对齐

```html
<h2 style="text-align:center">
    用户注册
</h2>
```

```html
<div style="width: 500px;border: 1px solid red;">
  <h2 style="text-align: center">用户注册</h2>
  <div>
    用户名：<input type="text" />
  </div>
</div>
```

- 垂直方向

  ```html
  <head>
      <meta charset="UTF-8">
      <title>Title</title>
      <style>
        .header{
          height: 48px;
          line-height: 48px;
          background-color: black;
        }
        .header >a{
          color: white;
        }
      </style>
  </head>
  <body>
  <div class="header">
    <a>小米手环</a>
    <a>小米手机</a>
    <a>小米电视</a>
  </div>
  </body>
  </html>
  ```

  <img src="C:\Users\战神\AppData\Roaming\Typora\typora-user-images\image-20240122110620614.png" alt="image-20240122110620614" style="zoom:50%;" />

#### 2. 浮动

```HTML
 	<span style="float: left">联通</span>
    <span style="float: right">移动</span>
```

<img src="C:\Users\战神\AppData\Roaming\Typora\typora-user-images\image-20240122111132206.png" alt="image-20240122111132206" style="zoom:50%;" />

- div块级标签(霸道)，浮动起来，不再霸道。

  ```html
  <div>
     <div style="float: left">联通</div>
     <div style="float: left">移动</div>
  </div>
  ```

  ![image-20240122111458864](C:\Users\战神\AppData\Roaming\Typora\typora-user-images\image-20240122111458864.png)

```html

<style>
    .item{
        float: left;
        height: 500px;
        width: 280px;
        border: 1px solid #dddd;
    }
</style>

<body>
  <div>
   <div class="item">联通</div>
   <div class="item">移动</div>
   <div class="item">移动</div>
   <div class="item">移动</div>
   <div class="item">移动</div>
  </div>
</body>
```

效果：

<img src="C:\Users\战神\AppData\Roaming\Typora\typora-user-images\image-20240122112029453.png" alt="image-20240122112029453" style="zoom:50%;" />

如果你让标签浮动起来，会脱离文档流(父亲管不住)。

```html
<div style="color: red;width: 500px;background-color: pink">
    <div>青海</div>
    <div style="height: 200px">甘薯</div>
</div>
<div>丽华</div> #儿子会将父亲的高度撑起来
```

```html
<body>
  <div style="color: red;background-color: pink">
    <div style="float: left">青海</div>
    <div style="height: 200px;float: right">甘薯</div>
  </div>
  <div style="clear: both;"></div>#解决的方案
  <div>丽华</div>
</body>
```

#### 3、内边距

脂肪厚了

```html
<style>
    .c1{
        width: 500px;
        height: 100px;
        border: 1px solid red;
        padding: 50px;
        padding-left:20px;#设置内边距
    }
</style>

<body>
  <div class="c1">我是一个粉刷匠</div>
</body>
```

#### 4、外边距

```
margin:10px;

margin-right:10px;
margin-top:10px;
```

```html
<style>
      .item{
          height: 200px;
          width: 100px;
          float: left;
          border: 2px solid red;
          margin-right: 10px;
          margin-bottom: 20px;
      }
</style>
<body>
<div>
    <div class="item">我是一个粉刷匠</div>
    <div class="item">我是一个粉刷匠</div>
    <div class="item">我是一个粉刷匠</div>
    <div class="item">我是一个粉刷匠</div>
    <div class="item">我是一个粉刷匠</div>
    <div class="item">我是一个粉刷匠</div>
</div>
```

##### 4.1、外边距的应用场景（对话窗口）

- 内容居中，整体内容居中显示,页面布局

  ```html
  <style>
        .content{
          height: 500px;
          width: 300px;
          margin-left: auto;
          margin-right: auto;#居中设置
          background-color: pink;
        }
  </style>
  
  <body>
    <div class="content"></div>
  </body>
  ```

- 居中窗体，用于登录页面显示

```HTML
<style>
    .box{
        height: 400px;
        width: 450px;
        border: 2px solid pink;
        margin-left: auto;
        margin-right: auto;
        background-color: white;
    }
</style>
<body>
  <div class="box"></div>
</body>
```

- 每个页面都需要设置的
- 将默认外边距设置为0

```html
<body style="margin: 0;">
  <div style="height: 500px;background-color: pink"></div>
</body>
```

#### 5.hover 伪类

鼠标放上才会用hover伪类中的样式

```html
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <style>
      span{
        color: red;
      }
      span:hover{
        color: green;
      }
    </style>
</head>
<body>
  <span>中国联通</span>
</body>
```

#### 6.after伪类

```html
<style>
li{
color: red;
}
li:after{
content: "大美女";
}
</style>

<body>
  <ul>
    <li>刘兰</li>
    <li>张三</li>
  </ul>
</body>
```

效果：

![image-20240123103451928](C:\Users\战神\AppData\Roaming\Typora\typora-user-images\image-20240123103451928.png)

##### 6.1、应用场景

- 使用after伪类**清除浮动**

```html
<style>
    .con{
        background-color: green;
    }
    .clearfix:after{
        content: "";
        clear: both;
        display: block;
    }
    .con .item{
        width: 100px;
        height: 200px;
        border: 1px solid red;
        float: left;
    }
</style>

<div class="con clearfix">
    <div class="item"></div>
    <div class="item"></div>
    <div class="item"></div>
</div>
<div class="con clearfix">
    <div class="item"></div>
    <div class="item"></div>
    <div class="item"></div>
</div>
```

### 7.边框

```HTML
<style>
    .c1{
        height: 100px;
        width: 100px;
        border: 1px solid red; # 边框宽度：px solid:实线 边框颜色
    }
</style>
<body>
  <div class="c1"></div>
</body>
```

### 8.边框+菜单的应用

```html
<style>
    .menu-list{
        height: 800px;
        width: 200px;
        border: 1px solid #3333;
    }
    .menu-list a{
        display: block; #将行内标签变为块级标签
        padding: 8px;	#填充内边距
        border-bottom:1px solid black; #设置底边框
    }
    .menu-list a:hover{
        border-right: 3px solid red;
      }#鼠标选中就显示的样式
</style>
<div class="menu-list">
    <a>用户管理</a>
    <a>账户管理</a>
    <a>财务管理</a>
</div>
```

<img src="C:\Users\战神\AppData\Roaming\Typora\typora-user-images\image-20240123111816251.png" alt="image-20240123111816251" style="zoom:50%;" />



### 9.背景色

背景图

```html
<style>
    .c1{
        background-image: url("imags/科研步骤.jpg");
        background-position: -205px -111px;
        width: 302px;
        height: 103px;
    }
</style>
<body>
    <div class="c1"></div>
</body>
```

### 10.Postion

```
possition:fixed;

possition:relative;

possition:absolute;
```

#### 1.fixed

固定在窗口的某个位置。

```HTML
<style>
    body{
        margin: 0;
    }
    .to-top{
        position: fixed;
        right: 20px;
        bottom: 20px;
        height: 100px;
        width: 100px;
        background-color: pink;
    }
</style>

<body>
  <div style="height: 2000px;background-color: #b0b0b0">safag</div>
  <div class="to-top">返回顶部</div>
</body>
```

<img src="C:\Users\战神\AppData\Roaming\Typora\typora-user-images\image-20240123203807735.png" alt="image-20240123203807735" style="zoom:50%;" />

##### 1.1弹出框的制作

```HTML
<style>
      .bg{
        position: fixed;
        left: 0;
        bottom: 0;
        top: 0;
        right: 0;
        background-color: #333333;
        opacity: 0.8; # 透明度
        z-index: 1000; #在页面多层关系中使用
      }
      .diagloug{
          position: fixed;
          left: 0;
          right: 0;
          top: 150px;

          margin-left:auto ;
          margin-right: auto;
          width: 400px;
          height: 300px;
          background-color: white;
          z-index: 1001;# 和bg相比，在bg页面上层
      }
</style>
<body style="margin: 0">
  <div style="height: 3000px;background-color: pink;">中国联通</div>
  <div class="bg"></div>
    <div class="diagloug"></div>
</body>
```

<img src="C:\Users\战神\AppData\Roaming\Typora\typora-user-images\image-20240123210159566.png" alt="image-20240123210159566" style="zoom:50%;" />

#### 2.relative+absolute



## 练习题

写小米商城顶部菜单

<img src="C:\Users\战神\AppData\Roaming\Typora\typora-user-images\image-20240122195232066.png" alt="image-20240122195232066" style="zoom:50%;" />

#### 1. 思路

- body的外边距去掉
- 贯穿的div+背景色+高度+line-height
- 区域居中

```html
<div>
    <div style="width:1150px;margin-left:auto;margin-right:auto;">
       <div style="float:left"><a></a></div> 
    </div>
</div>
```

- 区域内部 左右float

```html
<style>
      .c1{
        height: 30px;
        background-color: black;
        line-height: 25px;
        color: white;
      }
</style>

<div class="c1">
    <div style="width:1000px;margin-left: auto;margin-right: auto">
        <div style="float: left"><a>小米官网</a></div>
        <div style="float: right"><a>Location</a></div>
        <div style="clear: both;"></div>
    </div>
</div>
```

完整实现的代码：

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>小米商城上端页面</title>
    <style>
        body{
            margin: 0;
        }
      .header{
        height: 40px;
        background-color: black;
        color: #b0b0b0;
        font-size: 12px;
        line-height: 40px; #居中显示
      }
      .header .container{
          width: 1226px;
          margin-left: auto;
          margin-right: auto;
      }
      .header .left{
          float: left;
      }
      .header .right{
          float: right;
      }
     .header .left .menu{
            padding-left: 25px;
            padding-right: 25px;
            display: inline-block;
            color: #b0b0b0; /* 改变a标签的字体颜色*/
            text-decoration: none; /*#去除a标签的下划线*/
             }
     .header .right .rmenu{
         padding-right: 25px;
         padding-left: 25px;
         display: inline-block;
     }
    </style>
</head>
<body>
  <div class="header">
    <div class="container">
        <div class="left">
            <a class="menu" style="padding-left: 0" href="https://www.mi.com/shop">小米官网</a>
            <a class="menu" href="https://www.mi.com/shop">小米商城</a>
            <a class="menu" href="https://www.mi.com/shop">小米澎湃OS</a>
            <a class="menu">小米汽车</a>
            <a class="menu">小米影像</a>
            <a class="menu">云服务</a>
            <a class="menu">loT</a>
            <a class="menu">有品</a>
            <a class="menu">小爱开放平台</a>
        </div>
        <div class="right">
            <a class="rmenu">登录</a>
            <a class="rmenu" style="padding-right: 0">注册</a>
        </div>
        <div style="clear: both;"></div>
    </div>
  </div>
</body>
</html>
```

<img src="C:\Users\战神\AppData\Roaming\Typora\typora-user-images\image-20240122211433637.png" alt="image-20240122211433637" style="zoom:50%;" />

## 5.BootStrap

是别人帮我们已经写好的CSS样式，如果想要使用BOOTStrap:

- 下载BootStrap
- 使用
  - 在页面上引入BootStrap
  - 在编写HTML时，按照BootStrap的规定来编写+自定制

### 1.初始BootStrap

[BootStrap网址](https://v3.bootcss.com/)

- 创建目录结构

<img src="C:\Users\战神\AppData\Roaming\Typora\typora-user-images\image-20240129155914719.png" alt="image-20240129155914719" style="zoom:50%;" />

- 引入CSS样式

```html
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <!--HTML注释:开发版本 -->
    <link rel="stylesheet" href="static/plugins/bootstrap-3.4.1/css/bootstrap.css">		</link>
    <!--生产版本 -->
    <!-- <link rel="stylesheet" href="static/plugins/bootstrap-						3.4.1/css/bootstrap.min.css"></link>-->
</head>
<body>
    #用自己的样式
    <input type="button" value="提交"> 
    #用css插件中的样式
    <input type="button" value="提交" class="btn-primary">
    <input type="button" value="提交" class="btn-success">
    <input type="button" value="提交" class="btn-danger">
    <input type="button" value="提交" class="btn-danger btn-xs">
</body>
```

<img src="C:\Users\战神\AppData\Roaming\Typora\typora-user-images\image-20240129160150289.png" alt="image-20240129160150289" style="zoom:50%;" />

### 2.导航

[导航地址](https://v3.bootcss.com/components/#navbar-buttons)

```html
<link rel="stylesheet" href="static/plugins/bootstrap-3.4.1/css/bootstrap.css">
<style>
    .navbar{
        border-radius: 0;
    }
</style>
<body>
<div class="navbar navbar-default">
    <div class="container-fluid">
        <!-- Brand and toggle get grouped for better mobile display -->
        <div class="navbar-header">
            <button type="button" class="navbar-toggle collapsed" data-toggle="collapse"
                    data-target="#bs-example-navbar-collapse-1" aria-expanded="false">
                <span class="sr-only">Toggle navigation</span>
                <span class="icon-bar">注册</span>
                <span class="icon-bar">登录</span>
                <span class="icon-bar">冻结</span>
            </button>
            <a class="navbar-brand" href="#">中国联通</a>
        </div>

        <!-- Collect the nav links, forms, and other content for toggling -->
        <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
            <ul class="nav navbar-nav">
                <li class="active"><a href="#">Link <span class="sr-only">(current)</span></a></li>
                <li><a href="#">广西</a></li>
                <li><a href="#">上海</a></li>
                <li><a href="#">北京</a></li>
                <li class="dropdown">
                    <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup="true"
                       aria-expanded="false"> <span class="caret">选择</span></a>
                    <ul class="dropdown-menu">
                        <li><a href="#">Action</a></li>
                        <li><a href="#">Another action</a></li>
                        <li><a href="#">Something else here</a></li>
                        <li role="separator" class="divider"></li>
                        <li><a href="#">Separated link</a></li>
                        <li role="separator" class="divider"></li>
                        <li><a href="#">One more separated link</a></li>
                    </ul>
                </li>
            </ul>
            <form class="navbar-form navbar-left">
                <div class="form-group">
                    <input type="text" class="form-control" placeholder="Search">
                </div>
                <button type="submit" class="btn btn-default">Submit</button>
            </form>
            <ul class="nav navbar-nav navbar-right">
                <li><a href="#">登录</a></li>
                <li class="dropdown">
                    <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup="true"
                       aria-expanded="false">注册 <span class="caret"></span></a>
                    <ul class="dropdown-menu">
                        <li><a href="www.baidu.com">Action</a></li>
                        <li><a href="#">Another action</a></li>
                        <li><a href="#">Something else here</a></li>
                        <li role="separator" class="divider"></li>
                        <li><a href="#">Separated link</a></li>
                    </ul>
                </li>
            </ul>
        </div><!-- /.navbar-collapse -->
    </div><!-- /.container-fluid -->
</div>
</body>
```

### 3.栅格系统

屏幕变小会根据屏幕大小自己调整

[栅格网址](https://v3.bootcss.com/css/#grid)

- 把整体划分为了12格

- 分类

  - 响应式布局

    - ```html
      col-lg-1
      col-md-1
      col-sm-1
      
      col-xs-1
      ```

      

  - 非响应式

### 4.container

容器居中

```html
<div>
    <div class="container">我是大好人</div>
</div>
```

```HTML
#内容平铺
<div>
	<div class="container-fluid">我是大好人</div>
</div>
```

### 5.clearfix

- 如果见到浮动（float），不能够撑起父类，加入class=“clearfix”
- 清除浮动

```html
<div style="background-color: #ff6700" class="clearfix">
    <div class="col-sm-2">许磊</div>
    <div class="col-sm-10">张三</div>
</div>
```

## 案例：用户登录

要求：

<img src="C:\Users\战神\AppData\Roaming\Tencent\QQ\Temp\f213f22709ec9d53e6ee9e55620b3b32.png" alt="f213f22709ec9d53e6ee9e55620b3b32" style="zoom:50%;" />

程序：

```HTML
<link rel="stylesheet" href="static/plugins/bootstrap-3.4.1/css/bootstrap.css">
<style>
    .box{
        width: 400px;
        height: 400px;
        margin-top: 50px;

        margin-right: auto; #区域居中
        margin-left: auto;
        border: solid #dddddd; #边框显示
        border-radius: 5px;#边框圆角处理

        padding-left: 30px; #里面内容内边距
        padding-right: 30px;
        padding-bottom: 30px;

        box-shadow: 10px 10px 10px rgb(0 0 0 / 5%);#阴影效果，更显立体，前面两个太阳上照
    }
    .box h2{
        text-align: center; #边框中的文字居中显示
        padding-bottom: 20px;#文字内边距显示
    }
</style>

<div class="box">
    <h2>用户登录</h2>
    <form>
        <div class="form-group">
            <label for="user">用户名或手机号</label>
            <input type="text" class="form-control" id="user" placeholder="用户名或手机号">
        </div>
        #for="user"与id="user"将标签与输入框联系在一起。type：输入的类型。placeholder：输入框中提示输入的内容。
        <div class="form-group">
            <label for="pwd">密码</label>
            <input type="password" class="form-control" id="pwd" placeholder="输入的密码">
        </div>
        <div class="form-group">
            <label for="image">图片验证码</label>
            <input type="text" class="form-control" id="image" placeholder="输入的图片验证码">
        </div>
        <button type="submit" class="btn btn-primary">登 录</button>
    </form>

</div>
```

### 代码缩进

code-reformat code

# 6、flask框架

```
GET方式发送数据
	request.args

POST方式发送数据
	request.form
```

```
return "xxxx"
return render_template("xxxx.html")


return redirect("网址")
```

- 打开和展示HTML
  - 基于WEB框架【项目开发】
  - 基于本地文件
  - 基于Pycharm右上角【学习】

- CSS样式

  - 编写位置

    - 直接标签

    ```html
    <div style="xxx"><div>
    ```

    - 卸载head头部

      ```html
      <html>
          <head>
              <title>水电费</title>
              <style>
                  .c1{
                      color:red;
                  }
              </style>
          </head>
          <body>
              <span class='c1'>中国</span>
          </body>
      </html>
      ```

    - 写在CSS文件中

    ```html
    .c1{
    	color:red;
    }
    ```

    ```html
    <html>
        <head>
            <title>水电费</title>
            <link res='stytlesheet' href='.....'/>
        </head>
        <body>
            <span class='c1'>中国</span>
        </body>
    </html>
    ```

  - 选择器

  ```html
  <html>
      <head>
          <title>水电费</title>
          <style>
              .c1{
                  color:red;
              }
              #ix{
                  color:green;
              }
              a{
                  .....
              }
              .c1 a{}//后代标签
              .c1[xx='123']{}//属性
          </style>
      </head>
      <body>
          <span class='c1'>中国
              <a>xx</a>//后代标签
          </span> //类选择器
          <span id='ix'>伟大</span> //id选择器
          <a>最终</a> //标签选择器
          
          <span class='c1 c2'></span>
      </body>
  </html>
  ```

  - 常见样式

  ```
  - 高度 --->不能使用在行内标签上
  - 块级和行内
  	display:block;
  	display:inline
  	display:inline-block
  - 字体颜色、大小、加粗、字体样式
  ```

  
