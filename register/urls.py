from django.urls import path
from .views import login_view, forgot_pass_view, logout_view, register_msg_view
# from shop.views import shop_registeration_view
# from manufacturer.views import manufacturer_registeration_view
# from service.views import service_registeration_view

urlpatterns = [
    # path('shop/', shop_registeration_view, name='shop_reg'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('forgot/', forgot_pass_view, name='forgot'),
    path('register-msg/', register_msg_view, name='reg_msg'),


]