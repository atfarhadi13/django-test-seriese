from django.test import TestCase, SimpleTestCase

class TestHomePage(SimpleTestCase):
    def test_homepage_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_homepage_uses_correct_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'index.html')

    def test_homepage_contains_welcome_message(self):
        response = self.client.get('/')
        self.assertContains(response, 'Welcome to our Store!', status_code=200)