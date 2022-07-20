from django.contrib import admin
from app.models import Customers,Product,Cart,OrderedPlaced
# Register your models here.
@admin.register(Customers)
class CustomerAdminModel(admin.ModelAdmin):
    list_display = ['id','user','name','location','city','zipcode','provience','phone','email']


@admin.register(Product)
class ProductAdminModel(admin.ModelAdmin):
    list_display =['id','title','selling_price','discount_price','description','brand','category','product_image']


@admin.register(Cart)
class CartAdminModel(admin.ModelAdmin):
    list_display = ['id','user','product','quantity']

@admin.register(OrderedPlaced)
class OrderAdminModel(admin.ModelAdmin):
    list_display = ['id','user','customer','product','ordered_date','status']