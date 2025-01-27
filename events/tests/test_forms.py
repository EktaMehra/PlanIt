from django.test import TestCase
from .forms import EventForm, BookingForm
from django.contrib.auth.models import User

# Test Events Form
class EventFormTest(TestCase):
    def test_event_form_valid(self):
        user = User.objects.create(username="testuser")
        form_data = {
            'name': "Test Event",
            'date': "2025-02-01",
            'description': "Test Description",
            'category': "Music",
            'location': "Test Location",
            'time': "18:00:00",
            'created_by': user.id,
        }
        form = EventForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_event_form_invalid(self):
        form = EventForm(data={})
        self.assertFalse(form.is_valid())

# Test Booking Form
class BookingFormTest(TestCase):
    def test_booking_form_valid(self):
        form_data = {
            'name': "John Doe",
            'email': "john@example.com",
        }
        form = BookingForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_booking_form_invalid(self):
        form_data = {
            'name': "",
            'email': "",
        }
        form = BookingForm(data=form_data)
        self.assertFalse(form.is_valid())