from django.test import TestCase
from .forms import ContactForm
from django.urls import reverse


class TestContactForm(TestCase):

    def test_form_is_valid(self):
        """Test for all fields"""
        form = ContactForm(
            {"name": "Bob", "email": "test@test.com", "message": "Hello!"}
        )
        self.assertTrue(form.is_valid(), msg="Contact Form is not valid")

    def test_form_is_invalid_name(self):
        contact_form = ContactForm(
            {"name": "", "email": "test@test.com", "message": "Hello!"}
        )
        self.assertFalse(
            contact_form.is_valid(), msg="Contact Form is valid, Name included"
        )

    def test_form_is_invalid_email(self):
        contact_form = ContactForm(
            {"name": "Bob", "email": "", "message": "Hello!"}
        )
        self.assertFalse(
            contact_form.is_valid(),
            msg="Contact Form is valid, email included",
        )

    def test_form_is_invalid_message(self):
        contact_form = ContactForm(
            {"name": "Bob", "email": "test@test.com", "message": ""}
        )
        self.assertFalse(
            contact_form.is_valid(),
            msg="Contact Form is valid, message included",
        )

    def test_contact_form_submission_success(self):
        form_data = {"name": "Bob", "email": "test@test.com",
                     "message": "Hello!"}
        response = self.client.post(reverse("about"),
                                    data=form_data, follow=True)

        self.assertEqual(response.status_code, 200)
        self.assertContains(
            response, "Your message has been sent. We'll be in touch soon")

    def test_contact_form_submission_invalid(self):
        form_data = {"name": "", "email": "test@test.com",
                     "message": "Hello!"}
        response = self.client.post(reverse("about"), data=form_data)

        self.assertEqual(response.context["contact_form"].data["email"],
                         "test@test.com")

    def test_form_data_retained_on_invalid_post(self):
        form_data = {"name": "", "email": "test@test.com", "message": "Hello!"}
        response = self.client.post(reverse("about"), data=form_data)
        self.assertEqual(response.context["contact_form"].data["email"],
                         "test@test.com")

    def test_invalid_contact_form_shows_errors(self):
        form_data = {"name": "", "email": "", "message": ""}
        response = self.client.post(reverse("about"), data=form_data)
        self.assertFormError(response, "contact_form", "name",
                             "This field is required.")
