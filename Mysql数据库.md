# Mysql数据库基础篇

## 1.基础知识介绍

#### 1.1 mysql基本操作

- 进入mysql的根目录：mysql -u root -p
- 被提示输入mysql密码：XU938374

如何导入数据

> - 新建一个数据库，命名为one
> - 点开one,右键选择导入数据

#### 1.1.2 mysql 环境配置

## 2. 数据库管理

#### 2.1 内置客户端操作

当连接上mysql之后，执行以下指令（一般称为SQL语句），就可以对MYSQL的数据进行操作

- 查看当前所有数据库：show databases;
- 创建数据库：`creat database 数据库名 DEFAULT utf8 COLLATE utf8_general_ci;`

​	`create database 数据库名`

- 删除数据库：`drop database 数据库名;`
- 进入数据（进入文件）：`use 数据库;`

```python
#1. 登陆Mysql
C:\Users\战神>mysql -u root -p
Enter password: ********
```

#### 2.2 创建数据表的语法形式

```sql
creat table [if not exists] 数据表名(
	字段名1 数据类型1 [NOT NULL|NULL][DEFAULT 列默认值][COMMENT 注释信息] PRIMARY KEY,
    字段名2 数据类型2 [NOT NULL|NULL][DEFAULT 列默认值][COMMENT 注释信息]
......);
```

##### 2.2.1 SQL语言

> DDL语言：
>
> - 即数据库定义语言
> - creat创建库表，alter修改表，drop删除表

> DML语言
>
> - 即数据库操作语言（对表中数据进行操作）
> - insert插入，delect删除，update更新，select查询

insert插入

> - 用来插入行到数据库表的，要求制定==表名==和被插入到新行中的==值==，注意插入的值和列要保持一一对应关系
>   - insert into ==worker==(工号，年龄，性别，岗位) values('001','蛋卷','25','女',测试开发);
> - 如果想一次性插入多条语句，则每组值用（）括起来，并用逗号隔开，写法如下：
>   - insert into ==表名==(列名1,列名1,列名3,列名4.....) values(值1,值2,值3,值4......),(值1,值2,值3,值4......),......

delect删除

> - 删除整张表，则用
>   - delect from 表名;
> - 删除满足筛选条件的行，则用
>   - delect from 表名 where 条件;
>   - 条件与条件之间有两种连接方式：
>     - 同时满足用and,格式如：delect from 表名 where 条件1and条件2and 条件3.......
>     - 多个条件只需满足其中一个,用or，格式如：delect from 表名 where 条件1 or 条件2 or 条件3....
> - 删除数据要注意==外键==的影响
>   - <img src="D:\markdowan笔记\图片\delect.jpg" style="zoom:25%;" />

update 更新

用来修改表中的数据

> - 比如将worker表中的岗位改为软件开发，则写法如下；
>   - update worker set 岗位 = ’软件开发‘；
> - 如果要修改多列数据，则用
>   - update 表名 set 列名1 = 值1， 列名2 = 值2，.....;
> - 如果是有条件的更新，则用
>   - update 表名 set 列名1 = 值1 where 条件;
>   - 例如：把性别男的工人转岗到软件开发，写法如下：update worker set 岗位 = ’软件开发‘ where 性别 = ’男‘；

select 查询

> - 查询所有，select * from 表名；
> - 查询某一列，select 列名 from 表名;
> - 查询多个列，select 列名1,列名2,....from 表名;

如果想使用==别名==的方式对数据显示的标题做修改，则可以写

> select 列名 '别名' from 表名;
>
> 使用==关键字as==来连接表达式和指定的列名，写法如下：
> select 列名 as ’别名‘ from 表名；

#### 2.3 数据库管理

安装上数据库之后，就要学习指令了，通过指令让mysql去做出一些文件操作。

<img src="D:\markdowan笔记\图片\12.jpg" style="zoom: 50%;" />



如何将数据库管理系统与之前的文件管理做类比的话：

| 数据库管理系统 |      文件管理       |
| :------------: | :-----------------: |
|     数据库     |       文件夹        |
|     数据表     | 文件夹下的excel文件 |

