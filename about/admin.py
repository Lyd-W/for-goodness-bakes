from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import About

@admin.register(About)
class AboutAdmin(SummernoteModelAdmin):

    list_display = (
        'title',
        'author',
        'status',
        'created_on',
    )

    search_fields = ['title']
    list_filter = ('status', 'created_on')

    prepopulated_fields = {'slug': ('title',)}

    summernote_fields = (
        'content',
    )