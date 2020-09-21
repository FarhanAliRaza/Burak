from django.urls import path, re_path

from .views import list_view
app_name = 'products'
urlpatterns = [

    path('<slug:slug>/', list_view, name='list')
]
