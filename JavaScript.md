# JavaScript

- HTML,裸体

- CSS，好看

- JavaScript，动态

  - 编程语言，浏览器就是JavaScript语言的解释器

  - 类库(模块)

  - DOM和BOM

    - ```
      相当于编程语言内置的模块
      例如：python中的re、random、time、json等模块
      ```

- jQuery

  - ```
    相当于是编程语言的第三方模块
    例如：requests、openpyxl
    ```

  

# 1、初步了解

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
  <style>
    .menus{
      width: 200px;
      border: 1px solid red;
    }
    .menus .header{
      background-color: gold;
      padding: 20px 10px;
    }
  </style>
</head>
<body>
  <div class="menus">
    <div class="header" onclick="myfunc()">大标题</div>
    <div class="item">内容</div>
  </div>
  <script type="text/javascript">
    function myfunc(){
      // alert("你好啊！");
      confirm("是否要继续？");
    }

  </script>
</body>
</html>
```

![image-20240605154644746](C:/Users/user/AppData/Roaming/Typora/typora-user-images/image-20240605154644746.png)

# 2、代码位置

- 在head内部

  - ```html
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Title</title>
    
        <script type="text/javascript">
          //编写的代码
        </script>
    </head>
    ```

- 在body标签的内部中的最尾部(推荐)

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>

<script type="text/javascript">
      //编写的代码
</script>
</body>
</html>
```

# 3、JS代码的存在形式

- 当前的HTML中。

  - ```
    <script type="text/javascript">
          //编写的代码
    </script>
    ```

- 在其它JS文件中导入使用（导入一般也放在下面）

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    
</head>
<body>


  <script src="static/js/my.js"></script> //导入JS代码
  <script type="text/javascript">
    //编写代码
  </script>
</body>
</html>
```

# 4、注释

- HTML的注释

  - ```html
    <!--注释内容-->
    ```

- CSS的注释`style代码块中`

  - ```css
    /*注释内容*/
    ```

- JavaScript的注释，`script代码块中`

  - ```js
    //注释内容
    /*注释内容*/
    ```

# 5、JavaScript编程语言的学习

## 5.1、变量

变量的定义

```HTML
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
    <script type="text/javascript">
        var name= "高英";  
    </script>
</body>
</html>
```

输出：console.log(变量名)

```HTML
<body>
    <script type="text/javascript">
        var name= "高英";
        console.log(name); //查看变量
    </script>
</body>
```

## 5.2、字符串类型

```javascript
//声明
var name = "高倩";
var name = String("高倩");
```

```javascript
//常见功能
var name = "中国联通"

var v1 = name.length; //字符串长度
var v2 = name[0]; //字符串第0个元素  name.charAt(0)
var v3 = name.trim(); //去除空白
var v4 = name.substring(0,2)  //相当于切片，前取后不取
```

### 案例：跑马灯

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
  <span id="txt">欢迎中国联通领导高倩莅临指导</span>

  <script type="text/javascript">
    function show() {
      //1.去HTML中找到某个标签并获取他的内容(DOM)
      var tag = document.getElementById("txt");
      var datastring = tag.innerText;

      console.log(datastring);

      //2.动态起来，把文本中的第一个字符放在字符串后面
      var firstChar = datastring[0];
      var otherString = datastring.substring(1,datastring.length);

      var newText = otherString + firstChar;


      //3.在HTML标签中更新内容
      tag.innerText = newText;
    }

    //JavaScript中的定时器:定时执行某个函数，如：每秒中执行一次
    setInterval(show,1000);
  </script>
</body>
</html>
```

## 5.3、数组

```javascript
//定义
var v1 = [11,22,33];
var v2 = Array{[11,22,33,44]};
```

```javascript
 //操作

//添加
var v1 = [11,22,33,44];

v1[1];
v1[0] = "高倩";

v1.push("联通");     //尾部追加，相当于python中的append
v1.unshift("联通")   //开头追加，["联通",11,22,33,44]
v1.splice(索引位置,0,元素)  //在任意位置插入元素。
v1.splice(1,0,"中国")   //结果 [11,"中国",33,44]


//删除
v1.pop()  //尾部删除
v1.shift() //头部删除
v1.splice(索引位置,1)  //任意位置元素删除
v1.splice(2,1) //结果：[11,22,44]
```

