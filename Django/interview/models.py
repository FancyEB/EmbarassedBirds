# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from datetime import datetime
from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

#This is REST API area
class Sprint(models.Model):
    name = models.CharField(max_length=100,blank=True,default="")
    description = models.TextField(blank=True,default="")
    end = models.DateField(unique=True)

    def __str__(self):
        return self.name or _('Sprint ending %s') % self.end

class Task(models.Model):
    STATUS_TODO = 1
    STATUS_IN_PROGRESS = 2
    STATUS_TESTING = 3
    STATUS_DONE = 4

    STATUS_CHOICES = (
        (STATUS_TODO,_('Not Started')),
        (STATUS_IN_PROGRESS,_('In Progress')),
        (STATUS_TESTING,_('Testing')),
        (STATUS_DONE,_('Done')),
    )

    name = models.CharField(max_length=100)
    description = models.TextField(blank=True,default='')
    sprint = models.ForeignKey(Sprint,blank=True,null=True)
    status = models.SmallIntegerField(choices=STATUS_CHOICES,default=STATUS_TODO)
    order = models.SmallIntegerField(default=0)
    # assigned = models.ForeignKey(settings.USE,null=True,blank=True)  # what is this
    started = models.DateField(blank=True,null=True)
    completed = models.DateField(blank=True,null=True)

    def __str__(self):
        return self.name


#API setting End here
class User(models.Model):
    """
    用户表
    """
    username = models.CharField(verbose_name="名称", max_length=50)
    password = models.CharField(verbose_name="密码", max_length=256)
    email = models.EmailField(verbose_name="邮箱", max_length=50)
    mobile = models.CharField(verbose_name="手机号", max_length=11)
    wechat = models.CharField(verbose_name="微信号", max_length=11, blank=True, null=True)
    gen = (
        ("male", "男"),
        ("female", "女")
    )
    gender = models.CharField(verbose_name="性别", choices=gen, default="male", max_length=10)
    image = models.ImageField(verbose_name="头像", upload_to="users/%Y/%m", blank=True, null=True)

    class Meta:
        verbose_name = "用户表"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.username


class Proof(models.Model):
    """
    凭证
    """
    secretCode = models.CharField(verbose_name="随机码", max_length=100)  # 凭证 (问卷api?凭证=3561656156diusfhjdscudfhns)
    pid = models.IntegerField(verbose_name="问卷ID")
    mid = models.IntegerField(verbose_name="当前题目ID")

    class Meta:
        verbose_name = "凭证表"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.secretCode


class Paper(models.Model):
    """
    问卷
    """
    pid = models.CharField(verbose_name="问卷ID", max_length=20)
    name = models.ForeignKey(User,verbose_name="提问人")
    title = models.CharField(verbose_name="问卷名", max_length=50, default="-")
    buildTime = models.DateTimeField(verbose_name="创建时间", default=datetime.now)

    class Meta:
        verbose_name = "问卷"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.pid


class Topic(models.Model):
    """
    题目
    """
    mid = models.CharField(verbose_name="题目ID", max_length=20)
    pid = models.ForeignKey(Paper, verbose_name="问卷ID")
    text = models.TextField(verbose_name="题目内容", max_length=500)
    file = models.FileField(verbose_name="上传文件", upload_to="files/%Y/%m", blank=True, null=True)
    answers = models.CharField(verbose_name="选项", max_length=300)  # 包括多个选项

    class Meta:
        verbose_name = "题目"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.mid

