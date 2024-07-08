# BootStrap CSS样式

# 0、初始

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <!--HTML注释:开发版本 -->
    <link rel="stylesheet" href="static/plugins/bootstrap-3.4.1/css/bootstrap.css"></link>
    <!--生产版本 压缩版-->
    <!-- <link rel="stylesheet" href="static/plugins/bootstrap-3.4.1/css/bootstrap.min.css"></link>-->


</head>
<body>
    <input type="button" value="提交"/>
    <input type="button" value="提交" class="btn-primary"/>
    <input type="button" value="提交" class="btn-success"/>
    <input type="button" value="提交" class="btn-danger"/>
    <input type="button" value="提交" class="btn-danger btn-xs"/>
    <input type="button" value="呈现" class="btn-block"/>
    <input type="button" value="呈现" class="btn-group-justified"/>

</body>
</html>
```

![image-20240604104924220](C:/Users/user/AppData/Roaming/Typora/typora-user-images/image-20240604104924220.png)

# 1、导航条的实现

- 登录[组件 · Bootstrap v3 中文文档 | Bootstrap 中文网 (bootcss.com)](https://v3.bootcss.com/components/#navbar)选择组件样式，导航条，复制代码。
- 将复制的HTML代码运行，更改圆角，重写一些.navbar
- ![image-20240604152230282](C:/Users/user/AppData/Roaming/Typora/typora-user-images/image-20240604152230282.png)

```html
<div class="navbar navbar-default">
    <div class="container-fluid">
        <!-- Brand and toggle get grouped for better mobile display -->
        <div class="navbar-header">
            <button type="button" class="navbar-toggle collapsed" data-toggle="collapse"
                    data-target="#bs-example-navbar-collapse-1" aria-expanded="false">
                <span class="sr-only">Toggle navigation</span>
                <span class="icon-bar"></span>
                <span class="icon-bar"></span>
                <span class="icon-bar"></span>
            </button>
            <a class="navbar-brand" href="#">中国联通</a>
        </div>

        <!-- Collect the nav links, forms, and other content for toggling -->
        <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
            <ul class="nav navbar-nav">
                <li class="active"><a href="#">中国电信 <span class="sr-only">(current)</span></a></li>
                <li><a href="#">中国移动</a></li>
                <li class="dropdown">
                    <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup="true"
                       aria-expanded="false">下拉菜单 <span class="caret"></span></a>
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
                <button type="submit" class="btn btn-default">交付</button>
            </form>
            <ul class="nav navbar-nav navbar-right">
                <li><a href="#">登录</a></li>
                <li><a href="#">注册</a></li>
                <li class="dropdown">
                    <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup="true"
                       aria-expanded="false">选择 <span class="caret"></span></a>
                    <ul class="dropdown-menu">
                        <li><a href="#">Action</a></li>
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
```

# 2、栅格系统

[全局 CSS 样式 · Bootstrap v3 中文文档 | Bootstrap 中文网 (bootcss.com)](https://v3.bootcss.com/css/#grid)

- 利用栅格划分区域，栅格将页面整体划分了12个区域

- 分类

  - 响应式，根据屏幕宽度不同

    - ```
      .col-sm-   750px   
      .col-md-   970px
      .col-g-	   750px
      当页面宽度大于750px才生效
      ```

  - 非响应式

    -             <div class="col-xs-2" style="background: #0f0f0f">广东</div>
                  <div class="col-xs-10" style="background: #2aabd2">深圳</div>

  - 列偏移——可以前面空几个格

    - ```html
      <div class="col-sm-offset-4 col-sm-4" style="background: #2aabd2">中间位置</div>
      
      ```

# 3、container

- container

  - ```html
    <div class="container">
        <div class="col-sm-9">左边</div>
        <div class="col-sm-3">右边</div>
    </div>
    ```

- container-fluid

  - ```html
    <div class="container-fluid">
        <div class="col-sm-9">左边</div>
        <div class="col-sm-3">右边</div>
    </div>
    ```

# 4、面板

```html
<div class="container">
    <div class="col-sm-9">左边</div>
    <div class="col-sm-3">
        <div class="panel panel-default">
            <div class="panel-heading">最新推荐</div>
            <div class="panel-body">
                我是一个粉刷匠，粉刷本领强！
            </div>
        </div>
        <div class="panel panel-primary">
            <div class="panel-heading">最佳选手</div>
            <div class="panel-body">
                Panel content
            </div>
        </div>
    </div>
