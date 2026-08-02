from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse

class AuthSystemTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.username = 'testuser'
        self.email = 'testuser@example.com'
        self.password = 'password123'
        self.user = User.objects.create_user(
            username=self.username,
            email=self.email,
            password=self.password
        )

    def test_signup_view_creates_user_with_hashed_password(self):
        signup_url = reverse('signup')
        response = self.client.post(signup_url, {
            'username': 'newfoodie',
            'email': 'foodie@zomato.com',
            'password': 'securepassword'
        })
        self.assertEqual(response.status_code, 302)
        new_user = User.objects.get(username='newfoodie')
        self.assertEqual(new_user.email, 'foodie@zomato.com')
        # Check password is hashed properly
        self.assertTrue(new_user.check_password('securepassword'))
        self.assertNotEqual(new_user.password, 'securepassword')

    def test_login_and_welcome_redirect(self):
        login_url = reverse('login')
        response = self.client.post(login_url, {
            'username': self.username,
            'password': self.password
        })
        self.assertRedirects(response, reverse('welcome'))
        welcome_response = self.client.get(reverse('welcome'))
        self.assertContains(welcome_response, f'Welcome, <span class="text-primary">{self.username}</span>!')

    def test_navbar_conditional_rendering_and_logout(self):
        # Unauthenticated check
        home_res_anon = self.client.get(reverse('home'))
        self.assertContains(home_res_anon, 'Login')
        self.assertContains(home_res_anon, 'Signup')
        self.assertNotContains(home_res_anon, 'Logout')

        # Login
        self.client.login(username=self.username, password=self.password)
        home_res_auth = self.client.get(reverse('home'))
        self.assertContains(home_res_auth, self.username)
        self.assertContains(home_res_auth, 'Logout')

        # Logout
        logout_res = self.client.get(reverse('logout'))
        self.assertRedirects(logout_res, reverse('home'))

        home_res_after_logout = self.client.get(reverse('home'))
        self.assertContains(home_res_after_logout, 'Login')
        self.assertContains(home_res_after_logout, 'Signup')
        self.assertNotContains(home_res_after_logout, self.username)
