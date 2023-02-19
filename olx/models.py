from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name="profile")
    address=models.CharField(max_length=200)
    phone_number=models.CharField(max_length=200)
    
class Category(models.Model):
    category_name=models.CharField(max_length=20)

    def __str__(self):
        return self.category_name 

class Products(models.Model):
    name=models.CharField(max_length=200)
    owner=models.ForeignKey(User,on_delete=models.CASCADE)
    description=models.CharField(max_length=300)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    location=models.CharField(max_length=200)
    price=models.PositiveIntegerField()
    image=models.ImageField(null=True,upload_to="image")
    options=(
        ("for-sale","for-sale"),
        ("exchange","exchange"),
        ("sold","sold"),
        ("rent","rent")
    )
    status=models.CharField(max_length=200,choices=options,default="for-sale")
    created_date=models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name       


class Notifications(models.Model):
    product=models.ForeignKey(Products,on_delete=models.CASCADE)
    buyer=models.ForeignKey(User,on_delete=models.CASCADE)
    description=models.CharField(max_length=300)
    options=(
        ("send","send"),
        ("pending","pending")
    )
    status=models.CharField(max_length=200,choices=options)

class Orders(models.Model):
    product=models.ForeignKey(Products,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    options=(
        ("order-placed","order-placed"),
        ("dispatched","dispatched"),
        ("cancelled","cancelled"),
        ("in-transit","in-transit")
    )
    status=models.CharField(max_length=200,choices=options,default="order-placed")
    date=models.DateField(auto_now_add=True)
    address=models.CharField(max_length=200)
    location=models.CharField(max_length=200)
    phone=models.CharField(max_length=20)        

