from django.contrib.auth.models import User
from django.urls import reverse
from django.test import TestCase
from .forms import ContactForm
from .models import About


class TestAboutViews(TestCase):

    def setUp(self):
        self.user = User.objects.create_superuser(
            username="myUsername", password="myPassword", email="test@test.com"
        )
        self.about = About(
            title="Title",
            slug="about.title",
            author=self.user,
            status=1,
            content="Test",
        )

        self.about.save()

    def test_render_about_detail_page_with_contact_form(self):
        response = self.client.get(
            reverse("about")
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Title", response.content)
        self.assertIn(b"Test", response.content)
        self.assertIsInstance(response.context["contact_form"], ContactForm)
