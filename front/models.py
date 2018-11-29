from django.db import models
from django.core import validators
# Create your models here.
class HostInfo(models.Model):
    username = models.CharField(max_length=8)
    host = models.CharField(max_length=16,validators=[validators.RegexValidator(r'[ABC]-\d{1}-\d{4}$',message='格式错误，示例：B-1-0195')])
    displayer = models.CharField(max_length=16,validators=[validators.RegexValidator(r'[ABC]-\d{1}-\d{4}$',message='格式错误，示例：B-1-0195')])
    mem = models.CharField(max_length=2)
    cpu = models.CharField(max_length=16)
    ip_addr = models.CharField(max_length=30,validators=[validators.RegexValidator(r"\d{2,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$",message='格式错误，示例：192.168.24.30')])
    dep = models.ForeignKey('Department',on_delete=models.CASCADE)
    add_time = models.DateTimeField(auto_now_add=True)
    comment = models.TextField(null=True,blank=True)
class Department(models.Model):
    dep_name = models.CharField(max_length=20)