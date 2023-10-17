import datetime
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CreateTicketForm, UpdateTicketForm
from .models import Ticket


#Ticket detail view
def ticket_detail(request, pk):
    ticket = Ticket.objects.get(pk=pk)
    context = {'ticket': ticket}
    return render(request, 'ticket/ticket_detail.html', context)


''' Client Views '''


#Create ticket for client
def create_ticket(request):
    if request.method == 'POST':
        form = CreateTicketForm(request.POST)
        if form.is_valid():
            temp = form.save(commit=False)
            temp.created_by = request.user
            temp.ticket_state = 'Pending'
            temp.save()
            messages.success(request, 'Ticket created successfully')
            return redirect('dashboard')
        else:
            messages.warning(
                request, 'Something went wrong, kindly check your form inputs')
            return redirect('create-ticket')
    else:
        form = CreateTicketForm()
        context = {'form': form}
    return render(request, 'ticket/create_ticket.html', context)


# Update ticket view
def update_ticket(request, pk):
    ticket = Ticket.objects.get(id=pk)
    if request.method == 'POST':
        form = UpdateTicketForm(request.POST, instance=ticket)
        if form.is_valid():
            temp = form.save(commit=False)
            temp.updated_by = request.user
            ticket.updated_at = datetime.datetime.now()
            temp.save()
            messages.success(request, 'Ticket updated successfully')
            return redirect('dashboard')
        else:
            messages.warning(
                request, 'Something went wrong, kindly check your form inputs')
            return redirect('update-ticket', pk)
    else:
        form = UpdateTicketForm(instance=ticket)
        context = {'form': form}
    return render(request, 'ticket/update_ticket.html', context)


#Delete ticket
def delete_ticket(request, pk):
    ticket = Ticket.objects.get(id=pk)
    ticket.delete()
    messages.success(request, 'Ticket deleted successfully')
    return redirect('dashboard')


#View for all tickets for clients
def tickets(request):
    tickets = Ticket.objects.filter(created_by=request.user)
    context = {'tickets': tickets}
    return render(request, 'ticket/tickets.html', context)


''' Engineer Views '''


#Pending customer ticket list
def pending_tickets(request):
    tickets = Ticket.objects.filter(ticket_state='Pending')
    context = {'tickets': tickets}
    return render(request, 'ticket/pending_tickets.html', context)


# Accept pending tickets
def accept_ticket(request, pk):
    ticket = Ticket.objects.get(pk=pk)
    ticket.assigned_to = request.user
    ticket.ticket_state = 'Open'
    ticket.accepted_date = datetime.datetime.now()
    ticket.save()
    messages.info(request,
                  'Ticket accepted successfully, kindly resolve on time')
    return redirect('pending_tickets')


# Close pending ticket
def close_ticket(request, pk):
    ticket = Ticket.objects.get(id=pk)
    ticket.ticket_state = 'Closed'
    ticket.is_resolved = True
    ticket.closed_date = datetime.datetime.now()
    ticket.closed_by = request.user
    ticket.save()
    messages.info(request, 'Ticket closed successfully')
    return redirect('pending_tickets')


# Tickets in Engineer's workspace
def workspace(request):
    tickets = Ticket.objects.filter(assigned_to=request.user,
                                    is_resolved=False)
    context = {'tickets': tickets}
    return render(request, 'ticket/workspace.html', context)


# All closed tickets for Engineer
def closed_tickets(request):
    tickets = Ticket.objects.filter(assigned_to=request.user, is_resolved=True)
    context = {'tickets': tickets}

    return render(request, 'ticket/closed_tickets.html', context)
