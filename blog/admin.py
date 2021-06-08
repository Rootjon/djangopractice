from django.contrib import admin

from .models import Post, Comment

from django_summernote.admin import SummernoteModelAdmin
# Register your models here.
class PostAdmin(SummernoteModelAdmin):

    list_display = [
        'title',
        'description',
        'short_description',
        'thumbnail',
        'creation',
        

    ]

    summernote_fields = ('description')
admin.site.register(Post, PostAdmin)


class CommentAdmin(admin.ModelAdmin):
    
    list_display = [
        'name',
        'body',
      
    ]
admin.site.register(Comment, CommentAdmin)
