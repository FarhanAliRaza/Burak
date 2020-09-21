from django import forms
from.models import WholeSeller


class WholeSellerRegForm(forms.ModelForm):
    class Meta:
        model = WholeSeller
        fields = ['profile_pic', 'name', 'location']