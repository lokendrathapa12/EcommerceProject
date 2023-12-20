from email import message
from unicodedata import category, name
from django import dispatch
from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.views import View
from numpy import product
from .models import Cart, Customers, Product,OrderedPlaced
from .forms import registratioForm,ProfileForm,ProductUploadForm,ProductSearchForm
from django.contrib.auth import logout
from django.contrib import messages
from django.db.models import Q
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .utils import send_sold_out_email,send_out_email_customer,send_email_registration


@method_decorator(login_required,name='dispatch')
class ProductView(View):
    def get(self,request):
        tools = Product.objects.filter(category='TE')
        furniture = Product.objects.filter(category='OF')
        art = Product.objects.filter(category='AC')
        boys = Product.objects.filter(category='BF')
        girls = Product.objects.filter(category='GF')
        man = Product.objects.filter(category='MF')
        woman = Product.objects.filter(category='WF')
        baby = Product.objects.filter(category='B')
        electronics = Product.objects.filter(category='E')
        beauty = Product.objects.filter(category='BP')
        sport = Product.objects.filter(category='SO')
        toys = Product.objects.filter(category='TG')
        books = Product.objects.filter(category='BS')
        pet = Product.objects.filter(category='PS')
        digital = Product.objects.filter(category='DP')
        food = Product.objects.filter(category='FB')
        automotive = Product.objects.filter(category='AM')
        kitchen = Product.objects.filter(category='KA')
        groceries = Product.objects.filter(category='G')
        return render(request,'app/home.html',{'tools':tools,'furniture':furniture,'art':art,'boys':boys,
                                               'girls':girls,'man':man,'woman':woman,'baby':baby,'electronics':electronics,
                                               'beauty':beauty,'sport':sport,'toys':toys,'books':books,'pet':pet,
                                               'digital':digital,'food':food,'automotive':automotive,'kitchen':kitchen,
                                               'groceries':groceries})
class ToolView(View):
    def get(self,request):
        tool = Product.objects.filter(category='TE')
        return render(request,'app/tools.html',{'tool':tool})
    
class FurnitureView(View):
    def get(self,request):
        furniture = Product.objects.filter(category='OF')
        return render(request,'app/furniture.html',{'furniture':furniture})

class ArtView(View):
    def get(self,request):
        art = Product.objects.filter(category='AC')
        return render(request,'app/art.html',{'art':art})
    
class BoyfashionView(View):
    def get(self,request):
        boy = Product.objects.filter(category='BF')
        return render(request,'app/boys.html',{'boy':boy})
    
class GirlfashionView(View):
    def get(self,request):
        girl = Product.objects.filter(category='GF')
        return render(request,'app/girls.html',{'girl':girl})
    
class ManfashionView(View):
    def get(self,request):
        man = Product.objects.filter(category='MF')
        return render(request,'app/man.html',{'man':man})
    
class WomanfashionView(View):
    def get(self,request):
        woman = Product.objects.filter(category='WF')
        return render(request,'app/woman.html',{'woaman':woman})
    
class BabyView(View):
    def get(self,request):
        baby = Product.objects.filter(category='B')
        return render(request,'app/baby.html',{'baby':baby})
    
class ElectronicsView(View):
    def get(self,request):
        electronic = Product.objects.filter(category='E')
        return render(request,'app/electronics.html',{'electronic':electronic})
    
class BeautyView(View):
    def get(self,request):
        beauty = Product.objects.filter(category='BP')
        return render(request,'app/beauty.html',{'beauty':beauty})
    
class SportView(View):
    def get(self,request):
        sport = Product.objects.filter(category='SO')
        return render(request,'app/sports.html',{'sport':sport})
    
class ToysView(View):
    def get(self,request):
        toy = Product.objects.filter(category='TG')
        return render(request,'app/toy.html',{'toy':toy})
    
class BookView(View):
    def get(self,request):
        book = Product.objects.filter(category='BS')
        return render(request,'app/book.html',{'book':book})
    
class PetView(View):
    def get(self,request):
        pet = Product.objects.filter(category='PS')
        return render(request,'app/pet.html',{'pet':pet})
    
class DigitalView(View):
    def get(self,request):
        digital = Product.objects.filter(category='DP')
        return render(request,'app/digital.html',{'digital':digital})
    
class FoodView(View):
    def get(self,request):
        food = Product.objects.filter(category='FB')
        return render(request,'app/food.html',{'food':food})
    
class AutomotiveView(View):
    def get(self,request):
        automotive = Product.objects.filter(category='AM')
        return render(request,'app/automotive.html',{'automotive':automotive})
    
class KitchenView(View):
    def get(self,request):
        kitchen = Product.objects.filter(category='KA')
        return render(request,'app/kitchen.html',{'kitchen':kitchen})

