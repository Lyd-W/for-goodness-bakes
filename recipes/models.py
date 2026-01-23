from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = (
    (0, "Draft"),
    (1, "Published"),
)

DIFFICULTY_LEVELS = (
    (1, "Easy"),
    (2, "Medium"),
    (3, "Hard"),
)


class Recipe(models.Model):
    title = models.CharField(max_length=150, unique=True)
    slug = models.SlugField(max_length=150, unique=True)
    image = CloudinaryField("image")
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="recipes"
    )
    created_on = models.DateTimeField(auto_now_add=True)
    description = models.TextField()
    ingredients = models.TextField()
    prep_time = models.PositiveIntegerField()
    cook_time = models.PositiveIntegerField()
    method = models.TextField()
    servings = models.PositiveIntegerField()
    difficulty = models.PositiveIntegerField(choices=DIFFICULTY_LEVELS)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title


class Comment(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="comments"
    )
    comment_on = models.ForeignKey(
        Recipe, on_delete=models.CASCADE, related_name="comments"
    )
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    edited_on = models.DateTimeField(auto_now=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"Comment on {self.comment_on} by {self.author}"
