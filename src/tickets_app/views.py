# from django.shortcuts import render

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Ticket
from .forms import TicketForm


class CreateTicketView(CreateView):
    template_name = "tickets_app/create_ticket.html"
    model = Ticket
    # form_class = TicketForm
    fields = "__all__"
    success_url = reverse_lazy("homepage")


class UpdateTicketView(UpdateView):
    template_name = "tickets_app/update_ticket.html"
    model = Ticket
    # form_class = TicketForm
    fields = "__all__"
    success_url = reverse_lazy("homepage")


class DeleteTicketView(DeleteView):
    template_name = "tickets_app/delete_ticket.html"
    model = Ticket
    success_url = reverse_lazy("homepage")