```javascript
//数组内部元素进行循环

var v1 = [11,22,33,44];

for(var idx in v1){
    //获取到的idx是v1的索引
    //idx=0/1/2/3   data = v1[idx] 获取V1内部元素
}

for(var i=0;i<v1.length; i++)
    {
        data = v1[i]
    }
```

注意：break和continue

### 案例：动态数据

```HTML
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
    <ul id="city">
<!--        <li>北京</li>-->
<!--        <li>上海</li>-->
<!--        <li>深圳</li>-->
    </ul>

    <script type="text/javascript">
        //发送网络请求，获取数据
        var cityList = ["北京","上海","深圳"];
        for(var idx in cityList){
            var text = cityList[idx];  //获取到了文本


            //将文本添加到标签中
            //创建<li><li>
            var tag = document.createElement("li");

            //在li标签中写入内容
            tag.innerText = text;

            //添加到id="city"那个标签的里面。DOM
            var parentTag = document.getElementById("city"); //先找到city标签
            parentTag.appendChild(tag)
        }
    </script>
</body>
</html>
```

## 5.4、对象(python：字典)

```javascript
//python
info = {
    "name" = "高倩",
    "age" = 18
}

//javascript
info = {
    name:"高倩",
    age:18
}
```

```javascript
//操作
info.age;
info.name = "国志";


info["age"];
info["name"] = "国志";

delect info["age"] //删除

// 循环
info = {
    name:"高倩",
    age:18
}

for(var key in info){
    //key=name/age
    data = info[key]
}
```

### 案例：动态表格

```HTML
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
<table border="1">
    <thead>
    <tr>
        <th>id</th>
        <th>姓名</th>
        <th>年龄</th>
    </tr>
    </thead>
    <tbody id="body">
    <!--    script中生成-->
    </tbody>
</table>

<script type="text/javascript">
    //数据通过网络请求获取
    //添加多行
    var dataList = [
        {id: 1, name: "国志", age: 19},
        {id: 2, name: "骄傲", age: 20},
        {id: 3, name: "吱嘎", age: 22},
        {id: 4, name: "好噶", age: 35},
        {id: 5, name: "九八", age: 40},
        {id: 6, name: "按八分", age: 56}
    ]
    for (var idx in dataList) {
        var info = dataList[idx];
        var tr = document.createElement("tr");
        //取值
        for (var key in info) {
            var text = info[key];
            //生成<td>，并将值写入<td>标签中
            var td = document.createElement("td");  //生成td标签
            td.innerText = text;  //让td标签中的内容为text
            tr.appendChild(td); //每生成一个td标签，都要加入到tr中

            var bodyTag = document.getElementById("body");
            bodyTag.appendChild(tr);
        }
    }
    // //添加一行
    // var info = {id: 1, name: "国志", age: 19};
    //
    // //创建标签
    // var tr = document.createElement("tr");
    // //取值
    // for (var key in info) {
    //     var text = info[key];
    //     //生成<td>，并将值写入<td>标签中
    //     var td = document.createElement("td");  //生成td标签
    //     td.innerText = text;  //让td标签中的内容为text
    //     tr.appendChild(td); //每生成一个td标签，都要加入到tr中
    //
    //     var bodyTag = document.getElementById("body");
    //     bodyTag.appendChild(tr);
    // }
    // console.log(tr);
</script>
</body>
</html>
```

![image-20240606103414384](C:/Users/user/AppData/Roaming/Typora/typora-user-images/image-20240606103414384.png)

## 5.5、条件语句

语法：

```javascript
if(条件){
    
}else if(条件){
    
}else if(条件){
    
}else{
    
}
```

## 5.6、函数

```python
def func():
	函数内容....
func()
```

```javascript
function func(){
    ...
}
func()
```

## 5.7、DOM

==**DOM，就是一个模块，模块可以对HTML页面中的标签进行操作。**==

```javascript
//根据id获取标签 
var Tag = document.getElementById("xxx");

//获取标签中的文本
Tag.innerText

//修改标签中的文本
Tag.innerText = 'xxx';

//创建标签
var tag =  document.createElement("div"); 
tag.innerText = "XXXX" //往标签中写入内容

//往标签中添加标签
bodyTag.appendChild(tr);
```

### 5.7.1、事件的绑定

