from django.contrib import admin
from .models import Post 


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('uuid', 'caption', 'author', 'date_added')
    list_filters = ('author', 'date_added')
    fields = ['uuid', 'author', 'caption', 'text', 'picture']


