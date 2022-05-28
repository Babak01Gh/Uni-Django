from django.urls import path
from . import views

urlpatterns = [
    path('', views.ret_all),
    path('<str:pk>/', views.ret_sing),
]
