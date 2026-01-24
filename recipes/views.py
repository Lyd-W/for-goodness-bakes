from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from django.views import generic
from django.contrib import messages
from .models import Recipe, Comment
from .forms import CommentForm


# Create your views here.
class RecipeList(generic.ListView):
    queryset = Recipe.objects.filter(status=1).order_by("created_on")
    context_object_name = "recipes"
    template_name = "recipes/index.html"
    paginate_by = 6


def recipe_detail(request, slug):
    recipe = get_object_or_404(Recipe, slug=slug, status=1)

    if request.user.is_authenticated:
        comments = recipe.comments.filter(
            Q(approved=True) | Q(author=request.user)
            ).order_by("-created_on")
    else:
        comments = recipe.comments.filter(approved=True
                                          ).order_by("-created_on")

    comment_count = recipe.comments.filter(approved=True).count()

    comment_form = CommentForm()

    if request.method == "POST":
        if not request.user.is_authenticated:
            messages.error(request, "You need to log in to leave a comment")
            return redirect("recipe_detail", slug=recipe.slug)

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
    if not request.user.is_authenticated:
        messages.error(request, "You need to be logged in to edit comments")
        return redirect("recipe_detail", slug=slug)

    recipe = get_object_or_404(Recipe, slug=slug, status=1)
    comment = get_object_or_404(Comment, pk=comment_id, comment_on=recipe)

    if comment.author != request.user:
        messages.error(request, "That's not your cake to decroate")
        return redirect("recipe_detail", slug=slug)

    if request.method == "POST":
        comment_form = CommentForm(data=request.POST, instance=comment)
        if comment_form.is_valid() and comment.author == request.user:
            comment = comment_form.save(commit=False)
            comment.comment_on = recipe
            comment.approved = False
            comment.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                "Your comment has been successfully updated.",
            )
        else:
            messages.add_message(
                request,
                messages.ERROR,
                "Oh dear, your comment was not updated. Please try again.",
            )

    return redirect("recipe_detail", slug=slug)


def comment_delete(request, slug, comment_id):
    if not request.user.is_authenticated:
        messages.error(request, "You must be logged in to delete comments")
        return redirect("recipe_detail", slug=slug)

    recipe = get_object_or_404(Recipe, slug=slug, status=1)
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

    return redirect("recipe_detail", slug=slug)