接下来，先学习数据库（文件夹）相关操作的指令

<img src="D:\markdowan笔记\图片\QQ图片.jpg" style="zoom:50%;" />

#### 2.4 内置客户端操作

当连接上mysql之后，执行以下指令（一般称为SQL语句），就可以对MYSQL的数据进行操作

- 查看当前所有数据库：show databases;
- 创建数据库：`creat database 数据库名 DEFAULT utf8 COLLATE utf8_general_ci;`

​	`create database 数据库名`

- 删除数据库：`drop database 数据库名;`
- 进入数据（进入文件）：`use 数据库;`

#### 2.5 python代码操作

安装pymysql模块

安装完成后，就可以编写代码：

```python
import pymysql
#连接mysql（socket）
conn = pymysql.connect(host='127.0.0.1',port=3306,user='root',passwd='XU938374',charset="utf8")
cursor = conn.cursor()

#1.查看数据库
#发送指令
cursor.execute("show databases")
#获取指令结果
result = cursor.fetchall() //python接受返回的mysql指令
print(result) 
#(('cigarettes',), ('information_schema',), ('mysql',), ('performance_schema',), ('sakila',), ('sys',), ('world',))
#2.创建数据库
#发送指令
cursor.execute("create database db3 default charset utf8 collate utf8_general_ci")
conn.commit()

#3.查看数据库
#发送指令
cursor.execute("show databases")
#获取指令结果
result = cursor.fetchall()
print(result)

#4.删除数据库
#发送指令
cursor.execute("drop database db3")
conn.commit()

#3.查看数据库
#发送指令
cursor.execute("show databases")
#获取指令结果
result = cursor.fetchall()
print(result)
```

#### 2.6 datagrip的使用

1. 点击+
2. 选择datasource为MySQL
3. 选择root账号登录
4. 连接，应用

## 3. Mysql概述

### 3.1数据库相关概念

| 名称           | 全称                                                         | 简称                             |
| -------------- | ------------------------------------------------------------ | -------------------------------- |
| 数据库         | 存储数据的厂库，数据是有组织地进行存储                       | database(DB)                     |
| 数据库管理系统 | 操作和管理数据库的大型软件                                   | Database Management System(DBMS) |
| SQL            | 操作==关系型==数据库的编程语言，定义了一套操作关系数据库统一==标准== | Structured Query Language(SQL)   |

SQL操作数据库管理系统从而来操控数据库中的数据。

- 客户端连接

​			方式1：Mysql提供的客户端命令行工具

​			方式2：window系统自带的命令行工具执行指令

​						`mysql [-h：指定连接ip] [-p:指定连接端口] -u root -p`

​						==使用此种方式必须配置环境变量==：配置环境变量找到bin目录的地址

### 3.2 Mysql数据库

- 关系型数据库(RDBMS)

> 概念：建立在关系模型基础上，有多张表相互连接的二维表组成的数据库
>
> 特点：
>
> 1. 使用表存储数据，格式统一，便于维护
> 2. 使用SQL语言操作，标准统一，使用方便

- 数据模型(如何存储数据)

> SQL操作数据库管理系统从而来操控数据库中的数据.

## 4.SQL（==核心重点==）

- SQL 分类

| 分类 |            全称            |                        说明                        |
| :--: | :------------------------: | :------------------------------------------------: |
| DDL  |  Data Definition Language  | 数据定义语言，用来定义数据库对象(数据库，表，字段) |
| DML  | Data Manipulation Language |   数据操作语言，用来对数据库表中的数据进行增删改   |
| DQL  |    Data Query Languagae    |       数据查询语句，用来查询数据库中表的记录       |
| DCL  |   Data Control Language    |  数据控制语言，用来创建用户，控制数据库的访问权限  |

### 4.1 DDL语句的操作(数据库，表的增删查)

- DDL-数据库操作

