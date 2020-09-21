from django.shortcuts import render, redirect
from.models import Service

from .forms import ServiceRegisterationForm


def service_registeration_view(request):
    if request.user.is_authenticated:
        s = Service.objects.filter(vendor_id= request.user.id)
        if s:
            return redirect('home')

        userinstance = request.user
        form = ServiceRegisterationForm()
        if request.method == 'POST':
            form = ServiceRegisterationForm(request.POST, request.FILES)
            if form.is_valid():
                f = form.save(commit=False)
                f.vendor = userinstance
                f.main_category = 'Shop'
                f.save()
        else:
            form = ServiceRegisterationForm()
        template_name = 'service/serviceregister.html'
        context = {
            'form': form
               }
        return render(request, template_name, context)
    else:
        return redirect('account_signup')
