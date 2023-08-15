from django.contrib.auth.models import User
from django.db import models as m
from django.urls import reverse

# from lit_reviews.settings import AUTH_USER_MODEL


class Ticket(m.Model):
    title = m.CharField(max_length=128)
    description = m.TextField(max_length=2048)
    user = m.ForeignKey(to=User, on_delete=m.CASCADE)
    image = m.ImageField(null=True, blank=True)
    time_created = m.DateTimeField(auto_now_add=True)

    """def get_absolute_url(self):
        return reverse("homepage")"""
