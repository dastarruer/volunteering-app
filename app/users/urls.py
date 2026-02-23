from django.contrib.auth import views as auth_views
from django.urls import path

from . import views

app_name = "users"

urlpatterns = [
    path("login/", auth_views.LoginView.as_view(), name="login"),
    path("register/", views.register, name="register"),
    path("profile/", views.profile, name="profile"),
]
