from django import forms
from django.contrib.auth.forms import UserCreationForm
from ecom.settings import AUTH_USER_MODEL
User = AUTH_USER_MODEL

class LoginForm(forms.Form):
    mobile = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Mobile No",
                "class": "form-control"
            }
        ))
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password",
                "class": "form-control"
            }
        ))


# class SignUpForm(UserCreationForm):
#     mobile = forms.IntegerField(
#         widget=forms.NumberInput(
#             attrs={
#                 "placeholder": "Mobile No",
#                 "class": "form-control"
#             }
#         ))
    
#     password1 = forms.CharField(
#         widget=forms.PasswordInput(
#             attrs={
#                 "placeholder": "Password",
#                 "class": "form-control"
#             }
#         ))
#     password2 = forms.CharField(
#         widget=forms.PasswordInput(
#             attrs={
#                 "placeholder": "Password check",
#                 "class": "form-control"
#             }
#         ))

#     class Meta:
#         model = User
#         fields = ('mobile', 'password1', 'password2')
