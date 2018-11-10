# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import View

from models import Topic  # 导入model 中的题目数据类
# Create your views here.
# RESTful api setting START HERE
from django.contrib.auth import  get_user_model
from rest_framework import viewsets,authentication,permissions
from .models import Sprint,Task
from .serializers import SprintSerializer,TaskSerializer,UserSerializer

User = get_user_model()

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    lookup_field = User.USERNAME_FIELD
    lookup_url_kwarg = User.USERNAME_FIELD
    queryset = User.objects.order_by(User.USERNAME_FIELD)
    serializer_class = UserSerializer

class DefaultsMixin(object):
    authentication_classes = (
        authentication.BasicAuthentication,
        authentication.TokenAuthentication,
    )
    permissions_classes = (
        permissions.IsAuthenticated,
    )
    paginate_by = 25
    paginate_by_param = 'page_size'
    max_paginate_by = 100

class SprintViewSet(viewsets.ModelViewSet):
    queryset = Sprint.objects.order_by('end')
    serializer_class = SprintSerializer

# RESTful api setting END HERE



class InterListView(View):
    def get(self, request):
        all_Topic = Topic.objects.all()  # 获取所有题目对象(列表)
        return render(request, "interview_list.html", {
            "all_Topic": all_Topic,    # 传递模板变量给模板文件
        })