一点击按钮，就执行某个函数。

```HTML
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
    <input type="button" value="点击添加" onclick="addCityinfo()">
    <ul id="city">

    </ul>

    <script type="text/javascript">
        function addCityinfo(){
            var liTag = document.createElement('li');
            liTag.innerText = "联通";

            var cityTag = document.getElementById('city');
            cityTag.appendChild(liTag);
        }
    </script>
</body>
</html>
```

- 改进——添加用户输入

```HTML
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
    <input type="text" placeholder="请输入内容" id="txtUser">
    <input type="button" value="点击添加" onclick="addCityinfo()">
    <ul id="city">

    </ul>

    <script type="text/javascript">
        function addCityinfo(){

            //1.获取输入框中的数据
            var text = document.getElementById("txtUser")
            //2.获取input框中用户输入的内容
            var data = text.value;

            //2.1 判断用户是否输入为空，只有不为空才继续
            if (data.length > 0){
                 //3.创建标签
                var liTag = document.createElement('li');
                //4.更新标签中的内容
                liTag.innerText = data;
                //5.将li标签添加到ul标签中
                var cityTag = document.getElementById('city');
                cityTag.appendChild(liTag);
                //6.将输入框内容清空
                text.value = ""
            }else {
                alert("输入不能为空")
            }

        }
    </script>
</body>
</html>
```

![image-20240606152234313](C:/Users/user/AppData/Roaming/Typora/typora-user-images/image-20240606152234313.png)

注意：DOM中还有很多操作

```
DOM可以实现很多功能，但是很繁琐
页面上的效果:jQuery来实现/vue.js/react.js
```

25集2：30：00开始总结

# 6、jQuery

jQuery是一个JavaScript的第三方模块（第三方类库）。

- 基于jQuery,自己开发一个功能
- 现成的工具，依赖jQuery,例如：BootStrap动态效果。

## 6.1、快速上手

- 下载jQuery
- 应用jQuery

```HTML
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
  <h1 id="txt">中国联通</h1>


  <script src="./static/plugins/jQuery/jQuery.js"></script>
  <script type="text/javascript">
    //利用jQuery中的功能实现某些效果

    //1.找到id=txt标签
    $("#txt").text("广西移动");
    //2.内容修改

  </script>
</body>
</html>
```

### 6.1.1、寻找标签(直接寻找)

- ID选择器

```HTML
<body>
    <h1 id="txt"> 中国联通 </h1>
    <h1>中国移动</h1>
    <h1>中国电信</h1>
<script>
    $("#txt")
</script>
</body>
```

```HTML
$("#txt")
```

- 样式选择器

```html
<body>
    <h1 class="c1"> 中国联通 </h1>
    <h1 class="c1">中国移动</h1>
    <h1 class="c2">中国电信</h1>
</body>
```

```javascript
$(".c1")
```

- 标签选择器

```html
 <h1 class="c1"> 中国联通 </h1>
 <div class="c1">中国移动</div>
 <h1 class="c2">中国电信</h1>
```

```javascript
$("h1")
```

- 层级选择器

```html
<h1 class="c1"> 中国联通 </h1>
<h1 class="c1">
	<div class="c2">
        <span></span>
        <a></a>
    </div>    
</h1>
<h1 class="c2">中国电信</h1>
```

```javascript
$(".c1 .c2 a")
```

- 多选择器

```HTML
<h1 class="c1"> 中国联通 </h1>
<h1 class="c1">
	<div class="c3">
        <span id="c2"></span>
        <a></a>
    </div>    
</h1>
<ul>
    <li></li>
</ul>
<h1 class="c2">中国电信</h1>
```

```javascript
$(".c1,.c3,#c2,li")
```

- 属性选择器

```html
<input type="text" name='n1' />
<input type="text" name='n2' />
<input type="text" name='n3' />
```

```javascript
$("input[name="n1"]")
```

### 6.1.2、寻找标签(间接寻找)

- 找到兄弟

```html
<div>
    <div>北京</div>
    <div id="c1">上海</div>
    <div>深圳</div>
    <div>广州</div>
</div>
```

```javascript
$("#c1")   上海
$("#c1").prev()  北京
$("#c1").next()  深圳
$("#c1").next().next()  广州

$("#c1").siblings()  找到所有兄弟
```

