from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.views import APIView
from olx.models import Products
from olx.serializer import UserSerializer,ProductSerializer
from rest_framework import permissions,authentication
from django.contrib.auth.models import User
from rest_framework.decorators import action

# Create your views here.
class UsersView(viewsets.ModelViewSet):
    serializer_class=UserSerializer
    queryset=User.objects.all()   

class ProductsView(viewsets.ModelViewSet):
    serializer_class=ProductSerializer
    queryset=Products.objects.all()
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]

    # @action(methods=["POST"],detail=True)
    # def product_add(self,request,*args,**kw):
        
    #     id=kw.get("pk")
    #     category=Categories.objects.get(id=id)
    #     owner=request.user
    #     serializer=ProductSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save(category=category,owner=owner)
    #         return Response(data=serializer.data)
    #     else:
    #         return Response(data=serializer.errors)   

class ProductDeleteView(APIView):
    def delete(self,request,*args,**kwargs):
        id = kwargs.get("pk")
        Products.objects.filter(id=id).delete()
        return Response(data="product deleted")


# class CategoriesView(viewsets.ModelViewSet):
#     serializer_class=CategoriesSerializer
#     queryset=Categories.objects.all()
#     authentication_classes=[authentication.BasicAuthentication]
#     permission_classes=[permissions.IsAuthenticated]                        