class GroceriesView(View):
    def get(self,request):
        groceries = Product.objects.filter(category='G')
        return render(request,'app/groceries.html',{'groceries':groceries})

class product_detail(View):
    def get(self,request,pk):
        product = Product.objects.get(pk=pk)
        product_already_in_cart = False
        product_already_in_cart = Cart.objects.filter(Q(product=product.id) & Q(user=request.user)).exists()
        return render(request,'app/productdetail.html',{'product':product, 'product_already_in_cart':product_already_in_cart})
    
@login_required
def add_to_cart(request):
    user = request.user
    prod_id = request.GET.get('prod_id')
    product = Product.objects.get(id=prod_id)
    cart = Cart(user=user,product=product)
    cart.save()
    return redirect('/cart')

@login_required
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
        
@login_required
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

@login_required
def address(request):
    add = Customers.objects.filter(user=request.user)
    return render(request, 'app/address.html',{'add':add,'active':'btn-primary'})


#def mobile(request,data=None):
    #if data == None:
        #mobile = Product.objects.filter(category='M')
    #elif data == 'Redmi' or data == 'Samsung':
       # mobile = Product.objects.filter(category='M').filter(brand=data)
    #elif data =='below':
        #mobile = Product.objects.filter(category='M').filter(discount_price__lt=10000)
   # elif data == 'above':
        #mobile = Product.objects.filter(category='M').filter(discount_price__gt=10000)
    #return render(request, 'app/mobile.html',{'mobile':mobile})



class customerregistrationform(View):
    def get(self,request):
        form = registratioForm
        return render (request,'app/customerregistration.html',{'form':form})

    def post(self,request):
        form = registratioForm(request.POST)
        if form.is_valid():
            fm =form.save()
            if fm:
                send_email_registration(fm.id)
            messages.success(request, 'Congratulation!!  Registration Succesfully')
        return render (request,'app/customerregistration.html',{'form':form})

def LogoutView(request):
    logout(request)
    return redirect('/')


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


@login_required
def PaymentDoneView(request):
    user = request.user
    custid = request.GET.get('custid')
    customer = Customers.objects.get(id=custid)
    cart = Cart.objects.filter(user=user)
    for c in cart:
        ord =OrderedPlaced(user=user, customer=customer,location=customer.location,city=customer.city,
                      provience=customer.provience,zipcode=customer.zipcode,wardno=customer.wardno,
                      phone=customer.phone,email=customer.email,product=c.product,product_owner=c.product.user,
                      shopname=c.product.shopname,owner_email=c.product.owner_email,quantity=c.quantity)
        ord.save()
        c.delete()
        if ord:
        # Call the email sending function with the order ID
            send_sold_out_email(ord.id)
            send_out_email_customer(ord.id)

        return redirect('orders')
    


@login_required
def orders(request):
 op = OrderedPlaced.objects.filter(user=request.user)
 return render(request, 'app/orders.html',{'op':op})

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
    

@method_decorator(login_required,name='dispatch')
class ProductUploadView(View):
    def get(self,request):
        form = ProductUploadForm()
        return render(request, 'app/productupload.html',{'form':form, 'active':'btn-primary'})
    def post(self,request):
        form = ProductUploadForm(request.POST,request.FILES)
        if form.is_valid():
            user = request.user
            title = form.cleaned_data['title']
            shopname = form.cleaned_data['shopname']
            selling_price = form.cleaned_data['selling_price']
            discount_price = form.cleaned_data['discount_price']
            description = form.cleaned_data['description']
            brand = form.cleaned_data['brand']
            category = form.cleaned_data['category']
            subcategory = form.cleaned_data['subcategory']
            product_image_frontside = form.cleaned_data['product_image_frontside']
            product_image_backside = form.cleaned_data['product_image_backside']
            product_image_topside = form.cleaned_data['product_image_topside']
            product_image_bottomside = form.cleaned_data['product_image_bottomside']
            product_image_leftside = form.cleaned_data['product_image_leftside']
            product_image_rightside = form.cleaned_data['product_image_rightside']
            upload = Product(user=user,title=title,shopname=shopname,selling_price=selling_price,discount_price=discount_price,description=description,
                            brand=brand,category=category,subcategory=subcategory,product_image_frontside=product_image_frontside,
                            product_image_backside=product_image_backside,product_image_topside=product_image_topside,product_image_bottomside=product_image_bottomside,
                            product_image_leftside=product_image_leftside,product_image_rightside=product_image_rightside)
            upload.save()
            messages.success(request,'Your Product update Succesfully')

        return render(request,'app/productupload.html',{'form':form,'active':'btn-primary'})


def product_search(request):
    query = request.GET.get('query')
    if query:
        product = Product.objects.filter(title__istartswith=query)
        return render(request,'app/search.html',{'product':product})
    else:
        return render(request, 'app/search.html',{})