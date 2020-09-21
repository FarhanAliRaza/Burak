from django.urls import path
from .views import add_product, product_delete_view, product_update_view
app_name='dashboard'
urlpatterns = [
    # path('', dashboard_view, name='dashboard'),
    # path('add_product/', add_product, name='add_product'),
    # path('delete/<int:pk>/', product_delete_view, name='product_delete' ),
    # path('edit/<int:pk>/', product_update_view, name='product_update' ),
]
