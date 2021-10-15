
from django.urls import path
from . import views 
urlpatterns = [
    path('',views.home,name='home'),
    path('delete/<int:id>',views.delete,name='delete'),
    path('update/<int:edit_id>',views.update,name='edit') 
    
]
