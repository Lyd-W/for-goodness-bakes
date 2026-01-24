from django.contrib.auth.models import User
from django.urls import reverse
from django.test import TestCase
from .forms import CommentForm
from .models import Recipe


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
        response = self.client.get(reverse("recipe_detail",
                                           args=["recipe-title"]))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Recipe title", response.content)
        self.assertIn(b"Recipe description", response.content)
        self.assertIsInstance(response.context["comment_form"], CommentForm)
