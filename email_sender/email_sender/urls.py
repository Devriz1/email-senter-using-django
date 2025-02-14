from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('emails.urls')),  # Add this line
]