</div>
```

![image-20240604161411309](C:/Users/user/AppData/Roaming/Typora/typora-user-images/image-20240604161411309.png)

# 5、分页

```html
<nav aria-label="Page navigation">
    <ul class="pagination">
        <li>
            <a href="#" aria-label="Previous">
                <span aria-hidden="true">«</span>
            </a>
        </li>
        <li><a href="#">1</a></li>
        <li><a href="#">2</a></li>
        <li><a href="#">3</a></li>
        <li><a href="#">4</a></li>
        <li><a href="#">5</a></li>
        <li>
            <a href="#" aria-label="Next">
                <span aria-hidden="true">»</span>
            </a>
        </li>
    </ul>
</nav>
```

![image-20240604161914074](C:/Users/user/AppData/Roaming/Typora/typora-user-images/image-20240604161914074.png)



**案例**

![f71b962110f9d4322a1991f247ca6a86](C:/Users/user/Documents/Tencent%20Files/1134686635/nt_qq/nt_data/Pic/2024-06/Ori/f71b962110f9d4322a1991f247ca6a86.png)

![image-20240604164156987](C:/Users/user/AppData/Roaming/Typora/typora-user-images/image-20240604164156987.png)

```html
<div class="container-fluid">
    <div class="col-sm-9">
        <div class="media">
            <div class="media-left">
                <a href="#">
                    <img class="media-object" src="..." alt="Top aligned media">
                <a>

            </div>
            <div class="media-body">
                <h4 class="media-heading">name</h4>
                Cras sit amet nibh libero, in gravida nulla. Nulla vel metus scelerisque ante sollicitudin
                commodo. Cras
                purus odio, vestibulum in vulputate at, tempus viverra turpis. Fusce condimentum nunc ac nisi
                vulputate
                fringilla. Donec lacinia congue felis in faucibus.
                Donec sed odio dui. Nullam quis risus eget urna mollis ornare vel eu leo. Cum sociis natoque
                penatibus
                et magnis dis parturient montes, nascetur ridiculus mus.
            </div>
        </div>
        <div class="media">
            <div class="media-left media-middle">
                <a href="#">
                    <img class="media-object" src="..." alt="...">
                </a>
            </div>
            <div class="media-body">
                <h4 class="media-heading">Middle aligned media</h4>
                ...
            </div>
        </div>
    </div>
    <div class="col-sm-3">
        <div class="panel panel-default">
            <div class="panel-heading">最新推荐</div>
            <div class="panel-body">
                我是一个粉刷匠，粉刷本领强！
            </div>
        </div>
        <div class="panel panel-primary">
            <div class="panel-heading">最佳选手</div>
            <div class="panel-body">
                Panel content
            </div>
        </div>
    </div>
</div>
<nav aria-label="Page navigation">
    <ul class="pagination">
        <li>
            <a href="#" aria-label="Previous">
                <span aria-hidden="true">«</span>
            </a>
        </li>
        <li><a href="#">1</a></li>
        <li><a href="#">2</a></li>
        <li><a href="#">3</a></li>
        <li><a href="#">4</a></li>
        <li><a href="#">5</a></li>
        <li>
            <a href="#" aria-label="Next">
                <span aria-hidden="true">»</span>
            </a>
        </li>
    </ul>
</nav>
```

# 6、登录页面的实现

![image-20240604164947551](C:/Users/user/AppData/Roaming/Typora/typora-user-images/image-20240604164947551.png)

- 宽度+居中（区域居中）
- 内边距
- 表单
- 阴影

## 6.1、中间方框的实现

```
<style>
    .box {
    width: 400px;
    height: 400px;
    margin-top: 50px;

    border: solid red;
    margin-left: auto;
    margin-right: auto;
    border-radius: 5px;

    padding-left: 20px;
    padding-right: 20px;
    padding-bottom: 30px;
    }

    .box h1 {
    text-align: center;
    }
</style>

```



## 6.2、表单

[全局 CSS 样式 · Bootstrap v3 中文文档 | Bootstrap 中文网 (bootcss.com)](https://v3.bootcss.com/css/#buttons)

选择相应的表单

```html
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <link rel="stylesheet" href="static/plugins/bootstrap-3.4.1/css/bootstrap.css">
    <style>
      .box{
        width: 400px;
        height: 400px;
        margin-top: 50px;

        margin-right: auto;
        margin-left: auto;
        border: solid #dddddd;
        border-radius: 5px;

        padding-left: 30px;
        padding-right: 30px;
        padding-bottom: 30px;

        box-shadow: 10px 10px 10px rgb(0 0 0 / 5%);
      }
      .box h2{
        text-align: center;
        padding-bottom: 20px;
      }
    </style>
