from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models as m
from django.urls import reverse
from django.contrib.auth.models import User

# from lit_reviews.settings import AUTH_USER_MODEL
from tickets_app.models import Ticket


class Review(m.Model):
    # ticket = m.CharField(max_length=128)
    ticket = m.ForeignKey(to=Ticket, on_delete=m.CASCADE)
    headline = m.CharField(max_length=128)
    rating = m.PositiveSmallIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(5)]
    )
    user = m.ForeignKey(to=User, on_delete=m.CASCADE)
    body = m.TextField(max_length=8192)
    time_created = m.DateTimeField(auto_now_add=True)

    """def get_absolute_url(self):
        return reverse("homepage")"""


# from django.contrib.auth.models import User
# from django.db import models as m
# from .settings import AUTH_USER_MODEL


class UserFollows(m.Model):
    user = m.ForeignKey(to=User, on_delete=m.CASCADE)
    followed_user = m.ForeignKey(
        to=User, on_delete=m.CASCADE, related_name="followed_by"
    )

    class Meta:
        pass
        unique_together = (
            "user",
            "followed_user",
        )
