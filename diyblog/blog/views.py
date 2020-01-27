from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse, HttpResponseRedirect
from blog.models import BlogPost, Comment, Author
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from blog.forms import AddComment
from django.shortcuts import get_object_or_404
from django.urls import reverse

# Create your views here.
def index(request):
    """View function for homepage site"""

    # Generate account for some of the main objects
    num_blogpost = BlogPost.objects.all().count()
    num_bloggers = Author.objects.all().count()
    num_users = User.objects.all().count()
    context = {
        'num_blogpost': num_blogpost,
        'num_bloggers': num_bloggers,
        'num_users': num_users,
    }
    # Render the HTML template with the data in the context variable
    return render(request, 'blog/index.html', context=context)

@login_required
def add_comment(request, pk):
    blogpost = get_object_or_404(BlogPost, pk=pk)
    #  If this is a POST request then process the Form data
    if request.method == 'POST':
        # Create a form instance and populate it with data from the request (binding):
        form = AddComment(request.POST)
        comment = Comment()
        comment.blog_post = blogpost
        comment.comment_by = request.user
        # Check if the form is valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required (here we just write it to 
            # the model due_back field)
            comment.text = form.cleaned_data['added_comment']
            comment.save()

             # redirect to a new URL:
            return HttpResponseRedirect(reverse('blogpost-detail', args=[pk]))

    else:
        comment = ''
        form = AddComment(initial={'comment': comment})
    context = {
        'form': form,
        'comment': comment,
    }
    return render(request, 'blog/comment.html', context)


class BlogPostListView(generic.ListView):
    model = BlogPost
    paginate_by = 5

class BlogPostDetailView(generic.DetailView):
    model = BlogPost

class AuthorDetailView(generic.DetailView):
    model = Author

class AuthorListView(generic.ListView):
    model = Author
