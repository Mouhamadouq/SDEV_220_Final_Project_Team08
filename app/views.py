from django.shortcuts import render, get_object_or_404

from app.forms import TicketPurchaseForm
from .models import ticket, events
from django.utils import timezone

# Create your views here.
#  defined a view function named home(). When calling this function, it’ll render an HTML file named home.html.
def home(request):
    return render(request, 'app/home.html', {})

def purchase_ticket(request, ticket_id):
    print("rashmi baral")
    # print(get_object_or_404(events, pk=1))
    # try:
    #     ticket = Ticket.objects.get(ticketNum=ticket_id)
    # except Ticket.DoesNotExist:
    #     # Handle the case where the specified ticket number does not exist
    #     return redirect('ticket_not_found')  # Redirect to a not found page or display an error message

    if request.method == 'POST':
        form = TicketPurchaseForm(request.POST)
        # if form.is_valid():
        #     # Handle ticket purchase logic here (e.g., update the database)
        #     return redirect('purchase_success')  # Redirect to a success page
    else:
        form = TicketPurchaseForm()

    ticket1 = ticket(1, 1, 30, 1)

    return render(request, 'app/ticket_purchase.html', {'ticket': ticket1, 'form': form})

def confirm_purchase(request):
    return render(request, 'app/confirm_purchase.html',{})

