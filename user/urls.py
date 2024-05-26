from django.urls import path

from . import views


urlpatterns = [
    path("register/", views.register, name="register"),
    path("login/", views.login, name="login"),
    path("test-token/", views.test_token, name="test_token"),
    path("get-all/", views.get_all, name="get_all"),
    path("get-me/", views.get_me, name="get_me"),
    path("logout/", views.logout, name="logout"),
    path("edit-user/<int:id>/", views.edit_user, name="edit_user"),
    path("delete-user/<int:id>/", views.delete_user, name="delete_user"),
    path("create-user/", views.create_user, name="create_user"),
    path("get-user/<int:id>/", views.get_user_id, name="get_user_id")
]
