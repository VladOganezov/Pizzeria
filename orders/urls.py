from django.urls import path
from . import views

urlpatterns = [
    path('cart/', views.CartListView.as_view(), name='cart'),
    path('',  views.OrdersListView.as_view(), name='orders')
]
