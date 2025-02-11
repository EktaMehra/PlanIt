from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse

# Create your tests here.
from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse

class MembersTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='TestPassword123')

    def test_register_view_get(self):
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/register.html')

    def test_register_view_post_valid(self):
        response = self.client.post(reverse('register'), {
            'username': 'newuser',
            'password1': 'NewUserPassword123',
            'password2': 'NewUserPassword123'
        })
        self.assertEqual(response.status_code, 302)  # Redirect after successful registration
        self.assertTrue(User.objects.filter(username='newuser').exists())

    def test_register_view_post_invalid(self):
        response = self.client.post(reverse('register'), {
            'username': 'newuser',
            'password1': 'password',
            'password2': 'wrongpassword'
        })
        self.assertEqual(response.status_code, 200)  # Should reload with error
        self.assertFalse(User.objects.filter(username='newuser').exists())

    def test_login_view_get(self):
        response = self.client.get(reverse('organizer_login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'members/login.html')

    def test_login_view_post_valid(self):
        response = self.client.post(reverse('organizer_login'), {
            'username': 'testuser',
            'password': 'TestPassword123'
        })
        self.assertEqual(response.status_code, 302)  # Redirect after login

    def test_login_view_post_invalid(self):
        response = self.client.post(reverse('organizer_login'), {
            'username': 'wronguser',
            'password': 'wrongpassword'
        })
        self.assertEqual(response.status_code, 200)  # Reload with error

    def test_logout_view(self):
        self.client.login(username='testuser', password='TestPassword123')
        response = self.client.post(reverse('logout')) 
        self.assertEqual(response.status_code, 302)  # Redirect after logout


    def test_check_username_taken(self):
        response = self.client.get(reverse('check_username') + '?username=testuser')
        self.assertJSONEqual(response.content, {'is_taken': True})

    def test_check_username_available(self):
        response = self.client.get(reverse('check_username') + '?username=availableuser')
        self.assertJSONEqual(response.content, {'is_taken': False})
