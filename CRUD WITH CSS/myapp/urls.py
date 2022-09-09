from django.contrib import admin
from django.urls import path,include
from myapp import views

urlpatterns = [
    path('',views.welcome, name= "wel"),
     path('all',views.get_products , name= "all"),
     path('all/<id>/',views.get_single,name= "one"),
    # path('update/<int:id>/',views.update,name= "update"),

     path('delete/<int:id>/',views.delete,name= "delete"),
     path('add',views.addpro, name= "addpro"),

     path('updatedata/<int:id>/',views.updatedata , name="updatedata")
     
 
     
]
