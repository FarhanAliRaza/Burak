from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from products.models import Product, Category
from order.cart import Cart
from shop.models import Shop




def home(request):
    cart = Cart(request.session)
    no = cart.unique_count.real
    qs = Product.objects.all()
    cat_list = Category.objects.all()
    context = {
        'no_obj':no,
        "cat_list": cat_list
    }

    template_name= 'home.html'
    return render(request, template_name, context)