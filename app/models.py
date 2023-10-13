import uuid
from django.db import models
from django.utils import timezone
from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.

#Create a class customer 
class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=100)
    email = models.CharField(max_length=200)
    age = models.BigIntegerField(null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


# Create a class ticket to hold different ticket types and prices
class ticket(models.Model):
    TYPE = (
        ('Reservation', 'Reservation'),
        ('Balcony level', 'Balcony level'),
        ('Club level', 'Club level'),
        ('Lower level', 'Lower level'),
        ('Suite', 'Suite'),
        ('Courtside', 'Courtside'),
    )
    ticket_type = models.CharField(max_length=100, null=True, choices=TYPE)
    ticket_price = models.FloatField()
    date_created = models.DateTimeField(blank=True, null=True)

    

    def Made(self):
        self.date_created = timezone.now()
        self.save()

    def __str__(self):
        return self.ticket_type

# Create a class event to hold the many events of the website
class event(models.Model):
    EVENT = (
        ('Cleveland Cavaliers', 'Cleveland Cavaliers'),
        ('Charlotte Hornets', 'Charlotte Hornets'),
        ('Utah Jazz', 'Utah Jazz'),
        ('San Antonio Spurs', 'San Antonio Spurs'),
        ('UMilwaukee Bucks', 'UMilwaukee Bucks'),
        ('Orlando Magic', 'Orlando Magic'),
        ('Toronto Raptors', 'Toronto Raptors'),
    )
    PLACE = (
        ('Gainbridge Fieldhouse, Indianapolis, IN', 'Gainbridge Fieldhouse, Indianapolis, IN'),
    )
    event_name = models.CharField(max_length=100, choices=EVENT)
    description = models.TextField(null=True, blank=True)
    date = models.DateTimeField()
    date_ending = models.DateTimeField(null=True, blank=True)
    event_place = models.CharField(max_length=150, choices=PLACE)

    def __str__(self):
        return self.event_name

# Create a class order
class Order(models.Model):
    STATUS = (
              ('Pending','Pending'),
              ('Out of stock', 'Out of stock'),
              ('Bought', 'Bought'))
    
    customer = models.ForeignKey(Customer, null=True, on_delete= models.SET_NULL)
    events = models.ForeignKey(event, null=True, on_delete=models.SET_NULL)
    ticket= models.ForeignKey(ticket, null=True, on_delete=models.SET_NULL)
    status = models.CharField(max_length=200, null=True, choices=STATUS)
    date_bought = models.DateTimeField(blank=True, null=True)

    def purchase(self):
        self.date_bought = timezone.now()
        self.save()

    def __str__(self):
        return self.customer, self.ticket, self.status


class ConfirmPurchase(models.Model):
    event = models.ForeignKey(event, on_delete=models.CASCADE)
    ticket = models.ForeignKey(ticket, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    confirmation_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    # Add other fields related to the purchase confirmation

    def __str__(self):
        return f'Purchase Confirmation for {self.first_name} {self.last_name}'
