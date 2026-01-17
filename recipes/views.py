from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib import messages
from .models import Recipe
from .forms import CommentForm

# Create your views here.
class RecipeList(generic.ListView):
    queryset = Recipe.objects.filter(status=1).order_by("created_on")
    context_object_name = "recipes"
    template_name = "recipes/index.html"
    paginate_by = 6
    
def recipe_detail(request, slug):
    queryset = Recipe.objects.filter(status=1)
    recipe = get_object_or_404(queryset, slug=slug)
    comments = recipe.comments.filter(approved=True).order_by("-created_on")
    comment_count = recipe.comments.filter(approved=True).count()
    
    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.comment_on = recipe
            comment.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Your comment has been successfully submitted and is awaiting approval'
            )
        
    comment_form = CommentForm()
    
    return render(
        request,
        "recipes/recipe_detail.html",
        {
            "recipe": recipe,
            "comments": comments,
            "comment_count": comment_count,
            "comment_form": comment_form,
         },
    )
