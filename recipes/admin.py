from django.contrib import admin
from .models import Recipe, Comment
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Recipe)
class RecipeAdmin(SummernoteModelAdmin):

    list_display = (
        "title",
        "author",
        "difficulty",
        "prep_time",
        "cook_time",
        "status",
        "created_on",
    )

    search_fields = ["title", "description", "ingredients"]
    list_filter = ("status", "difficulty", "created_on")

    prepopulated_fields = {"slug": ("title",)}

    summernote_fields = (
        "description",
        "ingredients",
        "method",
    )


admin.site.register(Comment)