> - 查询
>
>   - 查询所有数据库 `SHOW DATABASES;`
>
>   - 查询当前所属数据库：`SELECT DATABASE()`
>
> - 创建
>
>   - 创建数据库：
>   - `CREATE DATABASE [IF NOT EXISTS]数据库名[DEFAULT CHARSET 字符集][COLLATE 排序规则];`
>
> - 删除
>
>   - `DROP DATABASE [IF EXISTE] 数据库名;`
>
> - 使用
>
>   - `USE 数据库名;`==切换数据库==

- DDL-表操作(==进入到当前的数据库==)

查询

> - 查询当前数据库中的所有表
>   - `SHOW TABLES;`
> - 查询表结构
>   - `DESC 表名;`
> - 查询指定表的建表语句
>   - `SHOW CREATE TABLE 表名;`

创建

> - 表的创建
>
>   - ```sql
>     CREATE TABLE 表名(
>     	字段1 字段1类型[COMMENT 字段1注释],
>         字段2 字段2类型[COMMENT 字段2注释],
>         字段3 字段3类型[COMMENT 字段3注释],
>         ...
>         字段n 字段n类型[COMMENT 字段n注释] #字段类型：int varchar 
>     )[COMMENT 表注释];
>     ```

Mysql中的数据类型，主要分为三类：数值类型，字符串类型，日期时间类型。

|    分类    |   类型   | 大小 | 有符号范围 | 无符号范围 |              描述              |
| :--------: | :------: | :--: | :--------: | :--------: | :----------------------------: |
|  数值类型  |   int    |      |            |            |              整数              |
|            |  float   |      |            |            |             浮点数             |
| 字符串类型 |   char   |      |   性能好   |            | 定常字符串（占用字符空间不变） |
|            | varchar  |      |  性能较差  |            | 变长字符串（占用字符空间变化） |
|            |          |      |            |    格式    |              描述              |
|  日期类型  |   date   |  3   |            |   Y-M-D    |             日期值             |
|            |   TIME   |  3   |            |   H-M-S    |         时间值：时分秒         |
|            | datetime |  8   |            |  YMD HMS   |       显示：年月日时分秒       |

- DDL-表操作-修改

​			添加字段：`ALTER TABLE 表名 ADD 字段名 类型(长度)[COMMENT注释][约束];`

​			修改数据类型：`ALTER TABLE 表名MODIFY 字段名 新数据类型(长度);`

​			修改字段名和字段类型

​						`ALTER TABLE 表名 CHANGE 旧字段名 新字段名 类型(长度)[COMMENT注释][约束];`

​			删除字段：`ALTER TABLE 表名 DROP 字段名;`

​			修改表名 `ALTER TABLE 表名 RENAME TO 新表名;`

- DDL-表操作-删除

​			删除表 `DROP TABLE [IF EXISTS] 表名;`

​			删除指定表，并重新创建该表：`TRUNCATE TABLE 表名;`

### 4.2 DML语句的操作（表中数据进行增删改）

对数据库中表的数据进行增删改操作

- 添加数据

> - DML-添加数据
>
>   1. 给指定字段添加数据
>
>   ​		`INSERT INTO 表名 (字段名1,字段名2,...) VALUES(值1,值2,....);`
>
>   2. 给全部字段添加数据
>
>      `INSERT INTO 表名 VALUES(值1,值2,值3,....);`
>
>   3. 批量添加数据
>
>      `INSERT INTO 表名(字段名1,字段名2,...) VALUES(值1,值2,...),(值1,值2,...)...;`
>
>      `INSERT INTO 表名 VALUES(值1,值2,...),(值1,值2,...)...;`
>
> - 注意：
>
>   - 插入数据时，指定的字段顺序需与值的顺序一一对应
>   - 字符串和日期型数据应包含在引号中
>   - 插入数据的大小，应该在字段的规定范围内

- 修改数据

> - DML-修改数据
> - `UPDATE 表名 SET 字段名1=值1,字段名2=值2,....[WHERE 条件];`
> - 注意：修改语句的条件可以有，也可以没有，如果没有条件，则会修改整张表的所有数据。

