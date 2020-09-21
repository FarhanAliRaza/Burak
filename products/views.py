from django.shortcuts import render, redirect, get_object_or_404
# from shop.models import Shop
# from manufacturer.models import Manufacturer
from.models import Product, Category
from order.cart import Cart
# def detail_view(request, pk):
#     obj = Product.objects.get(pk=pk)
#     v_id = obj.vendor
#     mc = obj.main_category
#     if mc == "Shop":
#         s = Shop.objects.get(pk=v_id)
#         context = {
#             'obj': obj,
#             'ven': s,
#         }
#         template_name = 'products/detail.html'

#         return render(request, template_name, context)
#     else:
#         s = Manufacturer.objects.get(pk=v_id)
#         context = {
#             'obj': obj,
#             'ven': s,
#         }

#         template_name = 'products/detail.html'

#         return render(request, template_name, context)

def list_view(request, slug):
    cart = Cart(request.session)
    no = cart.unique_count.real
    c = Category.objects.get(slug=slug)
    obj_list = Product.objects.filter(category=c)
    context = {
            'obj_list': obj_list,
            'no_obj':no
        }
    template_name = 'products/list.html'

    return render(request, template_name, context)

