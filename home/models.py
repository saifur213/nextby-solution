from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

# Create your models here.
class Package(models.Model):
    pck_id = models.CharField(max_length=20)
    pck_title = models.CharField(max_length=100)
    pck_img = models.ImageField(upload_to='img/')
    pck_price = models.DecimalField(max_digits=10, decimal_places=2)
    pck_f1 = models.CharField(max_length=100)
    pck_f2 = models.CharField(max_length=100)
    pck_f3 = models.CharField(max_length=100)
    pck_f4 = models.CharField(max_length=100)
    pck_f5 = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.pck_id
    
class CustomUser(models.Model):
    # Add custom fields
    username = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    password1 = models.CharField(max_length=20)
    password2 = models.CharField(max_length=20)

    

    def __str__(self):
        return self.username
    
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    mobile = models.IntegerField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name