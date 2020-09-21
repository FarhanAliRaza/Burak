from django import forms
from.models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['title', 'amount', 'category', 'price', 'image', "active"]


# class ManufacturerProductForm(forms.ModelForm):
#     class Meta:
#         model = Product
#         fields = ['title', 'description', 'minimum', 'price', 'image']


# class ServiceProductForm(forms.ModelForm):
#     class Meta:
#         model = Product
#         fields = ['title', 'description', 'pickup_delivery_free', 'price', 'image']

