from django.urls import path
from .views import register, login_view, profile, logout_view

urlpatterns = [
    path("register/", register, name="register"),
    path("login/", login_view, name="login"),
    path("profile/", profile, name="profile"),
    path("logout/", logout_view, name="logout"),
]
