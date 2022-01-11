from django.urls import path
from django.views.generic.base import View
from . import views

urlpatterns = [
    path('', views.Login, name='login'),
    path('logout', views.Logout, name="logout"),
    path('accounts/', views.AccountCreate.as_view(), name='accounts'),
    path('accounts/home/', views.home, name='home')
]