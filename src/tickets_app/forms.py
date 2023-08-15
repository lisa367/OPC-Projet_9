from django import forms
from .models import Ticket


class TicketForm(forms.ModelForm):
    title = forms.CharField(max_length=120, label='Titre')
    
    class Meta:
        model = Ticket
        exclude = ["time_created", "user",]
        # exclude = ["user" ]
