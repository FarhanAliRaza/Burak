from django.urls import path, re_path
from .views import shop_view
from dashboard.views import product_delete_view, product_update_view
app_name = 'shop'
urlpatterns = [

    path('', shop_view , name='shopview'),
    path('delete/<int:pk>/', product_delete_view, name='product_delete' ),
    path('edit/<int:pk>/', product_update_view, name='product_update' ),

    # path('<int:pk>/', shop_view, name='shops')
]