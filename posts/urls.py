from django.urls import path
from .views import PostView, PostListView, CommentView, LikeView


urlpatterns = [
    path('post', PostView.as_view() , name = 'post'),
    path('post/<int:post_pk>/', PostView.as_view(), name = 'post'),
    path('post_list', PostListView.as_view(), name = 'post_list'),
    path('post/<int:post_pk>/comments', CommentView.as_view(), name='comment'),
    path('post/<int:post_pk>/likes', LikeView.as_view(), name='like'),
    ]
 