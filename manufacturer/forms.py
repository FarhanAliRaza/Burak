from django import forms
from.models import Manufacturer


class MaufacturerRegisterationForm(forms.ModelForm):
    class Meta:
        model = Manufacturer
        fields = ['profile_pic', 'name', 'sub_category', 'manufactured_product']