from django.urls import path
from .views import CreateTicketView, UpdateTicketView, DeleteTicketView

app_name = "tickets_app"

urlpatterns = [
    path("create/", CreateTicketView.as_view(), name="create-ticket"),
    path("update/<int:pk>", UpdateTicketView.as_view(), name="update-ticket"),
    path("delete/<int:pk>", DeleteTicketView.as_view(), name="delete-ticket"),
]
