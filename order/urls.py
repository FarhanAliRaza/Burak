from django.urls import path, re_path
from .views import add, clear_view, show, delete, thankyou, user_order, order_detail
app_name = 'order'
urlpatterns = [

    path('add', add, name='add'),
    path('delete/<int:pk>/', delete, name='delete'),
    path('clear/', clear_view, name='clear'),
    path('cart/', show, name='show'),
    path('cart/thankyou', thankyou, name='thankyou'),
    path('orders/', user_order, name='oips'),
    path('order/<int:pk>/', order_detail, name='detail'),

]
