from django.contrib import admin

from .models import Category, Order, Product

admin.site.site_header = 'SergeiDashboard'


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'quantity']
    list_filter = ['category']


admin.site.register(Product, ProductAdmin)
admin.site.register(Order)
admin.site.register(Category)