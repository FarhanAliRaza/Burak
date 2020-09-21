from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from . cart import Cart
from products.models import Product
from cart.models import CartProduct
from shop.models import WholeSeller, Shop
from django.contrib.auth.decorators import login_required
from ecom.utils import unique_order_id_generator
from .models import Order, ShopOrder

def add(request):
    id = request.GET.get('id')
    quantity = request.GET.get('q')
    print(quantity)
    cart = Cart(request.session)
    product = Product.objects.get(pk=id)
    price = product.price
    cart.add(product=product, quantity=quantity, price=price)
    yes = cart.is_empty
    print(yes)
    return JsonResponse({'success': "success"})


def delete(request, pk):
    id = pk
    cart = Cart(request.session)
    product = Product.objects.get(pk=id)
    cart.remove(product)
    return redirect("/ajax/cart")


def show(request):
    cart = Cart(request.session)
    no = cart.unique_count.real
    cart_dict = cart.cart_serializable
    items = cart.total.real
    total = items + 50
    obj_list = []
    for i in cart_dict:
        obj = Product.objects.get(pk=i)
        obj_dict = cart_dict[i]
        obj_dict['title'] = obj.title
        obj_dict['thumbnail'] = obj.thumbnail
        obj_dict['sub'] = obj.price * obj_dict['quantity']

        obj_list.append(obj_dict)
    print(obj_list)

    return render(request, 'cart.html', {
        'obj_list': obj_list,
        'items': items,
        'total': total,
        'no_obj': no})


@login_required
def thankyou(request):
    try:
        usr_id = request.user.id
        cart = Cart(request.session)
        cart_dict = cart.cart_serializable
        total = cart.total.real + 50
        o = Order()
        unique_id = unique_order_id_generator(o)
        for i in cart_dict:
            obj = Product.objects.get(pk=i)
            obj_dict = cart_dict[i]
            obj_dict['subtotal'] = obj.price * int(obj_dict['quantity'])
            v_obj = WholeSeller.objects.get(pk=obj.vendor)

            s_obj = Shop.objects.get(pk=usr_id)
            x = CartProduct.objects.create(
                vendor=v_obj, vendor_location=v_obj.location, product=obj, quantity=int(
                    obj_dict['quantity']),
                subtotal=int(obj_dict['subtotal']), order_id=unique_id
            )
        x = CartProduct.objects.filter(order_id=unique_id)
        o = Order.objects.create(
            ordered_by=s_obj, delivery_loaction=s_obj.location, order_id=unique_id, total=total)
        for i in x:
            o.cart.add(i)
        v_dict = {}
        for i in x:
            if i.vendor in v_dict:
                x = v_dict[i.vendor]
                x.append(i)
                v_dict[i.vendor] = x
            else:
                v_dict[i.vendor] = []
                x = v_dict[i.vendor]
                x.append(i)
                v_dict[i.vendor] = x
        for v, p in v_dict.items():
            subtotal=0
            for i in p:
                subtotal += i.subtotal
            x = ShopOrder.objects.create(wholeseller=v, order_id=unique_id, total=subtotal)
            for i in p:
                x.cart.add(i)
        # products added to database
        # now for view
        order = Order.objects.get(order_id=unique_id)
        cart_list = CartProduct.objects.filter(order_id=unique_id)
        cart.clear()
    except:
        return redirect("/")
    return render(request, 'order.html', {
        "order": order,
        "cart": cart_list,
    })


def user_order(request):
    usr_id = request.user.id
    s_obj = Shop.objects.get(pk=usr_id)
    obj_list = Order.objects.filter(ordered_by=s_obj).order_by("-timestamp")
    context = {
        "obj_list":obj_list
    }
    return render(request, 'yourorders.html', context)


def order_detail(request, pk):
    obj = Order.objects.get(pk=pk)
    cart_list = CartProduct.objects.filter(order_id=obj.order_id)
    context = {
        "order": obj,
        "cart": cart_list,
    }
    return render(request, 'orderdetail.html', context)
def clear_view(request):

    cart = Cart(request.session)
    cart.clear()
    
    return redirect('/ajax/cart')
