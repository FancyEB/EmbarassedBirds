# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.
class User(models.Model):
    """
    用户表
    """
    username = models.CharField(verbose_name="名称", max_length=50)
    password = models.CharField(verbose_name="密码", max_length=256)
    email = models.EmailField(verbose_name="邮箱", max_length=50)
    mobile = models.IntegerField(verbose_name="手机号", max_length=11)
    wechat = models.CharField(verbose_name="微信号", max_length=11, blank=True, null=True)
    gen = (
        ("male", "男"),
        ("female", "女")
    )
    gender = models.CharField(verbose_name="性别", choices=gen, default="male")
    image = models.ImageField(verbose_name="头像", upload_to="users/%Y/%m", blank=True, null=True)


class Proof(models.Model):
    """
    凭证
    """
    pid = models.IntegerField(verbose_name="问卷ID", max_length=50)
    mid = models.IntegerField(verbose_name="当前题目ID", max_length=50)


class Paper(models.Model):
    """
    问卷
    """
    pid = models.IntegerField(verbose_name="问卷ID", max_length=50)
    name = models.CharField(verbose_name="提问人ID",max_length=50)
    title = models.CharField(verbose_name="问卷名",max_length=50,default="-")


class Topic(models.Model):
    """
    题目
    """
    mid = models.IntegerField(verbose_name="题目ID", max_length=50)
    pid = models.ForeignKey(Paper,verbose_name="问卷ID")
    text = models.TextField(verbose_name="题目内容", max_length=500)
    file = models.FileField(verbose_name="上传文件", upload_to="files/%Y/%m",blank=True,null=True)
    answers = models.CharField(verbose_name="选项", max_length=300)  #包括多个选项
