from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('purchase/<int:pk>/', views.purchase_ticket, name='purchase'),
    path('confirm_purchase/', views.confirm_purchase, name='confirm_purchase'),
]