</head>
<body>
  <div class="box">
    <h2>用户登录</h2>
    <form>
      <div class="form-group">
        <label for="user">用户名或手机号</label>
        <input type="text" class="form-control" id="user" placeholder="用户名或手机号">
      </div>
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
</body>
</html>
```

# 7、后台案例

![image-20240604202543606](C:/Users/user/AppData/Roaming/Typora/typora-user-images/image-20240604202543606.png)

- 导航
- 新建按钮
- 表格

```html
<nav class="navbar navbar-default">
    <div class="container">
        <!-- Brand and toggle get grouped for better mobile display -->
        <div class="navbar-header">
            <button type="button" class="navbar-toggle collapsed" data-toggle="collapse"
                    data-target="#bs-example-navbar-collapse-1" aria-expanded="false">
                <span class="sr-only">Toggle navigation</span>
                <span class="icon-bar"></span>
                <span class="icon-bar"></span>
                <span class="icon-bar"></span>
            </button>
            <a class="navbar-brand" href="#">Brand</a>
        </div>

        <!-- Collect the nav links, forms, and other content for toggling -->
        <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
            <ul class="nav navbar-nav">
                <li class="active"><a href="#">Link <span class="sr-only">(current)</span></a></li>
                <li><a href="#">Link</a></li>
                <li class="dropdown">
                    <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup="true"
                       aria-expanded="false">Dropdown <span class="caret"></span></a>
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
                <li><a href="#">Link</a></li>
                <li class="dropdown">
                    <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup="true"
                       aria-expanded="false">Dropdown <span class="caret"></span></a>
                    <ul class="dropdown-menu">
                        <li><a href="#">Action</a></li>
                        <li><a href="#">Another action</a></li>
                        <li><a href="#">Something else here</a></li>
                        <li role="separator" class="divider"></li>
                        <li><a href="#">Separated link</a></li>
                    </ul>
                </li>
            </ul>
        </div><!-- /.navbar-collapse -->
    </div><!-- /.container-fluid -->
</nav>
<div class="container">
    <button type="button" class="btn btn-primary">新建</button>
    <button type="button" class="btn btn-primary">删除</button>
    <button type="button" class="btn btn-primary">更改</button>
    <button type="button" class="btn btn-primary">查询</button>
</div>
<div class="container">
    <div class="bs-example" data-example-id="contextual-table">
        <table class="table">
            <thead>
            <tr>
                <th>#</th>
                <th>Column heading</th>
                <th>Column heading</th>
                <th>Column heading</th>
            </tr>
            </thead>
            <tbody>
            <tr class="active">
                <th scope="row">1</th>
                <td>Column content</td>
                <td>Column content</td>
                <td>Column content</td>
            </tr>
            <tr>
                <th scope="row">2</th>
                <td>Column content</td>
                <td>Column content</td>
                <td>Column content</td>
            </tr>
            <tr class="success">
                <th scope="row">3</th>
                <td>Column content</td>
                <td>Column content</td>
                <td>Column content</td>
            </tr>
            <tr>
                <th scope="row">4</th>
                <td>Column content</td>
                <td>Column content</td>
                <td>Column content</td>
            </tr>
            <tr class="info">
                <th scope="row">5</th>
                <td>Column content</td>
                <td>Column content</td>
                <td>Column content</td>
            </tr>
            <tr>
                <th scope="row">6</th>
                <td>Column content</td>
                <td>Column content</td>
                <td>Column content</td>
            </tr>
            <tr class="warning">
                <th scope="row">7</th>
                <td>Column content</td>
                <td>Column content</td>
                <td>Column content</td>
            </tr>
            <tr>
                <th scope="row">8</th>
                <td>Column content</td>
                <td>Column content</td>
                <td>Column content</td>
            </tr>
            <tr class="danger">
                <th scope="row">9</th>
                <td>Column content</td>
                <td>Column content</td>
                <td>Column content</td>
            </tr>
            </tbody>
        </table>
    </div>
