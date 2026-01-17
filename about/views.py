from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.views import generic
from .models import About
from .forms import ContactForm

def AboutPage(request):
    about = About.objects.all().order_by('-updated_on').first()
    
    if request.method == "POST":
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            contact_form.save()
            messages.add_message(
                request, messages.SUCCESS,
                "Your message has been sent. We'll be in touch soon"
            )
    
    contact_form = ContactForm()
  
    return render(
        request,
        "about/about.html",
        {
            "about": about,
            "contact_form": contact_form,
         }
        
    )
