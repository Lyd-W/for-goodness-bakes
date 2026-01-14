from django.shortcuts import render
from django.views import generic
from .models import Recipe

# Create your views here.

class RecipeList(generic.ListView):
    queryset = Recipe.objects.filter(status=1).order_by("created_on")
    context_object_name = "recipes"
    template_name = "recipes/index.html"
    paginate_by = 6