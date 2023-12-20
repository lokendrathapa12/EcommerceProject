from django.db import models
from django.contrib.auth.models import User
from app.models import Product
# Create your models here.
class VendorModel(models.Model):
    user = models.OneToOneField(User, on_delete= models.CASCADE)
    name = models.CharField(max_length=150)
    shopname = models.CharField(max_length=150)
    phone = models.IntegerField()
    email = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    panano = models.CharField(max_length=100)

    def __str__(self):
        return str(self.id)
    
class SelectProduct(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)