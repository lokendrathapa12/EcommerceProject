from email.policy import default
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

 
class Customers(models.Model):
    Provience_choice =(
        ('KP','Karnali Provience'),
        ('BP','Bagmati Provience'),
        ('GP','Gandaki Provience'),
        ('LP','Lumbini Pradesh'),
        ('P1','Provience 1'),
        ('P2','Provience 2'),
        ('P3','Provience 3')
    )
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    zipcode = models.IntegerField()
    provience = models.CharField(max_length=2,choices= Provience_choice,default='Karnali Provience')
    phone = models.IntegerField()
    email = models.EmailField(max_length=60)


    def __str__(self):
        return self.name

class Product(models.Model):
    category_choice =(
        ('M','Mobile'),
        ('L','Laptop'),
        ('TW','Top Wear'),
        ('BW','Bottom Wear')
    )
    title = models.CharField(max_length=100)
    selling_price = models.FloatField()
    discount_price = models.FloatField()
    description = models.TextField(max_length=10000)
    brand = models.CharField(max_length=100)
    category = models.CharField(max_length=2,choices=category_choice,default='Mobile')
    product_image = models.ImageField(upload_to = 'productimage',default='')

    def __str__(self):
        return self.title

class Cart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)


    def __str__(self):
        return str(self.id)
    @property
    def total_cost(self):
        return self.quantity * self.product.discount_price

class OrderedPlaced(models.Model):
    Status_Choice =(
        ('Accepted','Accepted'),
        ('Packed','Packed'),
        ('On The way','On The way'),
        ('Delivered','Delivered'),
        ('Cancel','Cancel')
    )
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    customer = models.ForeignKey(Customers,on_delete=models.CASCADE)
    ordered_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20,choices=Status_Choice,default='Accepted')

    def __str__(self):
        return str(self.id)