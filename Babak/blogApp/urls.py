from django.urls import path
from . import views

urlpatterns = [
    path('', views.ret_all),
    path('<str:slug>/', views.ret_sing),
]