- 找到父子

```html
<div>
    <div>
        <div>北京</div>
        <div id="c1">上海
        	<div> 青浦区</div>
            <div class="p10"> 宝山区</div>
        </div>
        <div>深圳</div>
        <div>广州</div>
    </div>
    <div>
        <div>陕西</div>
        <div>山西</div>
        <div>河北</div>
        <div>河南</div>
    </div>
</div>
```



```javascript
$("#c1").parent()    父亲
$("#c1").parent().parent() 

$("#c1").childern()    //获取所有的孩子
$("#c1").childern(".p10")   //宝山区，所有的儿子中寻找p10的标签

$("#c1").find(".p10")   //去所有的子孙中招P10标签
$("#c1").find("div")
```

### 案例：菜单的切换

- 双击实现隐藏标题

```html
<head>
    <meta charset="UTF-8">
    <title>Title</title>
  <style>
    .menu{
      width: 200px;
      height: 800px;
      border: 1px solid red;
    }

    .menu  .header{
      background-color: gold;
      padding: 10px 5px;
      border-bottom: 1px dotted #dddddd;

      cursor: pointer;
      /*//鼠标放上去变成小手*/
    }
    .menu .content a{
      display: block;   //占一整行显示
      padding: 5px 5px;
      border-bottom: 1px dotted #dddddd;
    }
    .hinder{
      display: none;  //显示隐藏
    }
  </style>
</head>

<body>
  <div class="menu">
    <div class="item">
      <div class="header" onclick="clickMe(this);">上海</div>
      <div class="content hinder">
        <a href="">宝山区</a>
        <a href="">青浦区</a>
        <a href="">浦东区</a>
      </div>
    </div>


    <div class="item">
      <div class="header" onclick="clickMe(this)">北京</div>
      <div class="content hinder">
        <a href="">东城区</a>
        <a href="">西城区</a>
        <a href="">丰台区</a>
      </div>
    </div>
  </div>






  <script src="static/plugins/jQuery/jQuery.js"></script>
  <script>

    // 这个函数实现双击就隐藏
    function clickMe(self){
      // $(self)-->表示当前点击的那个标签
      // 移除标签样式 $(self).next().remove("hinder")
      // $(self).next().removeClass("hinder");

      var hashide = $(self).next().hasClass("hinder");
      if(hashide){
        $(self).next().removeClass("hinder");
      }else{
        $(self).next().addClass("hinder");
      }
    }
  </script>
</body>

```

- 点击一个标题，只有这个标题显示，其他的全部隐藏

```html
<body>
  <div class="menu">
    <div class="item">
      <div class="header" onclick="clickMe(this);">上海</div>
      <div class="content hinder">
        <a href="">宝山区</a>
        <a href="">青浦区</a>
        <a href="">浦东区</a>
      </div>
    </div>


    <div class="item">
      <div class="header" onclick="clickMe(this)">北京</div>
      <div class="content hinder">
        <a href="">东城区</a>
        <a href="">西城区</a>
        <a href="">丰台区</a>
      </div>
    </div>

     <div class="item">
      <div class="header" onclick="clickMe(this);">上海2</div>
      <div class="content hinder">
        <a href="">宝山区</a>
        <a href="">青浦区</a>
        <a href="">浦东区</a>
      </div>
    </div>

    <div class="item">
      <div class="header" onclick="clickMe(this)">北京2</div>
      <div class="content hinder">
        <a href="">东城区</a>
        <a href="">西城区</a>
        <a href="">丰台区</a>
      </div>
    <div>
  </div>

  <script src="static/plugins/jQuery/jQuery.js"></script>
  <script>

    // 这个函数实现双击就隐藏
    function clickMe(self){
      // $(self)-->表示当前点击的那个标签
      // 移除标签样式 $(self).next().remove("hinder")
      // $(self).next().removeClass("hinder");

      var hashide = $(self).next().hasClass("hinder");
      if(hashide){
        $(self).next().removeClass("hinder");
      }else{
        $(self).next().addClass("hinder");
      }
    }
  </script>
</body>
```

![image-20240608161830848](C:/Users/user/AppData/Roaming/Typora/typora-user-images/image-20240608161830848.png)

### 6.1.3、操作样式

- addClass
- removeClass
- hasClass



## 6.2、值的操作

