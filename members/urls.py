from django.urls import path
from .views import EventOrganizerLoginView

urlpatterns = [
    path('login/', EventOrganizerLoginView.as_view(), name='organizer_login'),
    path('register/', views.register, name='register'),
]

print("Members URLs loaded successfully.")