from django.db import models


# Create your models here.

class CRUD_DataBase(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.IntegerField()
    password = models.CharField(max_length=16)
    datatime = models.DateTimeField(auto_now=True)





