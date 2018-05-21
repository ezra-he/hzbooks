# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import django.utils.timezone as timezone

# Create your models here.

class books(models.Model):
    # id = models.IntegerField(primary_key=True,default=1)  # 主键自增id
    uuid = models.CharField(max_length=32,blank=True,null=True)  # 图书的uuid
    name = models.CharField(max_length=32,blank=True,null=True)  # 图书名
    introduction = models.CharField(max_length=256,blank=True,null=True)  # 简介
    author = models.CharField(max_length=32,blank=True,null=True)  # 作者
    comment = models.CharField(max_length=256,blank=True,null=True)  # 评论
    scan = models.IntegerField(default=0)  # 点击量
    photo = models.CharField(max_length=32,blank=True,null=True)  # 图片
    status = models.CharField(max_length=16,default='normal')  # 状态
    update_time = models.DateTimeField(blank=True,null=True,auto_now=True)  # 图书更新时间
    build_time = models.DateTimeField(blank=True,null=True,default=timezone.now())  # 图书上架时间
