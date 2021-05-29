from django.urls import path
from . import views


urlpatterns = [
    path('contact/', views.ContactView.as_view(), name="contact"),
    path('about/', views.AboutView.as_view(), name="about"),
    path('feedback/', views.CreateContact.as_view(), name="feedback"),
]
