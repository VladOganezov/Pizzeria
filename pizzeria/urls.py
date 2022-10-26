from django.conf.urls import handler404
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
     path('admin/', admin.site.urls),
     path('accounts/', include('accounts.urls')),
     path('accounts/', include('allauth.urls')),
     path('accounts/', include('django.contrib.auth.urls')),
     path('address/', include('address.urls')),
     path('menu/', include('menu.urls')),
     path('orders/', include('orders.urls')),
     path('', include('pages.urls')),
     path('api/', include('api.urls')),
]

handler404 = 'pages.views.error_404'