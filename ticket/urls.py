from django.urls import path
from . import views

urlpatterns = [
    path('tickets/', views.tickets, name='tickets'),
    path('create-ticket', views.create_ticket, name='create-ticket'),
    path('ticket-detail/<int:pk>/', views.ticket_detail, name='ticket-detail'),
    path('update-ticket/<int-pk>/', views.update_ticket, name='update-ticket'),
    path('pending-tickets/', views.pending_tickets, name='pending-tickets'),
    path('delete-ticket/<int:pk>/', views.delete_ticket, name='delete-ticket'),
    path('accept-ticket/', views.accept_ticket, name='accept-ticket'),
    path('close-ticket/', views.close_ticket, name='close-ticket'),
    path('workspace/', views.workspace, name='workspace'),
    path('closed-tickets/', views.closed_tickets, name='closed-tickets'),
]
