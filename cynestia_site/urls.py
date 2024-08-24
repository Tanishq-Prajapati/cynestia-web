# creating all the main website end-points over here
from django.urls import path
from .views import home

urlpatterns = [
    path("", home)
]