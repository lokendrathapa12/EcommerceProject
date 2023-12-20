from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(VendorModel)
class vendorAdminModel(admin.ModelAdmin):
    list_display =['id','user','name','shopname','phone','email','location','panano']

@admin.register(SelectProduct)
class SelectProductAdminModel(admin.ModelAdmin):
    list_display = ['id','user','product','quantity']