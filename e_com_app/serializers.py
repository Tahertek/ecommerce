from rest_framework import serializers
from .models import Product,CustomUser,Panier
#define the serializer class for the product model
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields ='__all__'
class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields =('name','email','phone','client')

class panierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Panier
        fields='__all__'