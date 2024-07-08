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