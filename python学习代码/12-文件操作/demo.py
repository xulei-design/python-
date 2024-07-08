#导入json模块
import json
#准备好符合格式要求的python数据
data = [{"name":"admin","age":18},{"name":"zhangsan","age":20}]
#通过json.dump(data)方法将python数据转化为json数据
data = json.dumps(data)
print(f"转化过后的python数据，得到json数据{data}")

#通过json.loads(data)方法把json数据转化为python数据
data = json.loads(data)
print(f"转化过后的json数据，得到python数据{data}")