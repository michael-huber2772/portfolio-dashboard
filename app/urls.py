# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from app import views

urlpatterns = [

    # The home page
    path('', views.index, name='home'),

    path('customers/', views.customers, name='customers'),
    path('products/', views.products, name='products'),
    path('products/<str:pk>/', views.product, name='product'),

    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),

]