- 删除数据

> `DELECT FROM 表名[WHERE条件]`
>
> - 注意
>   - delect语句条件可以有，也可以没有，如果没有条件，会删除整张表的所有数据
>   - delect语句不能删除某一字段的值（可以用update删除）

### 4.3 DQL语句的操作(查询语句)

==数据查询语言，用来查询数据库中表的记录。关键字select==

==执行顺序：where > 聚合函数 >having==

分组之后，查询的字段一般为聚合函数和分组字段，查询其他字段无任何意义

- DQL-语法

  ```sql
  SELECT
  	字段列表
  FROM
  	表名列表
  WHERE
  	条件列表
  GROUP BY
  	分组字段列表
  HAVING
  	分组后条件列表
  ORDER
  	排序字段列表
  LIMIT
  	分页参数
  ```

##### 4.3.1基本查询(select...from...)

1. 查询多个字段

​		`SELECT 字段1,字段2,字段3,...FROM 表名;`

​		`SELECT * FROM 表名;`

2. 设置别名

​		`SELECT 字段1[AS 别名1],字段2[AS别名2]...FROM 表名;`起别名：增加可读性

3. 去除重复记录

​		`SELECT DISTINCT 字段列表 FROM 表名;`

##### 4.3.2条件查询(WHERE)

> - 语法
>   - `SELECT 字段列表 FROM 表名 WHERE 条件列表;`
> - 条件
>
> |    比较运算符    |                    功能                    | 逻辑运算符 | 功能 |
> | :--------------: | :----------------------------------------: | ---------- | ---- |
> |        >         |                    大于                    | AND或&&    | 与   |
> |        >=        |                  大于等于                  | or或\|\|   | 或   |
> |        <         |                    小于                    | not或！    | 非   |
> |        <=        |                  小于等于                  |            |      |
> |        =         |                    等于                    |            |      |
> |      !=或<>      |                   不等于                   |            |      |
> |     IN(...)      |        在IN之后的列表中的值，多选一        |            |      |
> | BETWEEN...AND... |       在某个范围之内(含最小，最大值)       |            |      |
> |    LIKE占位符    | 模糊匹配(_匹配单个字符，%匹配人任意个字符) |            |      |
> |     IS NULL      |                   是NULL                   |            |      |

##### 4.3.3聚合函数(count,max,min,avg,sum)

> 1. 介绍：将一列数据作为一个整体，进行纵向计算。
>
> 2. 常见的聚合函数
>
>    | 函数  |   功能   |
>    | :---: | :------: |
>    | count | 统计数量 |
>    |  max  |  最大值  |
>    |  min  |  最小值  |
>    |  avg  |  平均值  |
>    |  sum  |   求和   |

       3. 语法

​		`SELECT 聚合函数(字段列表) FROM 表名;`

​        ==所有的NULL值不参与聚合函数的运算==

##### 4.3.4 分组查询(GROUP BY)

通常配合着聚合函数来使用

> 1. 语法：`SELECT 字段列表 FROM 表名[WHERE 条件]GROUP BY 分组字段名[HAVING 分组后过滤条件];`
> 2. where 与 having区别
>    - 执行时机不同：where是分组之前进行过滤，不满足where条件，不参与分组；而having是分组之后对结果进行过滤
>    - 判断条件不同：where不能对聚合函数进行判断，而having可以。

例子:

> - 根据性别分组，统计男性员工和女性员工的数量
>
>   `select gender,count(*) from emp group by gender;`
>
> - 根据性别分组，统计男性员工和女性员工的平均年龄
>
>   `select gender,avg(age) from emp group by gender;`
>
> - 查询年龄小于45的员工，并根据工作地址分组，获取员工数量大于等于3的工作地址
>
>   `select workaddress,count(*) as address_count from emp where age<45 group by workaddress having address_count >= 3;`分组之后再次过滤用having

##### 4.3.5 排序查询(ORDER BY)

