import json

info = {'k1':123,'k2':(11,22,33,44)}
res = json.dumps(info)
print(res) #{"k1": 123, "k2": [11, 22, 33, 44]}
