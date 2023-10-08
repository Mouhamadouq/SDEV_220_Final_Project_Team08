from django import forms

class TicketPurchaseForm(forms.Form):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    email = forms.EmailField()
    # ticket_num = forms.IntegerField(min_value=1, label='Ticket Number')
    # credit_card_number = forms.CharField(max_length=16, label='Credit Card Number')
    # expiration_date = forms.CharField(max_length=5, label='Expiration Date (MM/YY)')
    # cvv = forms.CharField(max_length=3, label='CVV')



