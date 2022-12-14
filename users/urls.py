# from django.urls import path

# from .views import _login, login_user, _logout, signup, signup_user, user_profile, login_api


# urlpatterns = [
#     # Login URLConfs
#     path("login/", login_user, name="login_user"),
#     path("_login_/", _login, name="_login"),
#     path('logout/', _logout, name="_logout"),
#     path('profile/', user_profile, name="user_profile"),

#     # Api Login View Function
#     path("login_api/", login_api, name="login_api"),

#     # Signup URLConfs
#     path("signup/", signup, name="signup"),
#     path("signup_user/", signup_user, name="signup_user"),
# ]


# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path
from .views import login_view, register_user, logout_user
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', login_view, name="login"),
    path('register/', register_user, name="register"),
    path("logout/", logout_user, name="logout")
    
]
