from django.urls import path
from . import views

urlpatterns = [
    path('sendemail/', views.send_email),
]