> - 语法
>   - `SELECT 字段列表 FROM 表名 ORDER BY 字段1 排序方式1,字段2 排序方式2;`
> - 排序方式
>   - ASC:升序(默认值)
>   - DESC:降序
>   - ==如果是多字段排序，当第一个字段值相同时，才会根据第二个字段进行排序。==
> - 例子：
>   - 根据年龄对公司的员工进行升序排序
>     - `SELECT * FROM emp ORDER BY AGE ASC;`
>   - 根据年龄对公司的员工进行升序排序，年龄相同，再按照入职时间进行降序排序(黄色)
>     - `select * from emp order by age asc, entrydate desc; `

##### 4.3.6 分页查询(LIMIT)

> - 语法
>   - `select 字段列表 from 表名 limit 起始索引,查询记录数;`
> - 注意
>   - 起始索引从0开始，起始索引=(查询页码-1)*每页显示记录数。
>   - 分页查询是数据库的方言，不同数据库有不同的实现，Mysql中是LIMIT
>   - 如果查询的是第一页数据，起始索引可以省略，直接写为limit10.
> - 例子
>   - 查询第1页员工数据，每条展示10条记录
>     - `select * from emp limit 0,10;`
>   - 查询第2页员工数据，没有展示10条记录
>     - `select * from emp limit 10,10;`

##### 4.3.7 总结习题练习

> - 查询年龄为20，21，22，23女性员工的信息
>   - `select * from emp where gender='女'and age in(20,21,22,23);`
> - 查询性别为男，并且年龄在20-40岁(含)以内的姓名为三个字的员工，
>   - `select * from emp where gender='男' and age (between 20 and 40) and  name like '___'; `
> - 统计员工表中，年龄小于60岁的，男性员工和女性员工的人数。
>   - `select gender，count(*) from emp where age < 60 group by gender;`
> - 查询所有年龄小于等于35岁员工的姓名和年龄，并对查询结果按年龄升序排序，如果年龄相同按入职时间降序排序。
>   - `select name,age from emp where age <35 order by age asc,entrydate desc;`
> - 查询性别为男性，且年龄在20-40岁(含)以内的钱5个员工信息，对查询的结果按升序排序，年龄相同按入职时间升序排序。
>   - `select * from emp where gender='男'and age between 20 and 40  order age asc,entrydate asc limit 5 ;`

##### 4.3.8 DQL语句执行顺序

<img src="D:\Photo\QQ图片20231031173609.jpg" style="zoom: 33%;" />

##### 4.3.9 DQL语句的总结

<img src="D:\Photo\QQ图片20231031174008.jpg" style="zoom:33%;" />

### 4.4 DCL语句的操作(用户权限)

DCL是用来管理数据库用户，控制数据库的访问权限

1. 主要控制数据库有哪些用户可以访问
2. 控制每一个用户具有什么样的访问权限

#### 4.4.1 DCL-管理用户

> 1. 查询用户
>
>    `USE mysql;`
>    `SELECT * FROM user;`
>
> 2. 创建用户
>
>    `CREATE USER '用户名'@'主机名' IDENTIFIEND BY '密码';`
>
> 3. 修改用户密码
>
>    `ALTER USER '用户名'@'主机名' IDENTIFIED WITH mysql_native_password BY '新密码';`
>
> 4. 删除用户
>
>    `DROP USER '用户名'@'主机名';`

例子：

> 1. 创建用户xulei，可以在任意主机上访问该数据库，密码为‘123456’.使用通配符%
>
>    `create user 'xulei'@'%' identified by '123456';`
>
> 2. 修改用户xulei的访问密码为1234
>
>    `alter user 'xulei'@'%' identified with mysql_native_password by '1234';`
>
> 3. 删除itcast@localhost用户
>
>    `drop user 'itcast'@'localhost';`
>
> 注意：
>
> ​	==主机名可以使用%通配==
>
> ​	==这类SQL开发人员操作的比较少，主要是DBA（数据库管理员）使用。==

#### 4.4.2 DCL权限控制

