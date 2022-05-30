from django.urls import path
from .views import post_view, like_post

app_name = 'likes'

urlpatterns = [
  path('', post_view, name='post-list'),
  path('likes/', like_post, name='like-post'),
]