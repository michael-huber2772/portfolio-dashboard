# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse
from django import template

from .models import *

@login_required(login_url="/login/")
def index(request):
    total_customers = Customer.objects.all().count()
    total_products = Product.objects.all().count()


    context = {'total_customers': total_customers, 
               'total_products': total_products}
    context['segment'] = 'index'

    html_template = loader.get_template( 'index.html' )
    return HttpResponse(html_template.render(context, request))

@login_required(login_url="/login/")
def pages(request):
    
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:
        
        load_template      = request.path.split('/')[-1]
        context['segment'] = load_template
        
        html_template = loader.get_template( load_template )
        return HttpResponse(html_template.render(context, request))
        
    except template.TemplateDoesNotExist:

        html_template = loader.get_template( 'page-404.html' )
        return HttpResponse(html_template.render(context, request))

    except:
    
        html_template = loader.get_template( 'page-500.html' )
        return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def customers(request):
    customers = Customer.objects.all()

    context = {'customers': customers}
    return render(request, 'customers/customers.html', context)

@login_required(login_url="/login/")
def customer(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    products = Product.objects.filter(customer=pk)

    context = {'customer': customer, 'products': products}
    return render(request, 'customers/customer.html', context)

@login_required(login_url="/login/")
def products(request):
    products = Product.objects.all()

    context = {'products': products}
    return render(request, 'products/products.html', context)

@login_required(login_url="/login/")
def product_price(request, pk):
    product = get_object_or_404(Product, pk=pk)
    prices = ProductPrice.objects.filter(product_id=pk)

    context = {'product': product, 'prices': prices}
    return render(request, 'products/product_price.html', context)

@login_required(login_url="/login/")
def product_machine(request, pk):
    product = get_object_or_404(Product, pk=pk)
    machines = Machine.objects.filter(product=pk)

    context = {'product': product, 'machines': machines}
    return render(request, 'products/product_machine.html', context)

@login_required(login_url="/login/")
def product_material(request, pk):
    product = get_object_or_404(Product, pk=pk)
    materials = RawMaterial.objects.filter(product=pk)

    context = {'product': product, 'materials': materials}
    return render(request, 'products/product_material.html', context)

@login_required(login_url="/login/")
def machines(request):
    machines = Machine.objects.all()

    context = {'machines': machines}
    return render(request, 'machines/machines.html', context)