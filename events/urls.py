from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
]

print("Events URLs loaded successfully.")