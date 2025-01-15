from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
]

print("Members URLs loaded successfully.")