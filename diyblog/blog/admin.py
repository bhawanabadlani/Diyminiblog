from django.contrib import admin
from .models import BlogPost, Comment, Author
# Register your models here.

class CommentInline(admin.TabularInline):
    model = Comment

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'post_date', 'author')
    inlines = [CommentInline]
admin.site.register(Author)