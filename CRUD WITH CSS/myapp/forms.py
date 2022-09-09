from . models import *
from django.forms import ModelForm
    

class ProductForm(ModelForm):
    class Meta:
        model = Products
        fields = "__all__"