|        权限        |          说明          |
| :----------------: | :--------------------: |
| ALL,ALL PRIVILEGES |        所有权限        |
|       SELECT       |      查询数据权限      |
|       INSERT       |      插入数据权限      |
|       UPDATE       |      修改数据权限      |
|       DELECT       |      删除数据权限      |
|       ALTER        |    修改表/字段权限     |
|        DROP        | 删除数据库/表/试图权限 |
|       CREATE       |   创建数据库/表权限    |

> 1. 查询权限
>
>    `SHOW GRANTS FOR '用户名'@'主机名';`
>
> 2. 授予权限
>
>    `GRANT 权限列表 ON 数据库名.表名 TO '用户名'@'主机名';`
>
> 3. 撤销权限
>
>    `REVOKE 权限列表 ON 数据库名.表名 FROM '用户名'@'主机名';`

例子

> 1. -- 查询权限
>
>    `show grants for 'xulei'@'%';`
>
> 2. -- 授予权限
>
>    ``

## 5.函数

### 5.1字符串函数

Mysql中内置了很多字符串函数，常用的几个如下：

|           函数           |                            功能                             |
| :----------------------: | :---------------------------------------------------------: |
|   CONCAT(S1,S2,...Sn)    |         字符串拼接，将S1,S2,...,Sn拼接成一个字符串          |
|        LOWER(str)        |                  将字符串str全部转换为小写                  |
|        UPPER(str)        |                  将字符串str全部转换为大写                  |
|     LPAD(str,n,pad)      |  左填充，用字符串pad对str的左边进行填充，达到n个字符串长度  |
|     RPAD(str,n,pad)      |  右填充，用字符串pad对str的右边进行填充，达到n个字符串长度  |
|        TRIM(str)         |                 去掉字符串头部和尾部的空格                  |
| SUBSTRING(str,start,len) | 返回从字符串str从start位置起的len个长度的字符串(字符串截取) |

例子

```python
select concat('李四','我爱你'); #李四我爱你
select lower('Hello'); #hello
select lpad('hi',5,'_'); #___hi
select trim(' hello mysql '); #hello mysql
select substring('hello',1,3); #hel
```

### 5.2数值函数

|    函数    |               功能               |
| :--------: | :------------------------------: |
|  CEIL(x)   |             向上取整             |
|  FLOOR(x)  |             向下取整             |
|  MOD(x,y)  |   返回x/y的模(x/y的余数是什么)   |
|   RAND()   |        返回0-1内的随机数         |
| ROUND(x,y) | 求参数x的四舍五入的值，保留y小数 |

案例：通过数据库函数，生成一个六位数的随机验证码

```python
select lpad(round(rand()*1000000,0),6,0);
```

### 5.3日期函数

常见的日期函数：

|               函数                |                       功能                        |
| :-------------------------------: | :-----------------------------------------------: |
|             CURDATR()             |                   返回当前日期                    |
|             CURTIME()             |                   返回当前时间                    |
|               NOW()               |                返回当前日期和时间                 |
|            YEAR(date)             |                获取指定date的年份                 |
|            NONTH(date)            |                获取指定date的月份                 |
|             DAY(date)             |                获取指定date的日期                 |
| ADTE_ADD(date,INTERVAL expr type) | 返回一个日期/时间值加上一个时间间隔expr后的时间值 |
|       DATEDIFF(date1,date2)       |    返回起始时间date1和结束时间date2之间的天数     |

例子：

```python
select curdate();
select curtime();
select  now();
select year(now());
select month(now());
select day(now());
select date_add(now(),interval 70 day);
select datediff('2021-11-2','2023-12-5');#第一个时间减去第二个时间
```

案例：查询所有员工的入职天数，并根据入职天数倒序排序

```python
select  name,datediff(curdate(),entrydate) as entrydays from emp  order by  entrydays desc;
```

### 5.4流程函数

流程函数也是很常用的一类函数，可以在SQL语句中实现条件筛选，从而提高语句的效率

