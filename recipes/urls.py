from . import views
from django.urls import path

urlpatterns = [
    path('home/', views.RecipeList.as_view(), name='home'),
    path('<slug:slug>/', views.recipe_detail, name='recipe_detail'),
]