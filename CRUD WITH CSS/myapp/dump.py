# def update(request,id):
#      return render(request,'edit.html')

# def delete(request,id):
#     response = Products.objects.get(id=id)
#     response.delete()
#     return redirect('')




   #  path('update/<int:id>/',views.update,name= "update"),

    #  path('delete/<int:id>/',views.delete,name= "delete")




     <td> <a type = "button" href= "{% url 'update' i.id %}"> Edit </a>
            <td> <a type = "button" href= "{% url 'delete' i.id%}"> Delete </a>
            


    
     '''  response = Products.objects.get(id=id)
        response.title  =  request.POST['title']
        response.price = request.POST['price']
        response.category = request.POST['Category']
        response.description =  request.POST['Description']
        response.image   = request.POST['image']
        response.save()
        return redirect('all')  
        '''