from django.contrib import admin
from . import settings
from django.urls import path, re_path
from home.views import home
from django.urls import include
from django.conf.urls.static import static
from register.views import login_view, forgot_pass_view
from search.views import search
urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path('products/', include('products.urls'), name='products'),
    path('accounts/', include('register.urls'), name='register'),
    path('dashboard/', include('dashboard.urls'), name='shopdashboard'),
    path('search/', include('search.urls'), name='search'),
    path('search-page/', search),
    path('shop/', include('shop.urls')),
    path('ajax/', include('order.urls')),
    path('khata/', include('khata.urls'), name='khata'),
    path('burak/', include('driver.urls'), name='driver'),
    path('', include('pwa.urls')), 

]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
