from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Product, Order, Model
from .forms import ProductForm, OrderForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.serializers import serialize
from .serializers import OrderSerializer, ProductSerializer
import xml.etree.ElementTree as ET
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
@login_required
def index(request):
    orders = Order.objects.all()
    products = Product.objects.all()

    workers_count = User.objects.all().count()
    orders_count = Order.objects.all().count()
    items_count = Product.objects.all().count()

    if request.method == 'POST' :
        form = OrderForm(request.POST)
        if form.is_valid():
            isinstance = form.save(commit=False)
            isinstance.staff = request.user
            isinstance.save()
            return redirect('dashboard-index')
    else:
        form = OrderForm()
    context = {
        'orders' : orders,
        'form' : form,
        'products' : products,
        'workers_count' : workers_count,
        'orders_count' : orders_count,
        'items_count' : items_count

    }
    return render(request, 'dashboard/index.html', context)

@login_required
def staff(request):
    workers = User.objects.all()
    workers_count = workers.count()
    orders_count = Order.objects.all().count()
    items_count = Product.objects.all().count()
    context = {
        'workers' : workers,
        'workers_count' : workers_count,
        'orders_count' : orders_count,
        'items_count' : items_count
    }
    return render(request, 'dashboard/staff.html', context)

@login_required
def staff_detail(request, pk):
    worker = User.objects.get(id=pk)
    context = {
        'worker': worker
    } 
    return render(request, 'dashboard/staff_detail.html', context)


@login_required
def product(request):
    items = Product.objects.all() # using ORM
    items_count = items.count()

    # if you want to write normal SQL quieries you can use Raw
    # to retrive particular table name of application _ name of model
    # items = Product.objects.raw('SELECT * FROM dashboard_product')
    
    workers_count = User.objects.all().count()
    orders_count = Order.objects.all().count()

    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            product_name = form.cleaned_data.get('name') # Graping the name
            messages.success(request, f'{product_name} has been added')
            return redirect('dashboard-product')
    else:
        form = ProductForm()

    context ={
        'items' : items,
        'form' : form,
        'items_count' : items_count,
        'workers_count' : workers_count,
        'orders_count' : orders_count,
    }
    return render(request, 'dashboard/product.html', context)

@login_required
def product_delete(request, pk):
    item = Product.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('dashboard-product')
    return render(request, 'dashboard/product_delete.html')

@login_required
def product_update(request, pk):
    item = Product.objects.get(id=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('dashboard-product')
    else:
        form = ProductForm(instance=item)

    context ={
        'form' : form,
    }
    return render(request, 'dashboard/product_update.html', context)


@login_required
def order(request):
    orders = Order.objects.all()
    orders_count = orders.count()
    workers_count = User.objects.all().count()
    items_count = Product.objects.all().count()
    context = {
        'orders' : orders,
        'orders_count' : orders_count,
        'workers_count' : workers_count,
        'items_count' : items_count,
    }
    return render(request, 'dashboard/order.html', context)

# Add this missing function
def redirect_to_dashboard(request):
    return redirect('dashboard-index')

@api_view(['GET'])
def get_data(request, format=None):
    data = Order.objects.all()
    
    if format == 'xml':
        xml_data = '<?xml version="1.0" encoding="UTF-8"?>\n'
        for obj in data:
            serializer = OrderSerializer(obj)
            xml_data += serializer.to_xml(obj)
        return HttpResponse(xml_data, content_type='application/xml')
    
    elif format == 'json':
        json_data = serialize('json', data, use_natural_foreign_keys=True, use_natural_primary_keys=True)
        return HttpResponse(json_data, content_type='application/json')
    
    return Response({"error": "Unsupported format. Use ?format=xml or ?format=json"}, status=400)

@api_view(['GET'])
def get_products(request, format=None):
    data = Product.objects.all()
    
    if format == 'xml':
        xml_data = '<?xml version="1.0" encoding="UTF-8"?>\n'
        for obj in data:
            serializer = ProductSerializer(obj)
            xml_data += serializer.to_xml(obj)
        return HttpResponse(xml_data, content_type='application/xml')
    
    elif format == 'json':
        json_data = serialize('json', data)
        return HttpResponse(json_data, content_type='application/json')
    
    return Response({"error": "Unsupported format. Use ?format=xml or ?format=json"}, status=400)
