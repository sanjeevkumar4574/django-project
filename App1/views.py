from django.shortcuts import render,HttpResponseRedirect
from App1.forms import StudentRegistration
from App1.models import CRUD_DataBase

# Create your views here.
def home(request):
    if request.method == 'POST':
        data = StudentRegistration(request.POST)
        if data.is_valid():
            fname = data.cleaned_data['name']
            femail = data.cleaned_data['email']
            fphone = data.cleaned_data['phone']
            fpassword = data.cleaned_data['password']
            print(fname)
            mdata = CRUD_DataBase(name = fname,email= femail,phone = fphone,password = fpassword)
            mdata.save()
            data = StudentRegistration()
            
    else:
        data = StudentRegistration()
    model_data = CRUD_DataBase.objects.all()
    return render(request,'App1/core.html',{'form':data,'data':model_data})


#function for deete row data
def delete(request,id):
    if request.method == 'POST':
        data_4_delete = CRUD_DataBase.objects.get(pk=id)
        data_4_delete.delete()
    return HttpResponseRedirect('/')


# function for edit row data
def update(request,edit_id):
     
    if request.method == 'POST':
        edit_data = CRUD_DataBase.objects.get(pk=edit_id)
        data  = StudentRegistration(request.POST,instance=edit_data)
        if data.is_valid():
            data.save()
    else:
        edit_data = CRUD_DataBase.objects.get(pk=edit_id)
        data  = StudentRegistration(instance=edit_data)
    return render(request,'App1/update.html',{'edit1':data})