from django.urls import path
from . import views

urlpatterns = [
    path("", views.chat_view, name="chat"),  # Add this line
    path("completions/", views.chat_completions, name="chat_completions"),
]
