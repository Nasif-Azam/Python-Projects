from django.http import HttpResponse
from django.shortcuts import render
from .models import Product


def index(request):
    products = Product.objects.all()  # .filter,.get
    # return HttpResponse('I am Nasif Azam')
    return render(request, 'index.html', {'products': products})


def new_products(request):
    return HttpResponse('New Products Available!!!!')
