from django.urls import path,   path
from .views import (
    add,
    remove,
    show,

)
app_name = 'cart'
urlpatterns = [
    path('add/<int:id>', add, name='cart_add'),
    path('remove/<int:id>', remove, name='cart_remove'),
    path('show/', show, name='cart_show'),
]

