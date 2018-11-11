# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from models import User, Proof, Paper, Topic
from django.contrib import admin


# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ("username","email","gender",)
    list_filter = ("username",)
    search_fields = ("username",)



class ProofAdmin(admin.ModelAdmin):
    pass


class PaperAdmin(admin.ModelAdmin):
    list_display = ("name","pid","title",)
    list_filter = ("pid",)


class TopicAdmin(admin.ModelAdmin):
    search_fields = ("pid",)

admin.site.register(User,UserAdmin)
admin.site.register(Proof,ProofAdmin)
admin.site.register(Paper,PaperAdmin)
admin.site.register(Topic,TopicAdmin)