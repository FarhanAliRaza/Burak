from django.urls import path, re_path
from .views import filling_orders, home, order_detail, shop_order_cmplt, delivering_orders, order_detail_shop, order_cmplt
app_name = 'driver'
urlpatterns = [
    path('', home, name='homedriver'),
    path('deliver/', delivering_orders, name='delivering_orders'),
    path('fill/', filling_orders, name='filling_orders'),
    path('detail/<int:pk>/', order_detail, name='detail'),
    path('detailshop/<int:pk>/', order_detail_shop, name='detail'),
    path('<int:pk>/cmplt', shop_order_cmplt, name='shop_order_cmplt'),
    path('shop/<int:pk>/cmplt', order_cmplt, name='order_cmplt'),


]
