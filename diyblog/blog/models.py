from django.utils import timezone
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100, null=True)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField(null=True, blank=True)
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def get_absolute_url(self):
        return reverse('author-detail', args=[str(self.id)])

        
class BlogPost(models.Model):
    author = models.ForeignKey(
        Author,
        help_text="Name of the author",
        on_delete=models.SET_NULL,
        null = True
    )
    title = models.CharField(
        max_length=200, 
        help_text="Title of the blog"
    )
    content = models.TextField(
        "Description",
        help_text="Write here!",
    )
    post_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blogpost-detail', args=[str(self.id)])

    class Meta:
        ordering = ['-post_date',]


class Comment(models.Model):
    blog_post = models.ForeignKey(
        BlogPost, 
        on_delete=models.CASCADE, 
        null=True, 
    )
    comment_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null = True,
    )
    text = models.TextField()
    pub_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.blog_post.title

    class Meta:
        ordering = ['pub_date',]


