from django import forms


class TicketPurchaseForm(forms.Form):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    email = forms.EmailField()
    ticket_type = forms.ChoiceField(choices=[])

    def __init__(self, *args, **kwargs):
        # Pass the ticket types as choices when initializing the form
        ticket_choices = kwargs.pop('ticket_choices', [])
        super(TicketPurchaseForm, self).__init__(*args, **kwargs)
        self.fields['ticket_type'].choices = ticket_choices
