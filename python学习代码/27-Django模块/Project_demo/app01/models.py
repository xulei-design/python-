from django.db import models


class Admin(models.Model):
    """管理员表"""
    username = models.CharField(verbose_name="用户名", max_length=16)
    password = models.CharField(verbose_name="密码", max_length=64)


class DepartMent(models.Model):
    """部门表"""
    title = models.CharField(verbose_name="标题", max_length=16)

    def __str__(self):
        return '{}-{}'.format(self.id, self.title)


class AssetSet(models.Model):
    """资产表"""
    name = models.CharField(verbose_name="名称", max_length=32)
    price = models.IntegerField(verbose_name="价格")
    # 只适用于固定的选择
    category_choices = ((1, '办公类'), (2, "3C类"), (3, "房产类"))
    category = models.SmallIntegerField(verbose_name="资产类型", choices=category_choices)

    # 创建外键,在数据库生成的字段名depart_id on_delete=models.CASCADE:级联删除
    depart = models.ForeignKey(verbose_name="所属部门", to="DepartMent", to_field="id", on_delete=models.CASCADE)


class Staff(models.Model):
    """员工表"""
    name = models.CharField(verbose_name="姓名", max_length=16)
    mobile = models.CharField(verbose_name="手机号",max_length=11)
    email = models.EmailField(verbose_name="邮箱", max_length=64)
    gender = models.SmallIntegerField(verbose_name="性别", choices=((1, '男'), (2, "女")))
    # 创建外键
    depart = models.ForeignKey(verbose_name="所属部门", to="DepartMent", to_field="id", on_delete=models.CASCADE)
