from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    # http://localhost:8000/accounts/sign_up/
    path('sign_up/', views.SignUpListView.as_view(), name='signup'),
    # http://localhost:8000/accounts/sign_in/
    path('sign_in/', views.SignInListView.as_view(), name='signin'),
    # http://localhost:8000/accounts/profile/
    path('profile/', views.ProfileListView.as_view(), name='profile'),
    # http://localhost:8000/accounts/email/
    path('email/', views.EmailListView.as_view(), name='email'),
]
