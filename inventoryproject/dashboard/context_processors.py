from django.contrib.auth.models import User

from .models import Order, Product


def menu_products(request):
    return {"products_list": Product.objects.all()}


def menu_orders(request):
    return {"orders_list": Order.objects.all()}


def menu_staff(request):
    return {"workers_list": User.objects.all()}
