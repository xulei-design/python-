## 1.Flask-SQLAlchemy(不需要用SQL语句去操作数据库)

## 2.Flask-SQLAlchemy基本使用

### 2.1连接MySQL

使用Flask-SQLAlchemy操作数据库之前，要先创建一个由Flask-SQLAlchemy提供的SQLAlchemy类对象。在创建这个类的时候，要传入当前的app.然后还需要在app.config中设置SQLALCHEMY_DATABASE_URI，来配置数据库的连接，示例代码如下。

```python
from flask import Flask,render_template,request,redirect,url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text

#1.设置数据库连接:在Flask应用中配置连接到MYSQL数据库的信息,

app = Flask(__name__)
#MySQL所在主机名
HOSTNAME = "127.0.0.1"
#Mysql监听端口号，默认是3306
PORT = 3306
#连接MySQL的用户名
USERNAME = "root"
#连接MySQL的密码
PASSWARD = "XU938374"
#MySQL上创建的数据库名称
DATABASE = "test"

# 在app.config中设置好连接数据库的信息，使用SQLAlchemy(db)创建一个db对象
app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{USERNAME}:{PASSWARD}@{HOSTNAME}:{PORT}/{DATABASE}?charset=utf8"

#SQLAlchemy会自动读取app.config中连接数据库的信息
db = SQLAlchemy(app)
```

```python
Flask(__name__)语句含义：
`Flask` 是 Flask 框架的核心类，用于创建 Web 应用程序。
 `__name__` 是 Python 中的一个内置变量，代表当前模块的名称。当 Python 文件直接被运行时，`__name__` 的值为 `'__main__'`；当作为模块被导入时，`__name__` 的值为模块的名字。
传递给 `Flask()` 构造函数的参数是应用程序的名称或者所在的包。在大多数情况下，传递 `__name__` 可以让 Flask 框架找到相关资源并设置应用程序的根路径。

因此，`Flask(__name__)` 语句的作用是创建一个 Flask 应用实例，并使用当前模块的名称作为应用程序的名称或根目录。这是 Flask 应用的一个常见用法。

```



测试数据库是否连接成功

```python
#测试是否连接成功
with app.app_context():
    with db.engine.connect() as conn:
        rs = conn.execute(text("select 1"))
        print(rs.fetchone())
#输出(1,)证明连接成功
```

### 2.2 ORM模型

​	ORM（对象关系映射）是一种编程技术，用于在关系型数据库和面向对象编程语言之间建立映射关系，从而将数据库中的表、行和列映射到程序中的对象、属性和方法。ORM 提供了一种抽象的方法，使开发者可以通过面向对象的方式操作数据库，而不必直接编写 SQL 查询语句。

以下是 ORM 的一些重要概念和优势：

1. **对象模型和关系模型之间的映射：** ORM 允许开发者使用类和对象来表示数据库中的实体和关系，从而在代码中创建对象模型，并将其映射到数据库中的关系模型。

2. **简化数据库操作：** ORM 隐藏了许多与数据库操作相关的细节，使开发者可以通过简单的方法、属性和类来进行数据的增删改查，而不必编写复杂的 SQL 查询语句。

3. **跨平台性和数据库透明性：** ORM 屏蔽了底层数据库的差异，使得代码可以轻松地切换或同时使用不同类型的数据库，而不必更改大部分代码。

4. **更易维护和测试：** ORM 使代码更具可读性和可维护性，因为它更贴近面向对象的编程范式，易于测试和维护。

5. **提高开发效率：** ORM 的使用简化了数据库操作，减少了开发工作量，因为不需要编写大量的 SQL 查询和数据转换代码。

以下我们用Flask-SQLAlchemy来创建一个User模型，示例代码如下：

```python
class User(db.Model):
    #表名
    __tablename__ = "user"
    #添加字段
    id = db.Column(db.Integer,primary_key=True,autoincrement=True) #db.Integer整型,自动增长
    username = db.Column(db.String(80),unique=True,nullable=False)#字符串类型，会映射成数据库中Varchar类型
    email = db.Column(db.String(120),unique=True,nullable = False)
    def __init__(self,username,email):
        self.username = username
        self.email = email
with app.app_context():#不加会出现上下文错误
	db.create_all()#将所有的表同步到数据库中
```

### 2.3 CURD操作（增删改查）

ORM（对象关系映射）模型的 CURD 操作指的是在使用 ORM 框架时针对对象模型所执行的增加（Create）、查询（Read）、更新（Update）和删除（Delete）数据库中的操作。

