from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'accounts/dashboard.html')

def product(request):
    return render(request, 'accounts/product.html')

def customer(request):
    return render(request, 'accounts/customer.html')


