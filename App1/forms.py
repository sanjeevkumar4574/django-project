from django import forms
from django.db.models.base import Model
from django.forms import fields, widgets
from django.forms.models import  ModelForm
from App1.models import CRUD_DataBase


class StudentRegistration(ModelForm):
    class Meta:
        model = CRUD_DataBase
        exclude = ['datetime']

        widgets = {'password':forms.PasswordInput(attrs={'class':'form-control'}),
        'name':forms.TextInput(attrs={'class':'form-control'}),
        'email':forms.EmailInput(attrs={'class':'form-control'}),
        'phone':forms.NumberInput(attrs={'class':'form-control'})
        } 
        
        # error_messages = {
        #     'name':'Enter Your Name',
        #     'email':'Enter Your Email',
        #     'phone':'Enter Your Contact No.',
        #     'password':'Enter Password'
        # }