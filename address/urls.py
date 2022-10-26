from django.urls import path
from . import views


urlpatterns = [
   # http://localhost:8000/address/
   path('', views.AddressListView.as_view(), name='address'),
   # http://localhost:8000/address/shipping/
   path('shipping/', views.ShippingAddressListView.as_view(), name='shipping_address'),
]