使用ORM进行CRUD操作，需要先把操作添加到会话中，通过db.session可以获取到会话对象。会话对象只是在内存中，如果想要把会话中的操作提交到数据库中，需要调用db.session.commit()操作，如果想要把会话中的操作回滚，则可以通过db.session.rollback()实现。下面分别对CURD进行详解。

以下是使用 ORM 模型进行 CURD 操作的基本示例（以 SQLAlchemy 为例）：

**1. 创建对象：Create**

使用ORM创建一条数据非常简单，先使用ORM模型创建一个对象，然后添加到会话中，再进行commit操作即可，示例代码如下

```python
@app.route('/User/add')
def add_user():
    #创建ORM对象
    user1 = User("姜明凡",'1134686665@qq.com')
    user2 = User("张三","1154547211@qq.com")
    #将ORM对象添加到db.session中
    db.session.add(user1)
    db.session.add(user2)
    #将db.session中的改变同步到数据库中
    db.session.commit()
    return "用户创建成功！"
```

**2. 查询对象：Read**

```python
# 查询所有用户
users = User.query.all()
# 根据条件查询特定用户
@app.route("/User/query")
def query_User():
    #1.get查找:根据主键查找
    #query继承自db.model
    user = User.query.get(1)
    print(f"{user.id}:{user.username}--{user.email}")
    #2.filter_by查找
    #query:类数组，users是一个类数组的query类型
    users = User.query.filter_by(username = '姜明凡')#筛选对象
    for user in users:
        print(user.username)
    #.first()是获取第一个满足条件的数据
    user = User.query.filter_by(username = '许磊').first()
    print(user)
    return "数据查找成功！"
```

- 除了filter和filter_by以外，Flask_SQLAlchemy还提供以下过滤方法：

|         方法名          |               描述               |
| :---------------------: | :------------------------------: |
|     query.filter()      |         根据查询条件过滤         |
|    query.fiter_by()     |        根据关键字参数过滤        |
| query.slice(start,stop) |        对结果进行切片操作        |
|   query.limit(limit)    |        对结果数量进行限制        |
|  query.offset(offset)   | 在查询的时候跳过前面offset条数据 |
|    query.order_by()     |       根据给定字段进行排序       |
|    query.group_by()     |       根据给定字段进行分组       |

**3. 更新对象：Update**

```python
@app.route("/User/update")
def User_update():
    # 查询要更新的对象
    user = User.query.filter_by(username='John').first()
    # 更新对象属性
    user.email = 'new_email@example.com'
    #将更新过后的数据同步到数据库中
    db.session.commit()
```

**4. 删除对象：Delete**

```python
# 查询要删除的对象
user = User.query.filter_by(username='John').first()
# 从数据库中删除对象
db.session.delete(user)
db.session.commit()# 从数据库中删除对象
db.session.delete(user)
db.session.commit()
```

在这个例子中，假设 `User` 是一个 SQLAlchemy 模型类，代表了数据库中的用户表。通过使用 ORM 模型的 API，可以轻松地执行这些 CURD 操作，而不必直接编写 SQL 查询语句。这些操作能够有效地管理数据库中的数据，使开发者能够更方便地对数据库进行增加、查询、更新和删除操作。

## 3.表关系

​	数据库表之间的关系是指不同表之间的联系和连接方式，这些关系通常用于描述实体之间的相关性和交互。在关系型数据库中，有几种常见的表关系：

1. **一对一关系 (One-to-One Relationship)：**

  这种关系指的是两个实体之间的一对一关系。在数据库中，每个实体的记录只与另一个实体的一个记录相关联。例如，一个人只能有一个身份证号，而一个身份证号也只能对应一个人。

2. **一对多关系 (One-to-Many Relationship)：**

  这种关系指的是一个实体的记录可以与另一个实体的多个记录相关联。例如，在一个学校数据库中，一个班级可以有多个学生，但每个学生只能属于一个班级。

3. **多对多关系 (Many-to-Many Relationship)：**

  这种关系指的是两个实体之间的多对多关系。在数据库中，一个实体的多个记录可以与另一个实体的多个记录相关联。例如，学生和课程之间的关系就是多对多关系，一个学生可以选择多门课程，而一门课程也可以被多个学生选择。

​	在关系型数据库中，这些关系可以通过外键（Foreign Key）来建立和管理。外键是一个字段（或一组字段），它在一个表中创建引用另一个表的关联。通过外键，可以实现不同表之间的关联，确保数据的完整性和一致性。

### 3.1外键

外键是数据库层面的技术，在Flask-SQLAlchemy中支持创建ORM模型的时候就指定外键，创建外键是通过db.ForeignKey实现的。比如创建了一个Article表，这个表有一个author_id字段，通过外键引用user表的id字段，用来保存文章是谁编写的，那么article的模型代码如下：