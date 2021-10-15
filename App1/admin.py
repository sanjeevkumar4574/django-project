from django.contrib import admin
from django.db import models
from .models import CRUD_DataBase


# Register your models here.
class CURD_Admin(admin.ModelAdmin):
    list_display = ['id','name','email','phone','password']


admin.site.register(CRUD_DataBase,CURD_Admin)