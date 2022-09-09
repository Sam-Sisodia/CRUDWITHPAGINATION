from rest_framework import serializers
from . models import *


class Productserilizer(serializers.Serializer):
    class Meta :
        model = Products
        fields = '__all__'