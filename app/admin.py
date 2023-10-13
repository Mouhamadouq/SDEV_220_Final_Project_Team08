from django.contrib import admin
from .models import ConfirmPurchase, ticket
from .models import event
from .models import Customer
from .models import Order

admin.site.register(Customer)
admin.site.register(ticket)
admin.site.register(event)
admin.site.register(Order)
admin.site.register(ConfirmPurchase)
# Register your models here.