from django.test import TestCase
from .forms import ContactForm


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
