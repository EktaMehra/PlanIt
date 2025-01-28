from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('', views.event_list, name='event_list'),
    path('<int:id>/details/', views.event_detail, name='event_detail'),
    path('create/', views.create_event, name='create_event'),
    path('<int:id>/edit/', views.event_update, name='event_update'),
    path('<int:id>/delete/', views.event_delete, name='event_delete'),
    path('<int:id>/confirmation/', views.booking_confirmation, name='booking_confirmation'),
]
