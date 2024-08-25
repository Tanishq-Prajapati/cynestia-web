# creating all the main website end-points over here
from django.urls import path
from .views import CustomView, ContactView

urlpatterns = [
    path("", CustomView.as_view()),
    path("contact", ContactView.as_view())
]