from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import khata, Invoice
from shop.models import Shop
from .forms import SearchForm, KhataForm, InvoiceForm
from ecom.utils import unique_order_id_generator
def khata_home(request):
    template_name="khata/khata.html"
    s_obj = Shop.objects.get(pk=request.user.id)
    k_list = khata.objects.filter(shop=s_obj)
    total = 0
    for k in k_list:
        try:
            total += k.total
        except:
            pass
    if request.method == 'POST':
    
        form = SearchForm(request.POST)
        
    
        if form.is_valid():
            query = form.cleaned_data['query']
            obj_list = khata.objects.filter(shop=s_obj, name__icontains=query)
            if not obj_list:
                obj_list = khata.objects.filter(shop=s_obj).order_by('name')

            context={
                "obj_list":obj_list,
                "form":form,
                "total":total
            }
            return render(request, template_name, context)
    else:
        form = SearchForm()
    obj_list = khata.objects.filter(shop=s_obj).order_by('name')

    context={
        "obj_list":obj_list,
        "form":form,
        "total":total
    }
    return render(request, template_name, context)
def khatadetail(request, pk):
    template_name="khata/khatadetail.html"
    khr = khata.objects.get(pk=pk)
    u_i = khr.order_id
    objs_give = Invoice.objects.filter(unique_id=u_i, give=True)
    total_give = 0
    total_get = 0
    for obj in objs_give:
        total_give += obj.amount
    objs_get = Invoice.objects.filter(unique_id=u_i, give=False)
    for obj in objs_get:
        total_get += obj.amount
    total = total_get - total_give
    obj_list = Invoice.objects.filter(unique_id=u_i)
    khr.total = total
    khr.save()
    return render(request, template_name, context={
        'obj':khr,
        "obj_list":obj_list,
        "total":total
        })

def addbuyer(request):
    shp_id = request.user.id
    form = KhataForm()
    template_name="khata/khataform.html"
    if request.method == 'POST':
        form = KhataForm(request.POST)
        obj = Shop.objects.get(pk = shp_id)
        if form.is_valid():
            name = form.cleaned_data['name']
            phone = form.cleaned_data['phone']
            o = khata()
            u_i = unique_order_id_generator(o)
            k = khata(
                shop=obj,
                name=name,
                phone=phone,
                order_id=u_i 
                )
            k.save()
            return redirect('/khata')


        
    context={
                "form":form,
            }
    return render(request, template_name, context)
def getmoney(request, pk):
    shp_id = request.user.id
    form = InvoiceForm()
    template_name="khata/invoiceget.html"
    if request.method == 'POST':
        form = InvoiceForm(request.POST)
        obj = Shop.objects.get(pk = shp_id)
        khata_obj = khata.objects.get(pk=pk)
        u_i = khata_obj.order_id
        print("f1")
        print(form.errors)
        if form.is_valid():
            print("f")
            description = form.cleaned_data['description']
            amount = form.cleaned_data['amount']
            k = Invoice(
                description=description,
                amount=amount,
                unique_id=u_i,
                give=False
                )
            k.save()
            return redirect(f'/khata/{pk}')
    context={
                "form":form,
                "pk":pk
            }
    return render(request, template_name, context)

def givemoney(request, pk):
    shp_id = request.user.id
    form = InvoiceForm()
    template_name="khata/invoicegive.html"
    if request.method == 'POST':
        form = InvoiceForm(request.POST)
        obj = Shop.objects.get(pk = shp_id)
        khata_obj = khata.objects.get(pk=pk)
        u_i = khata_obj.order_id
        print("f1")
        print(form.errors)
        if form.is_valid():
            print("f")
            description = form.cleaned_data['description']
            amount = form.cleaned_data['amount']
            k = Invoice(
                description=description,
                amount=amount,
                unique_id=u_i,
                give=True
                )
            k.save()
            return redirect(f'/khata/{pk}')
    context={
                "form":form,
                "pk":pk
            }
    return render(request, template_name, context)

def invoicedetail(request, pk):
    template_name="khata/invoicedetail.html"
    obj = Invoice.objects.get(pk=pk)
    context={
                "obj":obj
            }
    return render(request, template_name, context)
