from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post, Comment

@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    """
    renders all instances of :model:`blog.Post` in the Admin panel

    Blog posts are sorted by their 'status' and date of creation.
    Summernote editor is loaded for editing and completing the 'content' section.

    """
    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title', 'content']
    list_filter = ('status', 'created_on')
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)

# Register your models here.

admin.site.register(Comment)
    """
    Renders all instances of :model:`blog.Comment` in the Admin panel
    """