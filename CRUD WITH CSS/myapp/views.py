
from dataclasses import field
from urllib import response

from django.shortcuts import render,redirect
# Create your views here.
from . models import *
from .  serializers import *
from rest_framework.response import Response
import requests
import urllib, json
from . forms import *

from django.core.paginator import Paginator





# def get_products(request):
#    response = requests.get("https://fakestoreapi.com/products").json()
#    for i in response:
#     print(i['price'])
#     Products.objects.create(title=i['title'],price =i['price'],category=i['category'],description=i['description'], image=i['image'])
#    return render(request,'show.html',{'response':response})

# def get_single(request,id):
#     response = requests.get("https://fakestoreapi.com/products/1").json()
    
#     return render(request,'one.html',{'response':response})

def welcome(request):
    return render(request,'wel.html')



def get_products(request):

    response = Products.objects.exclude(title="")
    paginator = Paginator(response,5)

    pagenumber =request.GET.get('page')
    response = paginator.get_page(pagenumber)
    return render(request,'show.html',{'response':response})
 
def get_single(request,id):
    response = Products.objects.get(id=id)
    return render(request,'one.html',{'response':response})


'''
def update(request,id):
    if request.method == "POST":
        response = Products.objects.get(id=id)
        response.title  =  request.POST['title']
        response.price = request.POST['price']
        response.description =  request.POST['Description']
        response.image   = request.POST['image']
        response.save()
        return redirect('all')        

    else:
        response = Products.objects.get(id=id)
        return render(request,'edit.html',{'response':response})'''
 

def delete(request,id):
    response = Products.objects.get(id=id)
    response.delete()
    return redirect('all')


def addpro(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('all')

            except:
                pass
    
    else:
        form = ProductForm()
        return render(request,"create.html",{'form':form})



def updatedata(request, id ):
    response = Products.objects.get(id=id)
    form = ProductForm(initial={'title':response.title,'price':response.price , 'category': response.category ,
                                        'description':response.description,  'image':response.image  })
                                        
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=response)
        if form.is_valid():
            form.save()
            return redirect('all')
        else:
            pass
    return render(request, "update.html", {'form':form})




    
    


