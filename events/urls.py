from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('', views.event_list, name='event_list'),
    path('<int:pk>/', views.event_detail, name='event_detail'),
    path('new/', views.event_create, name='event_create'),
    path('<int:pk>/edit/', views.event_update, name='event_update'),
    path('<int:pk>/delete/', views.event_delete, name='event_delete'),
    path('create/', views.create_event, name='create_event'),
]
