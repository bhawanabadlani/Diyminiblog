from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('blogs/', views.BlogPostListView.as_view(), name='blogs'),
    path('blogs/<int:pk>', views.BlogPostDetailView.as_view(), name='blogpost-detail'),
    path('bloggers/', views.AuthorListView.as_view(), name='authors'),
    path('bloggers/<int:pk>', views.AuthorDetailView.as_view(), name='author-detail'),
    path('<int:pk>/create', views.add_comment, name='comment'),
]