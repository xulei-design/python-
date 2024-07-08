from django.db import models

# Create your models here.

#app01_userinfo
class UserInfo(models.Model):
    username = models.CharField(verbose_name="用户名",max_length=16)
    password = models.CharField(verbose_name='密码',max_length=64)
    age = models.IntegerField(verbose_name="年龄")

class Role(models.Model):
    title = models.CharField(verbose_name='标题',max_length=16)
    count = models.IntegerField(verbose_name="个数")