|                          函数                           |                          功能                           |
| :-----------------------------------------------------: | :-----------------------------------------------------: |
|                      IF(value,t,f)                      |           如果value为true，则返回t,否则返回f            |
|                  IFNULL(value1,value2)                  |       如果value1不为空，返回value1,否则返回value2       |
|   CASE WHEN [val1] THEN [res1] ...ELSE [default] END    |    如果vall为true,返回res1,...否则返回default默认值     |
| CASE [expr] WHEN [val1] THEN [res1]...ELSE[default] END | 如果expr的值等于vall,返回res1,....否则返回default默认值 |

例子

```python
select if(true,1,2); #第一个是一个条件表达式
select ifnull('ok','Default'); #判断第一个值是否为空，不为空返回ok否则返回Default
select ifnull(null,'Default'); #Default
 -- case when then else end
# 需求：查询emp表格的员工姓名和工作地址(北京/上海--->一线城市，其它---->二线城市)
select
    name,
    (case workadress when '北京' then '一线城市' when '上海' then '一线城市' else '二线城市' end) as '工作地址'
from emp;
```

### 5.5总结

1. 字符串函数

`CONCAT,LOWER,UPPER,LPAD,RPAD,SUBSTRING`

2. 数值函数

   `CEIL, FLOOR,MOD,RAND,ROUND`

3. 日期函数

`CURDATE,CURTIME,NOW,YEAR,DATE_ADD,DATEDIFF`

4. 流程函数

`IF(VALUE,T,F)`

## 6.约束

### 6.1概念

- 概念：约束是作用于表中字段上的规则，用于限制存储在表中的数据。
- 目的：保证数据库中数据的准确性，有效性和完整性
- 分类：

|   约束   |                           描述                           |   关键字    |
| :------: | :------------------------------------------------------: | :---------: |
| 非空约束 |                限制该字段的数据不能为null                |  NOT NULL   |
| 唯一约束 |         保证该字段的所有数据都是唯一的，不重复的         |   UNIQUE    |
| 主键约束 |         主键是一行数据的唯一标识，要求非空且唯一         | PRIMARY KEY |
| 默认约束 |      保存数据时，如果未指定该字段的值，则采用默认值      |   DEFAULT   |
| 检查约束 |                  保证字段满足某一个条件                  |    CHECK    |
| 外键约束 | 用来让两张表的数据之间建立连接，保证数据的一致性和完整性 | FOREIGN KEY |

==约束是作用于表中字段上的，可以在创建表/修改表的时候添加约束==

### 6.2约束演示

根据需求，完成表结构的创建

| 字段名 |   字段含义   |  字段类型   |         约束条件          |            约束关键字            |
| :----: | :----------: | :---------: | :-----------------------: | :------------------------------: |
|   id   | ID唯一标识符 |     int     |    主键，并且自动增长     | PRIMARY KEY,<br />AUTO_INCREMENT |
|  name  |     姓名     | varchar(10) |     不为空，并且唯一      |          NOTNULL,UNIQUE          |
|  age   |     年龄     |     int     |  大于0，并且小于等于120   |              CHECK               |
| status |     状态     |   char(1)   | 如果没有指定该值，默认为1 |             DEFAULT              |
| gender |     性别     |   char(1)   |            无             |                                  |

演示：

```sql
create table user(
    id int primary key auto_increment comment '主键',
    name varchar(10) not null  unique comment '姓名',
    age int check ( age > 0 and age <= 120 ) comment '年龄',
    status char(1) default '1' comment '状态',
    gender char(1) comment '性别'

)comment '用户表';
```

### 6.3外键约束

- 概念：外键约束用来让两张表的数据建立连接，从而保证数据的一致性和完整性
- <img src="D:\Photo\QQ图片20231104112202.jpg" style="zoom:43%;" />*

### 6.4添加外键语法

- 添加外键语法
- 语法1

```sql
create table 表名(
    字段名 数据类型
    ...
    [constraint] [外键名称] foreign key(外键字段名) references 主表(主表列表)
);
```

- 语法2

```sql
ALTER TABLE 表名 ADD CONSTRAINT 外键名称 FOREIGN KEY(外键字段名) REFERENCES 主表(主表列名);

alter table enployment add constraint fk_enp_dept_id foreign key (dept_id) references dept(id);
```

