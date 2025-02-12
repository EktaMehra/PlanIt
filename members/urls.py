from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
from .views import EventOrganizerLoginView, check_username
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', EventOrganizerLoginView.as_view(), name='organizer_login'),
    path('register/', views.register, name='register'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('check-username/', check_username, name='check_username'),
]
