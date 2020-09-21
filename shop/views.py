from django.shortcuts import render, redirect, get_object_or_404
from.models import Shop, WholeSeller
from products.models import Product
from .forms import WholeSellerRegForm
from order.models import Order, ShopOrder
from cart.models import CartProduct
from django.contrib.auth.decorators import login_required
from khata.models import khata

def whole_seller_registeration_view(request):
    if request.user.is_authenticated:
        s = Shop.objects.filter(vendor_id= request.user.id)
        if s:
            return redirect('home')

        userinstance = request.user
        form = WholeSellerRegForm()
        if request.method == 'POST':
            form = ShopRegisterationForm(request.POST, request.FILES)
            if form.is_valid():
                f = form.save(commit=False)
                f.vendor = userinstance
                f.save()
        else:
            form = WholeSellerRegForm()
        template_name = 'shop/shopregister.html'
        context = {
            'form': form
               }
        return render(request, template_name, context)
    else:
        return redirect('account_signup')


def shop_view(request):
    # if request.user.is_vendor:
    #     usr_id = request.user.id
    #     w_obj = WholeSeller.objects.get(pk=usr_id)
    #     act_obj_list = ShopOrder.objects.filter(wholeseller=w_obj, is_complete=True).order_by("-timestamp")
    #     t_obj_list = ShopOrder.objects.filter(wholeseller=w_obj, is_complete=False).order_by("-timestamp")
    #     active = len(act_obj_list)
    #     inactive = len(t_obj_list)
    #     obj_list = ShopOrder.objects.filter(wholeseller=w_obj).order_by("-timestamp")
    #     total_orders = len(obj_list)
    #     total = 0
    #     for obj in obj_list:
    #         total += obj.total
    #     context = {
    #         'active': active,
    #         'inactive': inactive,
    #         'total_orders': total_orders,
    #         'total': total,
    #         "obj_list" : active,

    #     }
    #     template_name = "shop/vendordashboard.html"
    # else:
    usr_id = request.user.id
    template_name = "shop/dashboard.html"
    s_obj = Shop.objects.get(pk=usr_id)
    obj_list = Order.objects.filter(ordered_by=s_obj, is_complete=False).order_by("-timestamp")
    objs = Order.objects.filter(ordered_by=s_obj).order_by("-timestamp")
    total=0
    for i in objs:
        total += i.total 
    k_list = khata.objects.filter(shop=s_obj)
    k_total = 0
    for k in k_list:
        try:
            k_total += k.total
        except:
            pass
    context = {
        "order_no":len(obj_list),
        "total": total,
        "ktotal": k_total
    }
    return render(request, template_name, context)

def shop_product_view(request):
    if request.user.is_vendor:
        usr_id = request.user.id
        w_obj = WholeSeller.objects.get(pk=usr_id)
        context = {
            'obj_list': obj_list
        }
        template_name = "shop/list.html"
    else:
        usr_id = request.user.id
        template_name = "dashboard.html"
        s_obj = Shop.get_object_or_404(pk=usr_id)
        obj_list = Order.objects.filter(ordered_by=s_obj, is_complete=False).order_by("-timestamp")
        objs = Order.objects.filter(ordered_by=s_obj).order_by("-timestamp")
        total=0
        for i in objs:
            total += i.total 

        context = {
            "order_no":len(obj_list),
            "total": total
        }
    return render(request, template_name, context)

