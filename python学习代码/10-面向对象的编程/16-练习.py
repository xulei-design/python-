class Pagintation:
    def __init__(self,current_page,per_page_num=10):
        self.per_page_num = per_page_num
        self.current_page = current_page
        #判断页码是否是数字
        if not current_page.isdecimal():
            self.current_page = 1
            return
        current_page = int(current_page)
        if current_page < 1:
            self.current_page = 1
            return
        self.current_page = current_page
        #以上对不符合规格的数据进行处理
    def start(self):
        """
        计算起始索引
        :return:
        """
        return (self.current_page - 1) * self.per_page_num
    def end(self):
        """
        计算结束索引
        :return:
        """
        return self.current_page * self.per_page_num

user_list = [f"用户-{i}" for i in range(1,3000)]

#分页显示，每页显示10条
while True:
    page = input("请输入页码:")
    #page，当前访问页面码
    #10，每页显示10条数据
    #内部执行Pagination类的init方法。
    pg_object = Pagintation(page,10)
    page_data_list = user_list[pg_object.start():pg_object.end()]
    for item in page_data_list:
        print(item)