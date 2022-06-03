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