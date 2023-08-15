# models.py
"""

from django.conf import settings
from django.contrib.auth.models import User
from django.db import models as m
# from .settings import AUTH_USER_MODEL


class UserFollows(m.Model):
    user = m.ForeignKey(to=User, on_delete=m.CASCADE)
    followed_user = m.ForeignKey(
        to=User, on_delete=m.CASCADE, related_name="followed_by"
    )

    class Meta:
        unique_together =('user', 'followed_user', )
"""