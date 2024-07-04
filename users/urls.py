from django.urls import path
from django.contrib.auth.views import LogoutView
from users import views

urlpatterns = [
    path("login/", views.login, name="login"),
    path("register/", views.register, name="register"),
    path("logout/", LogoutView.as_view(template_name="users/logout.html"), name="logout"),
    path("profile/", views.profile, name="profile"),
    path("profile/edit/", views.edit_profile, name="edit_profile"),
    path("profile/edit/password/", views.ChangePasswordView.as_view(), name="change_password"),
    path("profile/edit/password/success", views.password_success, name="password_success")
]
