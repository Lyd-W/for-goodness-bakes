from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from recipes.models import Recipe, Comment


class TestCommentPermissions(TestCase):

    def setUp(self):
        self.author = User.objects.create_user(
            username="User1", password="pass123"
        )
        self.other_user = User.objects.create_user(
            username="User2", password="pass123"
        )

        self.recipe = Recipe.objects.create(
            title="Chocolate Cake",
            slug="chocolate-cake",
            author=self.author,
            description="Tasty",
            ingredients="Chocolate",
            prep_time=10,
            cook_time=30,
            method="Bake",
            servings=4,
            difficulty=1,
            status=1,
            image="placeholder"
        )

        self.comment = Comment.objects.create(
            author=self.author,
            comment_on=self.recipe,
            content="Original comment",
            approved=True
        )

    def test_comment_author_can_edit(self):
        self.client.login(username="User1", password="pass123")

        url = reverse(
            "comment_editing",
            args=[self.recipe.slug, self.comment.id]
            )

        response = self.client.post(url, {
            "content": "Updated comment"
            })

        self.comment.refresh_from_db()

        self.assertEqual(self.comment.content, "Updated comment")
        self.assertEqual(response.status_code, 302)

    def test_comment_author_can_delete(self):
        self.client.login(username="User1", password="pass123")

        url = reverse(
            "comment_delete",
            args=[self.recipe.slug, self.comment.id]
        )

        response = self.client.post(url)

        self.assertFalse(
            Comment.objects.filter(id=self.comment.id).exists()
        )
        self.assertEqual(response.status_code, 302)

    def test_non_author_cannot_edit_comment(self):
        self.client.login(username="User2", password="pass123")

        url = reverse(
            "comment_editing",
            args=[self.recipe.slug, self.comment.id]
        )

        response = self.client.post(url, {
            "content": "Changed comment"
        })

        self.comment.refresh_from_db()

        self.assertNotEqual(self.comment.content, "Changed comment")
        self.assertEqual(self.comment.content, "Original comment")
        self.assertEqual(response.status_code, 302)

    def test_non_author_cannot_delete_comment(self):
        self.client.login(username="User2", password="pass123")

        url = reverse(
            "comment_delete",
            args=[self.recipe.slug, self.comment.id]
        )

        response = self.client.post(url)

        self.assertTrue(
            Comment.objects.filter(id=self.comment.id).exists()
        )
        self.assertEqual(response.status_code, 302)

    def test_logged_out_user_cannot_edit_comment(self):
        url = reverse(
            "comment_editing",
            args=[self.recipe.slug, self.comment.id]
        )

        response = self.client.post(url, {
            "content": "Nope"
        })

        self.comment.refresh_from_db()
        self.assertEqual(self.comment.content, "Original comment")
        self.assertEqual(response.status_code, 302)

    def test_logged_out_user_cannot_delete_comment(self):
        url = reverse(
            "comment_delete",
            args=[self.recipe.slug, self.comment.id]
        )

        response = self.client.post(url)

        self.assertTrue(
            Comment.objects.filter(id=self.comment.id).exists()
        )
        self.assertEqual(response.status_code, 302)
