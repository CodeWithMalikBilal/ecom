from django.shortcuts import render,redirect
from django.views import View
from .models import Product,Customer,Cart,OrderStatus
from .forms import CustomerRegisterForm,CustomerProfileForm
from django.contrib import messages
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.db.models import Q
from django.http import JsonResponse
# Create your views here.

def home(request):
    return render(request,'home.html')



class MenuView(View):
    def get(self,request):
        pizza = Product.objects.filter(category="P")
        burger= Product.objects.filter(category = "B")
        cupcake = Product.objects.filter(category="CC")
        icecream = Product.objects.filter(category="IC")
        return render(request,'menu.html',{'pizza':pizza,'burger':burger,'cupcake':cupcake,'icecream':icecream})



#def menu(request):
#    return render(request,'menu.html')

def aboutus(request):
    return render(request,'aboutus.html')

def order(request):
    return render(request,'order.html')


def contact(request):
    return render(request,'contact.html')

#def login(request):
#return render(request,'login.html')

#Customer Registeration View

class CustomerRegisterView(View):
    def get(self,request):
        form = CustomerRegisterForm()
        return render(request,'register.html',{'form':form})
    def post(self,request):
        form = CustomerRegisterForm(request.POST)
        if form.is_valid():
            messages.success(request,'Registered SuccessFully!!')
            form.save()
        return render(request,'register.html',{'form':form})



#def register(request):
#    return render(request,'register.html')

#Function BaseD View To Show the Data in Product Detail

class ProductView(View):
    def get(self,request):
        pizza = Product.objects.filter(category="P")
        burger = Product.objects.filter(category="B")
        cupcake = Product.objects.filter(category="CC")
        icecream = Product.objects.filter(category="IC")
        return render(request,'home.html',{'pizza':pizza,'burger':burger,'cupcake':cupcake,'icecream':icecream})



class ProductDetailView(View):
    def get(self,request,pk):
        product = Product.objects.get(pk=pk)
        return render(request,'productdetail.html',{'product':product})




#def product_detail(request):
#    return render(request, 'product_detail.html')



#def profile(request):
#    return render(request, 'profile.html')


def addtocart(request):
    user = request.user
    product_id = request.GET.get('prod_id')
    product = Product.objects.get(id=product_id)
    Cart(user=user,product=product).save()
    return redirect('/cart')

def showcart(request):
    if request.user.is_authenticated:
        user = request.user
        cart = Cart.objects.filter(user=user)
        quantity = 0
        amount = 0.0
        shipping_amount = 200
        total_amount = 0.0
        cart_product = [p for p in Cart.objects.all() if p.user==request.user]
        if cart_product:
            for p in cart_product:
                tempamount = (p.quantity * p.product.price)
                amount += tempamount
                total_amount = amount + shipping_amount
                quantity +=1
        return render(request,'addtocart.html',{'carts':cart,'total':total_amount,'amount':amount,'quant':quantity})


def pluscart(request):
    if request.method=='GET':
        prod_id = request.GET['prod_id']
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.quantity+=1
        c.save()
        amount = 0.0
        shipping_amount = 200
        total_amount = 0.0
        cart_product = [p for p in Cart.objects.all() if p.user==request.user]
        for p in cart_product:
            tempamount = (p.quantity * p.product.price)
            amount+=tempamount
            total_amount = amount+shipping_amount
        data={
            'quantity':c.quantity,
            'amount':amount,
            'total_amount':total_amount
        }
        return JsonResponse(data)


def minuscart(request):
    if request.method=='GET':
        prod_id = request.GET['prod_id']
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.quantity-=1
        c.save()
        amount = 0.0
        shipping_amount = 200
        total_amount = 0.0
        cart_product = [p for p in Cart.objects.all() if p.user==request.user]
        for p in cart_product:
            tempamount = (p.quantity * p.product.price)
            amount+=tempamount
            total_amount = amount+shipping_amount
        data={
            'quantity':c.quantity,
            'amount':amount,
            'total_amount':total_amount
        }
        return JsonResponse(data)


def removecart(request):
    if request.method=='GET':
        prod_id = request.GET['prod_id']
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.delete()
        amount = 0.0
        shipping_amount = 200
        total_amount = 0.0
        cart_product = [p for p in Cart.objects.all() if p.user==request.user]
        for p in cart_product:
            tempamount = (p.quantity * p.product.price)
            amount+=tempamount
            total_amount = amount+shipping_amount
        data={

            'amount':amount,
            'total_amount':total_amount
        }
        return JsonResponse(data)




def logout_user(request):
    logout(request)
    return HttpResponseRedirect('accounts/login/')

def address(request):
    add = Customer.objects.filter(user=request.user)
    return render(request,'address.html',{'add':add})


class ProfileView(View):
    def get(self,request):
        form = CustomerProfileForm()
        return render(request,'profile.html',{'form':form})
    
    def post(self,request):
        form = CustomerProfileForm(request.POST)
        if form.is_valid():
            usr = request.user
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            mobile = form.cleaned_data['mobile']
            address = form.cleaned_data['address']
            reg = Customer(user = usr, name=name,email=email,mobile=mobile,address=address)
            reg.save()
            messages.success(request,'Profile Updated Successfully')
        return render(request,'profile.html',{'form':form})


    


