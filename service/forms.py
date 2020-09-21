from django import forms
from.models import Service


class ServiceRegisterationForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['profile_pic', 'name', 'sub_category', 'free_pickup_and_delivery']