- div标签中值的操作

```html
<div class="c1">
    内容
</div>
```

```javascript
$("#c1").text()   //获取文本内容
$("#c1").text("真的烦")  //设置文本内容
```

- input标签中值的操作

```HTML
<input type="text" id="c2">
```

```JAVASCRIPT
$("#c2").val()   //获取用户输入的值
$("#c2").val("哈哈哈哈")  //设置值
```

### 案例：获取输入文本框中的内容，并写入ul标签中——动态创建数据

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
  <input type="text" id="txtUser" placeholder="用户名">
  <input type="text" id="txtEmail" placeholder="邮箱">
  <input type="button" value="提交" onclick="getInfo()">
  <ul id="view">

  </ul>


  <script src="static/plugins/jQuery/jQuery.js"></script>
  <script>
    function getInfo(){
      // 获取用户输入的用户名和密码
      var username = $("#txtUser").val();
      var email = $("#txtEmail").val();
      var dataString = username + email;

      //2.创建Li标签:$("<li>"),写入内容
      var newLi = $("<li>").text(dataString);
      //3.将新创建的li标签添加到Ul中
      $("#view").append(newLi);
    }
  </script>

</body>
</html>
```

- 效果

![image-20240608164906632](C:/Users/user/AppData/Roaming/Typora/typora-user-images/image-20240608164906632.png)

## 6.3事件（之前都是DOM）

- 以前的绑定事件——以DOM方式绑定事件

```html
  <input type="button" value="提交" onclick="getInfo()">
  <script src="static/plugins/jQuery/jQuery.js"></script>
  <script>
    function getInfo(){
      
    }
```

- jQuery中绑定事件
  - 点击并获取文本

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
<ul>
  <li>百度</li>
  <li>谷歌</li>
  <li>搜狗</li>
</ul>

<script src="static/plugins/jQuery/jQuery.js"></script>
<script>
    //jQuery点击并获取文本
  $("li").click(function (){
    var text = $(this).text();
    console.log(text);
  })
</script>

</body>
</html>
```

- 在jQuery中可以删除某个标签(删除元素)

```html
<div id="c1">内容</div>


<script src="./static/plugins/jQuery/jQuery.js"></script>
<script>
    $("#c1").remove()  //将c1标签删除
</script>
```

- 当页面框架加载完成之后执行代码

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>

</head>
<body>
<div id="c1">内容</div>


<ul>
    <li>百度</li>
    <li>谷歌</li>
    <li>搜狗</li>
</ul>
 <script src="./static/plugins/jQuery/jQuery.js"></script>
<script>
    $(function (){
        //当页面框架加载完成之后就自动执行
        $("li").click(function (){
            $(this).remove();
        })
    })
</script>

</body>
</html>
```

## 6.4、案例：表格操作

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
  <table border="1">
    <thead>
    <tr>
      <th>ID</th>
      <th>姓名</th>
      <th>年龄</th>
      <th>操作</th>
    </tr>
    </thead>
    <tbody>
    <tr>
      <td>1</td>
      <td>许磊</td>
      <td>19</td>
      <td>
        <input type="button" value="删除" class="delect">
      </td>
    </tr>

    <tr>
      <td>2</td>
      <td>许磊</td>
      <td>19</td>
      <td>
        <input type="button" value="删除" class="delect">
      </td>
    </tr>
    <tr>
      <td>3</td>
      <td>许磊</td>
      <td>19</td>
      <td>
        <input type="button" value="删除" class="delect">
      </td>
    </tr>
    <tr>
      <td>4</td>
      <td>许磊</td>
      <td>19</td>
      <td>
        <input type="button" value="删除" class="delect">
      </td>
    </tr>
    </tbody>

  </table>
  <script src="static/plugins/jQuery/jQuery.js"></script>
  <script>
    $(function (){
      //找到所有的`class=delect的标签,绑定事件
      $(".delect").click(function (){
        //删除当前行的数据
      $(this).parent().parent().remove();
    });
    })

  </script>

</body>
</html>
```

![image-20240608180913020](C:/Users/user/AppData/Roaming/Typora/typora-user-images/image-20240608180913020.png)

# 7、整合前端页面案例

- HTML
- CSS
- JavaScript
- BootStrap(依赖jQuery，现有jQuery再有BootStrap)

