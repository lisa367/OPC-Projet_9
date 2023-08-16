from django.shortcuts import render, redirect

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Ticket
from .forms import TicketForm


class CreateTicketView(CreateView):
    template_name = "tickets_app/create_ticket.html"
    model = Ticket
    form_class = TicketForm
    # fields = "__all__"
    success_url = reverse_lazy("homepage")


class UpdateTicketView(UpdateView):
    template_name = "tickets_app/update_ticket.html"
    model = Ticket
    form_class = TicketForm
    # fields = "__all__"
    success_url = reverse_lazy("posts")


class DeleteTicketView(DeleteView):
    template_name = "tickets_app/delete_ticket.html"
    model = Ticket
    success_url = reverse_lazy("posts")


def create_ticket(request):
    context = {}
    if request.method == "POST":
        form = TicketForm(request.POST, request.FILES)
        if form.is_valid():
            new_ticket = form.save(commit=False)
            new_ticket.user = request.user
            new_ticket.save()
        return redirect("homepage")

    form = TicketForm()
    context["form"] = form

    return render(request, "tickets_app/create_ticket.html", context=context)
