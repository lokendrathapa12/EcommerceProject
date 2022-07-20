from email import message
from unicodedata import category, name
from django import dispatch
from django.shortcuts import render,redirect
from django.views import View
from numpy import product
from .models import Cart, Customers, Product
from .forms import registratioForm,ProfileForm
from django.contrib import messages
from django.db.models import Q
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
class ProductView(View):
    def get(self,request):
        topwear = Product.objects.filter(category='TW')
        bottomwear = Product.objects.filter(category='BW')
        mobile = Product.objects.filter(category='M')
        laptop = Product.objects.filter(category='L')
        return render(request,'app/home.html',{'topwear':topwear,'bottomwear':bottomwear,'mobile':mobile,'laptop':laptop})

#def product_detail(request):
 #return render(request, 'app/productdetail.html')

class product_detail(View):
    def get(self,request,pk):
        product = Product.objects.get(pk=pk)
        return render(request,'app/productdetail.html',{'product':product})
@login_required
def add_to_cart(request):
    user = request.user
    prod_id = request.GET.get('prod_id')
    product = Product.objects.get(id=prod_id)
    cart = Cart(user=user,product=product)
    cart.save()
    return redirect('/cart')

def ShowCart(request):
    if request.user.is_authenticated:
        user= request.user
        cart = Cart.objects.filter(user=user)
        amount=0.0
        shipping_amount=99.0
        total_amount=0.0
        cart_product=[p for p in Cart.objects.all() if p.user==user]
        if cart_product:
            for p in cart_product:
                tempamount = (p.quantity*p.product.discount_price)
                amount +=tempamount
                totalamount= amount+shipping_amount
            return render(request, 'app/addtocart.html',{'cart':cart,'totalamount':totalamount, 'amount':amount})
        else:
            return render(request,'app/emptycart.html')

def PlusCart(request):
    if request.method == 'GET':
        prod_id= request.GET['prod_id']
        c= Cart.objects.get(Q(product=prod_id) & Q(user=request.user))              
        c.quantity+=1
        c.save()
        amount=0.0
        shipping_amount=99.0
        cart_product=[p for p in Cart.objects.all() if p.user==request.user]
        for p in cart_product:
            tempamount = (p.quantity*p.product.discount_price)
            amount +=tempamount
            
        data={
            'quantity':c.quantity,
            'amount':amount,
            'totalamount':amount+shipping_amount
        }
        return JsonResponse(data)
@login_required
def MinusCart(request):
    if request.method == 'GET':
        prod_id= request.GET['prod_id']
        c= Cart.objects.get(Q(product=prod_id) & Q(user=request.user))              
        c.quantity-=1
        c.save()
        amount=0.0
        shipping_amount=99.0
        cart_product=[p for p in Cart.objects.all() if p.user==request.user]
        for p in cart_product:
            tempamount = (p.quantity*p.product.discount_price)
            amount +=tempamount
              

        data={
            'quantity':c.quantity,
            'amount':amount,
            'totalamount':amount+shipping_amount
        }
        return JsonResponse(data)  
@login_required
def removecart(request):
    if request.method == 'GET':
        prod_id= request.GET['prod_id']
        c= Cart.objects.get(Q(product=prod_id) & Q(user=request.user))              
        c.delete()
        amount=0.0
        shipping_amount=99.0
        cart_product=[p for p in Cart.objects.all() if p.user==request.user]
        for p in cart_product:
            tempamount = (p.quantity*p.product.discount_price)
            amount +=tempamount
              

        data={
            'quantity':c.quantity,
            'amount':amount,
            'totalamount': amount+shipping_amount
        }
        return JsonResponse(data)
@login_required
def buy_now(request):
 return render(request, 'app/buynow.html')

#def profile(request):
 #return render(request, 'app/profile.html')
@login_required
def address(request):
    add = Customers.objects.filter(user=request.user)
    return render(request, 'app/address.html',{'add':add,'active':'btn-primary'})
@login_required
def orders(request):
 return render(request, 'app/orders.html')


def mobile(request,data=None):
    if data == None:
        mobile = Product.objects.filter(category='M')
    elif data == 'Redmi' or data == 'Samsung':
        mobile = Product.objects.filter(category='M').filter(brand=data)
    elif data =='below':
        mobile = Product.objects.filter(category='M').filter(discount_price__lt=10000)
    elif data == 'above':
        mobile = Product.objects.filter(category='M').filter(discount_price__gt=10000)
    return render(request, 'app/mobile.html',{'mobile':mobile})


def laptop(request,data=None):
    if data == None:
        laptop = Product.objects.filter(category='L')
    elif data == 'Dell' or data == 'Hp'or data == 'Acer':
        laptop = Product.objects.filter(category='L').filter(brand=data)
    elif data =='below':
        laptop = Product.objects.filter(category='L').filter(discount_price__lt=30000)
    elif data == 'above':
        laptop = Product.objects.filter(category='L').filter(discount_price__gt=30000)
    return render(request, 'app/laptop.html',{'laptop':laptop})

def topwear(request,data=None):
    if data == None:
        topwear = Product.objects.filter(category='TW')
    elif data == 'Above':
        topwear = Product.objects.filter(category='TW').filter(discount_price__gt=1000)
    elif data == 'Below':
        topwear = Product.objects.filter(category='TW').filter(discount_price__lt=1000)
    return render(request, 'app/topwear.html',{'topwear':topwear})

def bottomwear(request,data=None):
    if data == None:
        bottomwear = Product.objects.filter(category='BW')
    elif data == 'Above':
        bottomwear = Product.objects.filter(category='BW').filter(discount_price__gt=1000)
    elif data == 'Below':
        bottomwear = Product.objects.filter(category='BW').filter(discount_price__lt=1000)
    return render(request, 'app/bottomwear.html',{'bottomwear':bottomwear})


class customerregistrationform(View):
    def get(self,request):
        form = registratioForm
        return render (request,'app/customerregistration.html',{'form':form})

    def post(self,request):
        form = registratioForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Congratulation!!  Registration Succesfully')
        return render (request,'app/customerregistration.html',{'form':form})

@login_required
def checkout(request):
    user = request.user
    add = Customers.objects.filter(user=user)
    cart = Cart.objects.filter(user=user)
    amount = 0.0
    shipping_amount = 99.0
    total_amount = 0.0
    cart_product=[p for p in Cart.objects.all() if p.user==user]
    if cart_product:
        for p in cart_product:
            tempamount = (p.quantity*p.product.discount_price)
            amount +=tempamount
        totalamount= amount+shipping_amount
    return render(request, 'app/checkout.html',{'add':add,'totalamount':totalamount,'cart':cart})

@method_decorator(login_required,name='dispatch')
class ProfileView(View):
    def get(self,request):
        customer = ProfileForm()
        return render(request,'app/profile.html',{'form':customer,'active':'btn-primary'})
    def post(self,request):
        customer = ProfileForm(request.POST)
        if customer.is_valid():
            usr= request.user
            name= customer.cleaned_data['name']
            location= customer.cleaned_data['location']
            city= customer.cleaned_data['city']
            phone= customer.cleaned_data['phone']
            provience= customer.cleaned_data['provience']
            zipcode= customer.cleaned_data['zipcode']
            email= customer.cleaned_data['email']
            reg =Customers(user=usr, name=name, location=location,city=city,phone=phone,provience=provience,zipcode=zipcode,email=email)
            reg.save()
            messages.success(request,'Your profile update Succesfully')
        return render(request,'app/profile.html',{'form':customer,'active':'btn-primary'})
