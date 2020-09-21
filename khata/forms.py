from django import forms
from .models import khata, Invoice
class SearchForm(forms.Form):
    query = forms.CharField(max_length=100)

class KhataForm(forms.ModelForm):
    class Meta:
        model = khata
        fields = ['name', 'phone']

class InvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = ['description', 'amount']



