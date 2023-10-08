from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('purchase/<int:ticket_id>/', views.purchase_ticket, name='purchase'),
]

