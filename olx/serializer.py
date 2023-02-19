from rest_framework import serializers
from django.contrib.auth.models import User
from olx.models import Products

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=["first_name","last_name","username","email","password"]

    def create(self,validated_data):
        return User.objects.create_user(**validated_data)    

class ProductSerializer(serializers.ModelSerializer):
    owner=serializers.CharField(read_only=True)
    category=serializers.CharField(read_only=True)
    created_date=serializers.CharField(read_only=True)

    class Meta:
        model=Products
        fields=["name","description","location","price","image"]

# class CategoriesSerializer(serializers.ModelSerializer):
#     is_active=serializers.CharField(read_only=True)

#     class Meta:
#         model=Categories
#         fields="__all__"

       
               


