from django.urls import path, re_path
from .views import (
    CreateReviewView,
    UpdateReviewView,
    DeleteReviewView,
    create_review,
    create_review_and_ticket,
)

app_name = "reviews_app"

urlpatterns = [
    # path("create/<int:ticket_id>", CreateReviewView.as_view(), name="create-review"),
    path("create/<int:ticket_id>", create_review, name="create-review"),
    path("update/<int:pk>", UpdateReviewView.as_view(), name="update-review"),
    path("delete/<int:pk>", DeleteReviewView.as_view(), name="delete-review"),
    path(
        "create-review-and-ticket/",
        create_review_and_ticket,
        name="create-review-ticket",
    ),
]
