from flask import Flask, render_template, request
import pymysql
import os
from dotenv import load_dotenv

# 加载环境变量
load_dotenv()

app = Flask(__name__)


def init_db():
    conn = pymysql.connect(
        host=os.getenv('DB_HOST', '127.0.0.1'),
        port=int(os.getenv('DB_PORT', 3306)),
        user=os.getenv('DB_USER', 'root'),
        password=os.getenv('DB_PASSWORD', 'xu938374'),
        charset="utf8",
        db=os.getenv('DB_NAME', 'employee')
    )
    cursor = conn.cursor()
    create_table_sql = """
    CREATE TABLE IF NOT EXISTS user (
        id INT AUTO_INCREMENT PRIMARY KEY,
        username VARCHAR(255) NOT NULL,
        password VARCHAR(255) NOT NULL,
        mobile VARCHAR(20) NOT NULL
    );
    """
    cursor.execute(create_table_sql)
    conn.commit()
    cursor.close()
    conn.close()


@app.route("/add/user", methods=["GET", "POST"])
def adduser():
    if request.method == 'GET':
        return render_template("02-adduser.html")

    if request.method == 'POST':
        try:
            username = request.form.get("user")
            password = request.form.get("pwd")
            mobile = request.form.get("mobile")

            # 连接Mysql
            sql = "INSERT INTO user (username, password, mobile) VALUES (%s, %s, %s)"
            conn = pymysql.connect(
                host=os.getenv('DB_HOST', '127.0.0.1'),
                port=int(os.getenv('DB_PORT', 3306)),
                user=os.getenv('DB_USER', 'root'),
                password=os.getenv('DB_PASSWORD', 'xu938374'),
                charset="utf8",
                db=os.getenv('DB_NAME', 'employee')
            )
            cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

            # 执行SQL
            cursor.execute(sql, [username, password, mobile])
            conn.commit()

        except pymysql.MySQLError as e:
            return f"Database error: {str(e)}"
        except Exception as e:
            return f"Error: {str(e)}"
        finally:
            # 关闭连接
            cursor.close()
            conn.close()

        return "添加成功"

@app.route("/show/user")
def show_user():

     # 从数据库获取所有的用户信息

    #1.连接mysql
    conn = pymysql.connect(host="127.0.0.1",port=3306,user="root",password="xu938374",charset="utf8",db='employee')
    # 基于cursor发送接收数据
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

    #2.发送指令
    sql = "select * from admin"
    cursor.execute(sql)
    data_list = cursor.fetchall()

    #3.关闭
    cursor.close()
    conn.close()

    print(data_list)
    return render_template("show_user.html",data_list=data_list)

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
