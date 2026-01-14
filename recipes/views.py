from django.shortcuts import render
from django.views import generic
from .models import Recipe

# Create your views here.

class RecipeList(generic.ListView):
    queryset = Recipe.objects.all()
    context_object_name = "recipes"
    template_name = "recipes/index.html"
    paginate_by = 6