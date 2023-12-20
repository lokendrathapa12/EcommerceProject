from django.shortcuts import render,redirect
from django.views import View
from app.models import Product
from .models import *

# Create your views here.
class VendorHomeView(View):
    def get(self,request):
        product = Product.objects.filter(user=request.user)
        user = request.user
        selectproduct = SelectProduct.objects.filter(user = user)
        return render(request, 'vendor/home.html',{'product':product, 'selectproduct':selectproduct})
    
def SlectProductView(request):
    user = request.user
    prod_id = request.GET.get('prod_id')
    product = Product.objects.get(id=prod_id)
    selectitem = SelectProduct(user=user,product=product)
    selectitem.save()
    return redirect('/vendor')
