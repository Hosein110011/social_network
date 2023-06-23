from django.urls import path
from .views import (
    UserListView, RequestView,RequestListView, AcceptView
    ,FriendListView
)

urlpatterns = [
    path('users-list/', UserListView.as_view()),
    path('request/', RequestView.as_view()),
    path('requests-list/', RequestListView.as_view()),
    path('accept/', AcceptView.as_view()),
    path('friends/', FriendListView.as_view()),
]

