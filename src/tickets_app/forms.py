from django.forms.models import ModelForm
from .models import Ticket


class TicketForm(ModelForm):
    class Meta:
        model = Ticket
        exclude = ["time_created", "user",]
        # exclude = ["user" ]
