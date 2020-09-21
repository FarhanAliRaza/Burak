from django.shortcuts import render, redirect
from order.models import Order, CartProduct, ShopOrder
import datetime

def home(request):
    usr_id = request.user.id
    context = {}
    return render(request, 'homedriver.html', context)
def filling_orders(request):
    if request.user.is_driver or request.user.is_admin:
    
        previous = datetime.date.today() - datetime.timedelta(days=4)
        #timestamp__startswith=previous
        obj_list = ShopOrder.objects.filter().order_by("-timestamp")
        context = {
            "obj_list":obj_list
        }
        return render(request, 'filling.html', context)
    else:
        redirect("/")

def order_detail(request, pk):
    obj = ShopOrder.objects.get(pk=pk)
    cart_list = CartProduct.objects.filter(order_id=obj.order_id)
    context = {
        "obj_list": cart_list,
        "pk": pk,
    }
    return render(request, 'driverdetail.html', context)

def shop_order_cmplt(request, pk):
    obj = ShopOrder.objects.get(pk=pk)
    obj.is_complete = True
    obj.save()
    return redirect('/burak/fill')

def order_cmplt(request, pk):
    obj = Order.objects.get(pk=pk)
    obj.is_complete = True
    obj.save()
    return redirect('/burak/deliver')
def delivering_orders(request):
    if request.user.is_driver or request.user.is_admin:
    
        previous = datetime.date.today() - datetime.timedelta(days=4)
        #timestamp__startswith=previous
        obj_list = Order.objects.filter().order_by("-timestamp")
        context = {
            "obj_list":obj_list
        }
        return render(request, 'delivering.html', context)
    else:
        redirect("/")

def order_detail_shop(request, pk):
    obj = Order.objects.get(pk=pk)
    cart_list = CartProduct.objects.filter(order_id=obj.order_id)
    context = {
        "obj_list": cart_list,
        "pk": pk,
        'ord':obj
    }
    return render(request, 'driverdetailshop.html', context)
