from django.urls import path
from blogapp.apps import BlogappConfig
from blogapp.views import BlogPostsListView, BlogPostsCreateView, BlogPostsDetailView, BlogPostsUpdateView, \
    BlogPostsDeleteView

app_name = BlogappConfig.name

urlpatterns = [
    path('blog/', BlogPostsListView.as_view(), name='posts_list'),
    path('blog/posts_form/', BlogPostsCreateView.as_view(), name='posts_form'),
    path('blog/posts_details/<int:pk>/', BlogPostsDetailView.as_view(), name='posts_details'),
    path('blog/<int:pk>/edit/', BlogPostsUpdateView.as_view(), name='post_edit'),
    path('blog/<int:pk>/delete/', BlogPostsDeleteView.as_view(), name='posts_delete'),
]