from django.contrib import admin
from app.models import Customers,Product,Cart,OrderedPlaced
# Register your models here.
@admin.register(Customers)
class CustomerAdminModel(admin.ModelAdmin):
    list_display = ['id','user','name','location','wardno','city','zipcode','provience','phone','email']


@admin.register(Product)
class ProductAdminModel(admin.ModelAdmin):
    list_display =['id','user','title','shopname','owner_email','selling_price','discount_price','description','brand','category','subcategory','product_image_frontside','product_image_backside','product_image_topside','product_image_bottomside','product_image_leftside','product_image_rightside','upload_date']


@admin.register(Cart)
class CartAdminModel(admin.ModelAdmin):
    list_display = ['id','user','product','quantity']

@admin.register(OrderedPlaced)
class OrderAdminModel(admin.ModelAdmin):
    list_display = ['id','user','customer','product','product_owner','shopname','owner_email','ordered_date','location','city','provience','zipcode','wardno','phone','email','status']

