# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin

from .models import *
# Register your models here.


admin.site.register(Customer)
admin.site.register(Machine)
admin.site.register(MTag)
admin.site.register(RawMaterial)
admin.site.register(Product)
admin.site.register(ProductPrice)