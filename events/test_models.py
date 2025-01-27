from .models import Event, Booking
from django.test import TestCase
from django.contrib.auth.models import User


# Test Event Model
class EventModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username="testuser")
        self.event = Event.objects.create(
            name= "Test Event",
            date= "2025-02-01",
            description= "Test Description",
            category= "Music",
            location= "Test Location",
            time= "18:00:00",
            created_by= self.user
        )

    def test_event_creation(self):
        self.assertEqual(self.event.name, "Test Event")
        self.assertEqual(self.event.created_by, self.user)


# Test Booking Model
class BookingModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username="testuser")
        self.event = Event.objects.create(
            name="Test Event",
            date="2025-02-01",
            description="Test Description",
            category="Music",
            location="Test Location",
            time="18:00:00",
            created_by=self.user,
        )

        self.booking = Booking.objects.create(
            event=self.event,
            name="John Doe",
            email="john@example.com",
        )

    def test_booking_creation(self):
        self.assertEqual(self.booking.name, "John Doe")
        self.assertEqual(self.booking.event, self.event)

