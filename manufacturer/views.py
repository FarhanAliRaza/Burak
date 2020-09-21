from django.shortcuts import render, redirect
from.models import Manufacturer

from .forms import MaufacturerRegisterationForm


def manufacturer_registeration_view(request):
    if request.user.is_authenticated:
        s = Manufacturer.objects.filter(vendor_id= request.user.id)
        if s:
            return redirect('home')

        userinstance = request.user
        form = MaufacturerRegisterationForm()
        if request.method == 'POST':
            form = MaufacturerRegisterationForm(request.POST, request.FILES)
            if form.is_valid():
                f = form.save(commit=False)
                f.vendor = userinstance
                f.main_category = 'Shop'
                f.save()
        else:
            form = MaufacturerRegisterationForm()
        template_name = 'manufacture/manufacturerregister.html'
        context = {
            'form': form
               }
        return render(request, template_name, context)
    else:
        return redirect('account_signup')
