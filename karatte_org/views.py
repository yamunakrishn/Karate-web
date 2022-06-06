from atexit import register
from django.shortcuts import redirect, render
from urllib import request
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth import authenticate ,login, logout
from django.contrib.auth.decorators import login_required
from .models import *


def load_home_page(request):
    return render(request,'index.html')

#load affiliation page

def load_affiliation_page(request):
    return render(request,'affiliation.html')


def admin_login(request):
    error = ""
    if request.method == 'POST':
        u = request.POST['uname']
        p = request.POST['pwd']
        user = authenticate(username=u, password=p)
        try:
            if user.is_staff:
                login(request, user)
                error = "no"
            else:
                error = "nop"
        except:
            error = "yes"
    return render(request,'admin_login.html', locals())


def admin_home(request):
    return render(request,'admin_home.html')
def gallery_home(request):
    return render(request,'gallery_home.html')

# def gallery_home(request):
#     form= createproductform()
#     if request.method == 'POST':
#         form=createproductform(request.POST,request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('product')
#     return render(request,'gallery_home.html',{'form':form})


# def product(request):
#     product=  Product.objects.all()
#     return render(request,'product.html',{'product':product})
    