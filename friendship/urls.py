from django.urls import path
from .views import UserListView, RequestView,RequestListView


urlpatterns = [
    path('users-list/', UserListView.as_view()),
    path('request/', RequestView.as_view()),
    path('requests-list/', RequestListView.as_view()),
    # path('accept/'),
    # path('friends/'),
]

