from django.shortcuts import render, redirect, get_object_or_404
from products.models import Product
from shop.models import WholeSeller
from products.forms import ProductForm
from PIL import Image


# def dashboard_view(request):
#     if request.user.is_authenticated:
#         usrid = request.user.id
#         if WholeSeller.objects.is_exist(usrid):
#             template_name = 'shop/shopdashboard.html'
#             s = WholeSeller.objects.get(pk=usrid)
#         # elif Manufacturer.objects.is_exist(usrid):
#         #     template_name = 'manufacturer/shopdashboard.html'
#         #     s = Manufacturer.objects.get(pk=usrid)
#         # else:
#         #     return redirect('shop_reg')
#     else:
#         return redirect('account_login')

#     qs = Product.objects.filter(vendor=usrid)
#     context = {
#         'obj_list': qs,
#         'ven': s ,
#         }
#     return render(request, template_name, context)

#Future Update
def add_product(request):
    if request.user.is_authenticated:
        usrid = request.user.id
        if WholeSeller.objects.is_exist(usrid):
            s = WholeSeller.objects.get(vendor=usrid)
            n = s.name
        else:
            return redirect('#')
    else:
        return redirect('login')
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            f = form.save(commit=False)
            f.vendor = request.user
            f.vendor_name = n
            f.save()
            return redirect('/dashboard')

        else:
            form = ProductForm()
    template_name = 'add_product.html'
    context = {
        'form': form
        }
    return render(request, template_name, context)


def product_delete_view(request, pk):
    x = Product.objects.get(pk=pk)
    if x.vendor.pk == request.user.id:
        obj = get_object_or_404(Product, pk=pk)

        template_name = 'shop/delete.html'
        if request.method == "POST":
            obj.delete()
            return redirect("/shop")
        context = {"object": obj}
        return render(request, template_name, context)
    else:
        return redirect('home')


def product_update_view(request, pk):
    obj = get_object_or_404(Product, pk=pk)
    form = ProductForm(request.POST or None, instance=obj)
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('/shop')
    template_name = 'shop/update.html'
    context = {"title": f"Update {obj.title}", "form": form}
    return render(request, template_name, context)  


#old


# def dashboard_view(request):
#     if request.user.is_authenticated:
#         usrid = request.user.id
#         if WholeSeller.objects.is_exist(usrid):
#             template_name = 'shop/shopdashboard.html'
#             s = WholeSeller.objects.get(pk=usrid)
#         # elif Manufacturer.objects.is_exist(usrid):
#         #     template_name = 'manufacturer/shopdashboard.html'
#         #     s = Manufacturer.objects.get(pk=usrid)
#         # else:
#         #     return redirect('shop_reg')
#     else:
#         return redirect('account_login')

#     qs = Product.objects.filter(vendor=usrid)
#     context = {
#         'obj_list': qs,
#         'ven': s ,
#         }
#     return render(request, template_name, context)


# def add_product(request):
#     if request.user.is_authenticated:
#         usrid = request.user.id
#         if WholeSeller.objects.is_exist(usrid):
#             s = WholeSeller.objects.get(vendor=usrid)
#             n = s.name
#         else:
#             return redirect('#')
#     else:
#         return redirect('login')
#     form = ShopProductForm()
#     if request.method == 'POST':
#         form = ShopProductForm(request.POST, request.FILES)
#         if form.is_valid():
#             f = form.save(commit=False)
#             f.vendor = request.user
#             f.vendor_name = n
#             f.save()
#             return redirect('/dashboard')

#         else:
#             form = ProductForm()
#     template_name = 'add_product.html'
#     context = {
#         'form': form
#         }
#     return render(request, template_name, context)


# def product_delete_view(request, pk):
#     x = Product.objects.get(pk=pk)
#     if x.vendor.id == request.user.id:
#         obj = get_object_or_404(Product, pk=pk)

#         template_name = 'delete.html'
#         if request.method == "POST":
#             obj.delete()
#             return redirect("/dashboard")
#         context = {"object": obj}
#         return render(request, template_name, context)
#     else:
#         return redirect('home')


# def product_update_view(request, pk):
#     obj = get_object_or_404(Product, pk=pk)
#     form = ShopProductForm(request.POST or None, instance=obj)
#     if form.is_valid():
#         form.save()
#         return redirect('/dashboard')
#     template_name = 'add_product.html'
#     context = {"title": f"Update {obj.title}", "form": form}
#     return render(request, template_name, context)  

# def add_manufacturer_product(request):
#     if request.user.is_authenticated:
#         usrid = request.user.id
#         if Manufacturer.objects.is_exist(usrid):
#             s = Manufacturer.objects.get(vendor=usrid)
#             mc = s.main_category
#             sc = s.sub_category
#             n = s.name
#         else:
#             return redirect('shopregisterationview')
#     else:
#         return redirect('account_login')
#     form = ManufacturerProductForm()
#     if request.method == 'POST':
#         form = ManufacturerProductForm(request.POST, request.FILES)
#         if form.is_valid():
#             f = form.save(commit=False)
#             f.vendor = request.user
#             f.vendor_name = n
#             f.slug = unique_slug_generator(n)
#             f.main_category = mc
#             f.sub_category = sc
#             f.save()
#         else:
#             form = ManufacturerProductForm()
#     template_name = 'add_product.html'
#     context = {
#         'form': form
#         }
#     return render(request, template_name, context)


