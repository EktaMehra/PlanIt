from django.test import TestCase, Client
from django.urls import reverse
from .models import Event, Booking
from django.contrib.auth.models import User

class EventViewsTest(TestCase):
    # CRUD and view-related tests and validations
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username="testuser", password="testpassword")
        self.event = Event.objects.create(
            name="Test Event",
            date="2025-02-01",
            description="Test Description",
            category="Music",
            location="Test Location",
            time="18:00:00",
            created_by=self.user,
        )