from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Recipe

# Create your views here.
class RecipeList(generic.ListView):
    queryset = Recipe.objects.filter(status=1).order_by("created_on")
    context_object_name = "recipes"
    template_name = "recipes/index.html"
    paginate_by = 6
    
def recipe_detail(request, slug):
    queryset = Recipe.objects.filter(status=1)
    recipe = get_object_or_404(queryset, slug=slug)
    
    return render(
        request,
        "recipes/recipe_detail.html",
        {"recipe": recipe},
    )
