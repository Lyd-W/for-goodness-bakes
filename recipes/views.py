from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Recipe, Comment
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
    comments = recipe.comments.all().order_by("-created_on")
    comment_count = recipe.comments.filter(approved=True).count()

    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.comment_on = recipe
            comment.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                "Your comment has been submitted and is awaiting approval",
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


def comment_editing(request, slug, comment_id):

    if request.method == "POST":

        queryset = Recipe.objects.filter(status=1)
        recipe = get_object_or_404(queryset, slug=slug)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.author == request.user:
            comment = comment_form.save(commit=False)
            comment.comment_on = recipe
            comment.approved = False
            comment.save()
            messages.add_message
            (
                request,
                messages.SUCCESS,
                "Your comment has been successfully updated.",
            )
        else:
            messages.add_message
            (
                request,
                messages.ERROR,
                "Oh dear, your comment was not updated. Please try again.",
            )

    return HttpResponseRedirect(reverse("recipe_detail", args=[slug]))


def comment_delete(request, slug, comment_id):

    queryset = Recipe.objects.filter(status=1)
    recipe = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id, comment_on=recipe)

    if comment.author == request.user:
        comment.delete()
        messages.add_message(
            request,
            messages.SUCCESS,
            "Your comment has been successfully removed!",
        )
    else:
        messages.add_message(
            request, messages.ERROR, "Sorry, that slice doesn't belong to you"
        )

    return HttpResponseRedirect(reverse("recipe_detail", args=[slug]))
