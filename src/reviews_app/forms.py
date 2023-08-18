# from django.forms import ModelForm, RadioSelect
from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):
    CHOICES = [
        (0, 0),
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
    ]

    headline = forms.CharField(max_length=120, label="Titre")
    rating = forms.ChoiceField(
        widget=forms.RadioSelect(attrs={"id": "note"}), choices=CHOICES, label="Note"
    )
    body = forms.CharField(
        widget=forms.Textarea(attrs={"placeholder": "Ecrivez un commentaire"}),
        label="Commentaire",
    )

    class Meta:
        model = Review
        exclude = ["time_created", "user", "ticket"]
        # widgets = {"rating": RadioSelect}
        # labels = {"": ()}
