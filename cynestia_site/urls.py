# creating all the main website end-points over here
from django.urls import path
from .views import (
    CustomView, 
    ContactView,
    BlogsGrid,
    BlogDetails
)

urlpatterns = [
    path("", CustomView.as_view()),
    path("contact", ContactView.as_view()),
    path("blogs", BlogsGrid.as_view()),
    path("blogs/<slug:slug>", BlogDetails.as_view())
]