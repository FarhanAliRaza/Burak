from django.shortcuts import render, redirect
from .forms import LoginForm
from django.contrib.auth import authenticate, login, logout

def login_view(request):
    form = LoginForm(request.POST or None)

    msg = None

    if request.method == "POST":

        if form.is_valid():
            mobile = form.cleaned_data.get("mobile")
            password = form.cleaned_data.get("password")
            mobile = int(mobile)
            user = authenticate(mobile=mobile, password=password)
            if user is not None:
                login(request, user)
                return redirect("/")
            else:
                msg = 'Invalid credentials'
        else:
            msg = 'Error validating the form'

    return render(request, "register/login.html", {"form": form, "msg": msg})
def logout_view(request):
    
    logout(request)
    return redirect("/accounts/login")
           



# def register_user(request):

#     msg = None
#     success = False

#     if request.method == "POST":
#         form = SignUpForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get("username")
#             raw_password = form.cleaned_data.get("password1")
#             user = authenticate(username=username, password=raw_password)

#             msg = 'User created.'
#             success = True

#             # return redirect("/login/")

#         else:
#             msg = 'Form is not valid'
#     else:
#         form = SignUpForm()

#     return render(request, "accounts/register.html", {"form": form, "msg": msg, "success": success})

def forgot_pass_view(request):


    return render(request, "register/forgot.html", {})

def register_msg_view(request):
    return render(request, "register/reg_msg.html", {})
