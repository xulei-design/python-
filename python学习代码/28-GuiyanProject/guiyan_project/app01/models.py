from django.db import models


# Create your models here.

class DepartMent(models.Model):
    """部门表"""
    title = models.CharField(verbose_name="标题", max_length=16)
