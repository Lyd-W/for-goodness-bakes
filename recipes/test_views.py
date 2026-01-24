from django.contrib.auth.models import User
from django.urls import reverse
from django.test import TestCase
from .forms import CommentForm
from .models import Recipe
from django.contrib.messages import get_messages


class TestRecipeViews(TestCase):

    def setUp(self):
        self.user = User.objects.create_superuser(
            username="myUsername", password="myPassword", email="test@test.com"
        )
        self.recipe = Recipe(
            title="Recipe title",
            author=self.user,
            slug="recipe-title",
            description="Recipe description",
            status=1,
            ingredients="ingredients",
            prep_time="1",
            cook_time="1",
            method="method",
            servings="1",
            difficulty="1",
        )

        self.recipe.save()

    def test_render_recipe_detail_page_with_comment_form(self):
        response = self.client.get(
            reverse("recipe_detail", args=["recipe-title"])
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Recipe title", response.content)
        self.assertIn(b"Recipe description", response.content)
        self.assertIsInstance(response.context["comment_form"], CommentForm)

    def test_comment_submission_success(self):
        self.client.login(username="myUsername", password="myPassword")
        recipe_data = {"content": "This is a test"}
        response = self.client.post(
            reverse("recipe_detail", args=["recipe-title"]),
            recipe_data,
            follow=True,
        )
        self.assertEqual(response.status_code, 200)

        self.assertTrue(
            self.recipe.comments.filter(content="This is a test").exists()
        )

        messages = list(get_messages(response.wsgi_request))
        self.assertTrue(
            any(
                "Your comment has been submitted and is awaiting approval"
                in str(m)
                for m in messages
            )
        )

    def test_commenting_signed_out(self):
        recipe_data = {"content": "This is a test"}
        response = self.client.post(
            reverse("recipe_detail", args=["recipe-title"]),
            recipe_data,
            follow=True
        )
        self.assertEqual(response.status_code, 200)

        self.assertFalse(
            self.recipe.comments.filter(content="This is a test").exists()
        )