</div>
```

## 7.1、后台管理+面板

![image-20240605130126857](C:/Users/user/AppData/Roaming/Typora/typora-user-images/image-20240605130126857.png)

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>后台管理+面板</title>
    <link rel="stylesheet" href="static/plugins/bootstrap-3.4.1/css/bootstrap.css">
</head>
<body>
<div class="container">
    <nav class="navbar navbar-default">
        <div class="container-fluid">
            <!-- Brand and toggle get grouped for better mobile display -->
            <div class="navbar-header">
                <button type="button" class="navbar-toggle collapsed" data-toggle="collapse"
                        data-target="#bs-example-navbar-collapse-1" aria-expanded="false">
                    <span class="sr-only">Toggle navigation</span>
                    <span class="icon-bar"></span>
                    <span class="icon-bar"></span>
                    <span class="icon-bar"></span>
                </button>
                <a class="navbar-brand" href="#">Brand</a>
            </div>

            <!-- Collect the nav links, forms, and other content for toggling -->
            <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
                <ul class="nav navbar-nav">
                    <li class="active"><a href="#">Link <span class="sr-only">(current)</span></a></li>
                    <li><a href="#">Link</a></li>
                    <li class="dropdown">
                        <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup="true"
                           aria-expanded="false">Dropdown <span class="caret"></span></a>
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
                    <li><a href="#">Link</a></li>
                    <li class="dropdown">
                        <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup="true"
                           aria-expanded="false">Dropdown <span class="caret"></span></a>
                        <ul class="dropdown-menu">
                            <li><a href="#">Action</a></li>
                            <li><a href="#">Another action</a></li>
                            <li><a href="#">Something else here</a></li>
                            <li role="separator" class="divider"></li>
                            <li><a href="#">Separated link</a></li>
                        </ul>
                    </li>
                </ul>
            </div><!-- /.navbar-collapse -->
        </div><!-- /.container-fluid -->
    </nav>
</div>
<div class="container">
    <div class="panel panel-default">
        <div class="panel-heading">表单区域</div>
        <div class="panel-body">
            <form class="form-inline">
                <div class="form-group">
                    <label for="exampleInputName2">Name</label>
                    <input type="text" class="form-control" id="exampleInputName2" placeholder="Jane Doe">
                </div>
                <div class="form-group">
                    <label for="exampleInputEmail2">Email</label>
                    <input type="email" class="form-control" id="exampleInputEmail2" placeholder="jane.doe@example.com">
                </div>
                <button type="submit" class="btn btn-success">保 存</button>
            </form>
        </div>
    </div>
    <div class="panel panel-default">
        <div class="panel-heading">数据列表</div>
        <table class="table table-bordered">
            <thead>
            <tr>
                <th>#</th>
                <th>First Name</th>
                <th>Last Name</th>
                <th>Username</th>
            </tr>
            </thead>
            <tbody>
            <tr>
                <th scope="row">1</th>
                <td>Mark</td>
                <td>Otto</td>
                <td>@mdo</td>
            </tr>
            <tr>
                <th scope="row">2</th>
                <td>Jacob</td>
                <td>Thornton</td>
                <td>@fat</td>
            </tr>
            <tr>
                <th scope="row">3</th>
                <td>Larry</td>
                <td>the Bird</td>
                <td>@twitter</td>
            </tr>
            </tbody>
        </table>

    </div>
    <nav aria-label="Page navigation">
            <ul class="pagination">
                <li>
                    <a href="#" aria-label="Previous">
                        <span aria-hidden="true">«</span>
                    </a>
                </li>
                <li><a href="#">1</a></li>
                <li><a href="#">2</a></li>
                <li><a href="#">3</a></li>
                <li><a href="#">4</a></li>
                <li><a href="#">5</a></li>
                <li>
                    <a href="#" aria-label="Next">
                        <span aria-hidden="true">»</span>
                    </a>
                </li>
            </ul>
        </nav>
</div>
</body>
</html>
```

# 8、图标

- bootstrap提供，但不多
- font Awesome [Font Awesome，一套绝佳的图标字体库和CSS框架 (dashgame.com)](https://fontawesome.dashgame.com/#google_vignette)

使用font Awesome的方法：

- 下载
- 引入

```html
    <link rel="stylesheet" href="./static/plugins/font-awesome-4.7.0/css/font-awesome.css">
```

- 去font awesome找相关的代码

# 9、BootStrap依赖

bootstrap依赖JavaScript的类库，jQuery.

- 下载jQuery,在页面上
