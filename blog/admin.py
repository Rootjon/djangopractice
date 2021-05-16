from django.contrib import admin

from .models import Post

# Register your models here.
class PostAdmin(admin.ModelAdmin):

    list_display = [
        'title',
        'description',
        'short_description',
        'thumbnail',
        'creation',

    ]
admin.site.register(Post, PostAdmin)