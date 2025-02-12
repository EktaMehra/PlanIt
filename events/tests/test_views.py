from django.test import TestCase, Client
from django.urls import reverse
from events.models import Event, Booking
from django.contrib.auth.models import User


class EventViewsTest(TestCase):
    # CRUD and view-related tests and validations
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username="testuser", password="testpassword")
        self.event = Event.objects.create(
            name="Test Event",
            date="2025-02-01",
            description="A Test event Description",
            category="Music",
            location="Test Location",
            time="18:00:00",
            created_by=self.user,
        )

    def test_event_list_view(self):
        self.client.login(username="testuser", password="testpassword")
        response = self.client.get(reverse("event_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Event")

    def test_event_detail_view(self):
        response = self.client.get(reverse("event_detail", args=[self.event.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Event")

    def test_create_event_view(self):
        self.client.login(username="testuser", password="testpassword")
        response = self.client.post(reverse("create_event"), {
            'name': "New Event",
            'date': "2025-02-02",
            'description': "New Description",
            'category': "Workshop",
            'location': "New Location",
            'time': "15:00:00",
            'created_by': self.user.id,
        })
        self.assertEqual(response.status_code, 302)  # Redirect after creation

    def test_update_event_view(self):
        self.client.login(username="testuser", password="testpassword")
        response = self.client.post(reverse("event_update", args=[self.event.id]), {
            'name': "Updated Event",
            'date': "2025-02-03",
            'description': "Updated Description",
            'category': "Conference",
            'location': "Updated Location",
            'time': "10:00:00",
        })
        self.assertEqual(response.status_code, 302)
        self.event.refresh_from_db()
        self.assertEqual(self.event.name, "Updated Event")

    def test_delete_event_view(self):
        self.client.login(username="testuser", password="testpassword")
        response = self.client.post(reverse("event_delete", args=[self.event.id]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Event.objects.filter(id=self.event.id).exists())
