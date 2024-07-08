import csv
file = open('test.csv','w')
writer = csv.writer(file)
writer.writerow(['name', 'age', 'score'])
writer.writerows([['zhangsan', '18', '98'],['lisi', '20', '99'], ['wangwu', '17', '90'], ['jerry', '19', '95']])
file.close()



from io import StringIO
f = StringIO()
f.write('hello\r\n')
f.write('good')
print(f.getvalue())
f.close()
