from django.forms import ModelForm
from django import forms
from .models import Order


class TicketPurchaseForm(forms.Form):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    email = forms.EmailField()
    ticket_type = forms.ChoiceField(choices=[])

    def __init__(self, *args, **kwargs):
        ticket_choices = kwargs.pop('ticket_choices', [])
        super(TicketPurchaseForm, self).__init__(*args, **kwargs)
        print("from form")
        print(ticket_choices)
        self.fields['ticket_type'].choices = ticket_choices

#class OrderForm(ModelForm):
 #   class Meta:
  #      model = Order
   #     fields = '__all__'


class ConfirmationIdForm(forms.Form):
    confirmation_id = forms.CharField(max_length=36, label='Confirmation ID')

