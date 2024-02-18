from django.contrib import admin

# Register your models here.
from .models import *
class AdminProduct(admin.ModelAdmin):
    list_display = ['name', 'price', 'category']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']


# admin.site.register(
# [Category,Customer,Products,Order]
#     )
admin.site.register(Category)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(Products)
