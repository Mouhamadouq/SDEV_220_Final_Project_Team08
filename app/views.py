from django.shortcuts import render, get_object_or_404

from app.forms import TicketPurchaseForm
from .models import ticket, event
from django.utils import timezone

# Create your views here.
#  defined a view function named home(). When calling this function, it’ll render an HTML file named home.html.


def home(request):
    events = event.objects.order_by("date")
    print(events)
    return render(request, 'app/home.html', {'events': events})


def purchase_ticket(request, pk):
    selected_event = get_object_or_404(event, pk=pk)
    ticket_types = ticket.objects.order_by("ticket_price")
    ticket_choices = [
        (ticket.ticket_type, f"{ticket.ticket_type} - ${ticket.ticket_price}") for ticket in ticket_types]

    if request.method == 'POST':
        print(request.__dict__)
        form = TicketPurchaseForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            ticket_type = request.POST.get('ticket_type')
            email = form.cleaned_data.get('email')

            print(first_name, last_name, email, ticket_type)

    else:

        form = TicketPurchaseForm(ticket_choices=ticket_choices)

    return render(request, 'app/ticket_purchase.html', {'event': selected_event, 'ticket_types': ticket_types, 'form': form})


def confirm_purchase(request):
    return render(request, 'app/confirm_purchase.html', {})
