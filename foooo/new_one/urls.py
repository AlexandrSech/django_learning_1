from django.urls import path, include
from .views import hello, new, create_user, CreateUserView, UsersListView, user
from .viewsets import MyUsersListView, MyUsersViewSet


from rest_framework.routers import DefaultRouter

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'users', MyUsersViewSet, basename="users")
router.register(r'users', MyUsersViewSet, basename="users")
router.register(r'users', MyUsersViewSet, basename="users")
router.register(r'users', MyUsersViewSet, basename="users")
router.register(r'users', MyUsersViewSet, basename="users")
router.register(r'users', MyUsersViewSet, basename="users")


urlpatterns = [
    path('hello', hello),
    path('new', new),
    path('create_user', create_user, name="create_user"),
    path('create_user2', CreateUserView.as_view()),
    path('users/list', UsersListView.as_view(), name="users_list"),
    path('users/list/<int:user_id>/profile', UsersListView.as_view(), name="users_list"),
    path('user', user, name="user"),
    path("users_list/", MyUsersListView.as_view()),
    path('', include(router.urls)),
]
