from django.shortcuts import render
from .models import *
# Create your views here.

def home(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()

    total_customers = customers.count()

    total_orders = orders.count()
    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status='Pedning').count()

    context = {'orders':orders, 'customers':customers, 'total_customers':total_customers, 'total_orders':total_orders, 'delivered':delivered, 'pending':pending}
    return render(request, 'accounts/dashboard.html', context )

def products(request):
    products = Product.object.all()
    return render(request, 'accounts/products.html')

    return render(request, 'accounts/products.html', {'products':products})

def customers(request):
    customers = Customer.objects.get(id=pk_test)
    return render(request, 'accounts/customers.html')
