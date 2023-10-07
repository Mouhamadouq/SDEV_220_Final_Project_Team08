from django.db import models

# Create your models here.

class user(models.Model):
    age = models.BigIntegerField()


class ticket(models.Model):
    ticketID = models.BigIntegerField()
    ticketNum = models.BigIntegerField()
    ticket_price = models.DecimalField(max_digits=2, decimal_places= 2)
    Is_available = models.BigIntegerField()

class events(models.Model):
    event_name = models.CharField(max_length=100)
    description = models.TextField()
    date_starting = models.DateTimeField(auto_now_add=True)
    date_ending = models.DateTimeField(null=True, blank=True)
    event_place = models.CharField(max_length=150)

class ticketSystem(models.Model):
    reservation = models.BigIntegerField()
    regular_ticket = models.BigIntegerField()
