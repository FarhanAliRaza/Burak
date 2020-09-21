from django.urls import path, re_path
from .views import khata_home, addbuyer, khatadetail, getmoney, givemoney, invoicedetail
app_name = 'khata'
urlpatterns = [

    path('', khata_home, name='query'),
    # path('delete/<int:pk>/', delete, name='delete'),
    path('invoice/<int:pk>/', invoicedetail, name='invoicedetail'),
    path('add/', addbuyer, name='addbuyer'),
    path('give/<int:pk>/', givemoney , name='givemoney'),
    path('get/<int:pk>/', getmoney , name='getmoney'),
    path('<int:pk>/', khatadetail , name='detail'),

]
