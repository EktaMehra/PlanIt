from django.urls import path
from . import views
from .views import EventOrganizerLoginView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', EventOrganizerLoginView.as_view(), name='organizer_login'),
    path('register/', views.register, name='register'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