### 6.5 删除外键

```python
ALTER TABLE 表名 DROP FOREIGN KEY 外键名称;
```

### 6.6 外键约束的删除/更新行为

- 删除/更新行为

|    行为     |                             说明                             |
| :---------: | :----------------------------------------------------------: |
|  NO ACTION  | 当在父表中删除/更新对应记录时，首先检查该记录是否有对应外键，如果有则不允许删除/更新。(与RESTRICT一致) |
|  RESTRICT   | 当在父表中删除/更新对应记录时，首先检查该记录是否有对应外键，如果有则不允许删除/更新。(与NO ACTION一致) |
|   CASCADE   | 当在父表中删除/更新对应记录时，首先检查该记录是否有对应外键，如果有,则也删除/更新外键在子表中的记录。 |
|  SET NULL   | 当在父表中删除对应记录时，首先检查该记录是否有对应外键，如果有则设置子表中该外键值为NULL(这就要求该外键允许去null) |
| SET DEFAULT |  父表有变更时，子表将外键列设置成一个默认的值(innodb不支持)  |

`alter table 表名 add constraint 外键名称 foreign key(外键字段) references 主表名(主表字段名) on update cascade on delete cascade; `

## 7.多表查询

### 7.1多表关系

- 概述：表结构之间存在着各种联系，基本分为三种：

		1. 一对多（多对一）
		1. 多对多
		1. 一对一

- 一对多(多对一)

> 案例：部门与员工的关系
>
> 关系：一个部门对应多个员工，一个员工对应一个部门
>
> 实现：==在多的一方建立外键，指向一的一方的主键==

- 多对多

> 案例：学生与课程的选择
>
> 关系：一个学生可以选择多门课程，一门课程也可以供多个学生选择
>
> 实现:==建立第三方中间表，中间表至少包含两个外键，分别关联两方主键==
>
> <img src="D:\Photo\QQ图片20231104144919.jpg" style="zoom:43%;" />

==软件展示多表之间的关系：点击中间表，右键，选择diagrams(示意图)，选择show diagrams==

- 一对一

> 案例：用户与用户详情的关系
>
> 关系：一对一的关系，多用于单表的拆分，将一张表的基础字段放在一张表中，其他详情字段放在另一张表中，以提升操作效率。
>
> 实现：==在任意的一方加入外键，关联另一方的主键，并且设置外键为唯一的(UNIQUE)==

### 7.2多表查询概述

- 概述：指的是从多张表中查询数据

- 语法

  ```sql
   -- 多表查询--笛卡尔积
   select * from 表1,表2; --会产生笛卡尔积
   -- 笛卡尔积：笛卡尔积是指在数学中，两个集合A和集合B的所有组合情况。(在多表查询时，需要消除无效的笛卡尔积)结果A,B
   
   -- 消除无效的笛卡尔积：观察两张表是通过哪个字段建立联系的。
   select * from emp,dept where emp.dept_id = dept.id;
  ```

### 7.3 多表查询分类

#### 7.3.1 连接查询

##### 内连接

==内连接相当于查询A,B交集的部分==

- 隐式内连接
  - 语法结构：`select 字段列表 from 表1,表2 Where 条件....;`
    - 找表结构，那两张表
    - 找连接条件，消除笛卡尔积
  - 例子：查询每一个员工的姓名，以及关联的部门的名称(隐式内连接实现)
  - `select emp.name,dept.name from dept,emp where dept.id  = emp.dept_id;`
- 显式内连接
  - 语法结构：`select 字段列表 from 表1[INNER] Join 表2 连接条件...;`

##### 外连接

==左外连接：查询左表所有数据，以及两张表交集部分数据==

==右外连接：查询右表所有数据，以及两张表交集部分数据。==

##### 自连接

==当前表与自身的连接查询，自连接必须使用表别名。==

#### 7.3.2子查询

### 7.4多表查询案例

## 8.事务（==保证安全==）3
