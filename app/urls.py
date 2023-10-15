from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('purchase/<int:pk>/', views.purchase_ticket, name='purchase'),
    path('enter-confirmation-id/', views.confirmation_details, name='enter_confirmation_id'),
    path('tickets', views.tickets, name='tickets'),
    path('customer/<str:pk>/', views.customer, name='customer'),
]
