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
        ('KO','Koshi Pradesh'),
        ('MP','Madesh Pradesh'),
        ('SP','Sudurpashim pradesh')
    )
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    wardno = models.IntegerField(default=1)
    city = models.CharField(max_length=100)
    zipcode = models.IntegerField()
    provience = models.CharField(max_length=2,choices= Provience_choice,default='Bagmati Provience')
    phone = models.BigIntegerField()
    email = models.EmailField(max_length=60)


    def __str__(self):
        return self.name

class Product(models.Model):
    category_choice =(
        ('TE','Tools And Equipment'),
        ('OF','Office furniture'),
        ('AC','Art And Craft'),
        ('BF','Boys Fashion'),
        ('GF','Girls Fashion'),
        ('MF','Men Fashion'),
        ('WF','Women Fashion'),
        ('B','Baby'),
        ('E','Electronics'),
        ('BP','Beauty And Personal Care'),
        ('SO','Sports And Outdoors:'),
        ('TG','Toys And Games'),
        ('BS','Books And Stationry'),
        ('PS','Pet Suppliers'),
        ('DP','Digital Product'),
        ('FB','Food And Beverage'),
        ('AM','Automotive'),
        ('KA','kitchen And Appliances'),
        ('G','Groceries'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE,default="")
    title = models.CharField(max_length=100)
    owner_email = models.EmailField(max_length=150,default='')
    shopname = models.CharField(max_length=250,default='')
    selling_price = models.FloatField()
    discount_price = models.FloatField()
    description = models.TextField(max_length=10000)
    brand = models.CharField(max_length=100)
    upload_date = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=3,choices=category_choice,default='Office Furniture')
    subcategory = models.CharField(max_length=150,default='')
    product_image_frontside = models.ImageField(upload_to = 'productimage',default='')
    product_image_backside = models.ImageField(upload_to = 'productimage',default='')
    product_image_topside = models.ImageField(upload_to = 'productimage',default='')
    product_image_bottomside = models.ImageField(upload_to = 'productimage',default='')
    product_image_leftside = models.ImageField(upload_to = 'productimage',default='')
    product_image_rightside = models.ImageField(upload_to = 'productimage',default='')
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
        ('Pending','Pending')
    )
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    product_owner = models.CharField(max_length=100,default='')
    shopname = models.CharField(max_length=100,default='')
    owner_email = models.EmailField(max_length=50,default='')
    customer = models.ForeignKey(Customers,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    ordered_date = models.DateTimeField(auto_now_add=True)
    location = models.CharField(max_length=150,default="")
    city = models.CharField(max_length=150, default="")
    provience = models.CharField(max_length=150,default="")
    zipcode = models.IntegerField(default=0000)
    wardno = models.IntegerField(default=1)
    phone = models.BigIntegerField(default=0000000000)
    email = models.EmailField(max_length=60,default='')
    status = models.CharField(max_length=20,choices=Status_Choice,default='Pending')

    def __str__(self):
        return str(self.id)
    
    @property
    def total_cost(self):
        return self.quantity * self.product.discount_price