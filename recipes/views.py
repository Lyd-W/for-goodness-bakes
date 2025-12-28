from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def recipes_list(request):
    return HttpResponse("Lets get baking!")