from datetime import date
import django.utils.timezone as timezone

from django.db import models


# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=128, verbose_name="用户名")
    password = models.CharField(max_length=128, verbose_name="密码")
    email = models.EmailField(max_length=128, verbose_name="邮箱")

    def __str__(self):
        return self.username


class Task(models.Model):
    level_choices = (
        (0, ""),
        (1, "紧急"),
        (2, "临时"),
        (3, "重要"),
    )
    level = models.SmallIntegerField(verbose_name="任务级别", choices=level_choices, default=1)
    title = models.CharField(verbose_name="任务标题", max_length=64)
    detail = models.TextField(verbose_name="任务详细信息")
    user = models.ForeignKey(verbose_name="负责人", to="User", on_delete=models.CASCADE)
    createtime = models.DateTimeField(default=timezone.now)