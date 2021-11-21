from django.urls import path
from .views import CreateContact, ContactView, AboutView

urlpatterns = [
    path("about", AboutView.as_view(), name="about"),
    path("contact", ContactView.as_view(), name="contact"),
    path("feedback", CreateContact.as_view(), name="feedback"),

]
