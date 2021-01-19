from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView
from . import views

urlpatterns = [
    path("", views.home, name="blog_home"),
    path("blog/", PostListView.as_view(), name="actually_blog"),
    path("post/<int:pk>", PostDetailView.as_view(), name="post-detail"),
    path("post/new", PostCreateView.as_view(), name="post-create"),
    path("about/", views.about, name="blog_about"),
]