from django.urls import path
from .views import hello, new, create_user, CreateUserView, UsersListView, user

urlpatterns = [
    path('', hello),
    path('new', new),
    path('create_user', create_user, name="create_user"),
    path('create_user2', CreateUserView.as_view()),
    path('users/list', UsersListView.as_view(), name="users_list"),
    path('user', user, name="user"),
]
