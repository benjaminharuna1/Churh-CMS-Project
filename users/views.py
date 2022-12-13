# from django.shortcuts import render, redirect

# from django.http import JsonResponse

# from django.contrib import messages
# from django.contrib.auth import authenticate, login, logout

# from django.contrib.auth.models import User

# from .forms import UserForm, SignupForm
# from .models import UserProfile

# from member.models import *




# def login_user(request):
#     template = "accounts/login.html"
#     form = UserForm()
#     context = {"form": form}
#     return render(request, template, context)


# def _logout(request):
#     user = request.user
#     logout(request)
#     return redirect("login_user")


# def _login(request):
#     if request.method == "POST":
#         # import pdb; pdb.set_trace()
#         form = UserForm(request.POST or None)
#         if form.is_valid():

#             username = form.cleaned_data.get("username")
#             password = form.cleaned_data.get("password")

#             next_url = request.POST.get("next") or "home"

#             user = authenticate(username=username, password=password)

#             if user is not None:
#                 login(request, user)
#                 # import pdb; pdb.set_trace()
#                 if next_url:
#                     return redirect(next_url)
#                 else:
#                     return redirect("home")
#             else:
#                 messages.error(request, "Invalid Username or Password")
#                 return redirect(next_url)


# def signup(request):
#     template = "accounts/register.html"
#     form = SignupForm()
#     context = {"form": form}
#     return render(request, template, context)


# def signup_user(request):
#     if request.method == "POST":
#         form = SignupForm(request.POST or None)

#         username = request.POST.get("username")
#         email = request.POST.get("email")

#         try:
#             user = User.objects.get(username=username)
#             user2 = User.objects.get(email=email)
#         except:
#             user = None
#             user2 = None

#         if user is not None:
#             messages.error(request, "User with that name already exists")
#             return redirect("login_user")

#         if user2 is not None:
#             # import pdb; pdb.set_trace()
#             messages.error(request, "User with that email already exists")
#             return redirect("login_user")

#         if form.is_valid():
#             form.save()
#             return redirect("home")
#         else:
#             import pdb; pdb.set_trace()
#             messages.error(request, "Password Validation Error")
#             return redirect("login_user")


# def user_profile(request):
#     # SLTGhana = 030 223 1886
#     template = "home/profile.html"
#     profile = UserProfile.objects.get_or_create(user=request.user)
#     try:
#         homecell = HomeCell.objects.get(name=request.user.username)
#         members = homecell.member_set.active()
#         # import pdb; pdb.set_trace()
#     except:
#         homecell = None
#         members = None
#     # import pdb; pdb.set_trace()
#     context = {"profile": profile, "members": members, "homecell": homecell}
#     return render(request, template, context)


# def login_api(request):
#     if request.method == "POST":
#         form = UserForm(request.POST or None)
#         if form.is_valid():
#             username = form.cleaned_data.get("username")
#             password = form.cleaned_data.get("password")
#             user = authenticate(username=username, password=password)

#             if user is not None:
#                 if user.is_active:
#                     login(request, user)
#                     response = {"STATUS": "OK", "USER_ID": user.pk}
#                     return JsonResponse(response, content_type="Application/json", safe=False)
#                 else:
#                     response = {"STATUS": "INACTIVE"}
#                     return JsonResponse(response, content_type="Application/json", safe=False)
#             else:
#                 response = {"STATUS": "INVALID USER CREDENTIALS", "CODE": -1}
#                 return JsonResponse(response, content_type="Application/json", safe=False)

#         else:
#             response = {"STATUS": "VALIDATION ERROR"}
#             return JsonResponse(response, content_type="Application/json", safe=False)


# def signup_api(request):
#     if request.method == "POST":
#         form = SignupForm(request.POST or None)
#         if form.is_valid():
#             form.save()
#             response = {"STATUS": "OK", "CODE": 0}
#             return JsonResponse(response, content_type="Application/json", safe=False)
#         else:
#             response = {"STATUS": "ERROR", "CODE": -1}
#             return JsonResponse(response, content_type="Application/json", safe=False)

# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import LoginForm, SignUpForm


def login_view(request):
    form = LoginForm(request.POST or None)

    msg = None

    if request.method == "POST":

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("/")
            else:
                msg = 'Invalid credentials'
        else:
            msg = 'Error validating the form'

    return render(request, "accounts/login.html", {"form": form, "msg": msg})

def logout_user(request):
    user = request.user
    logout(request)
    messages.success(request, ("You are logged out successfully"))
    return redirect("login")
    

def register_user(request):
    msg = None
    success = False

    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)

            msg = 'User created - please <a href="/login">login</a>.'
            success = True

            # return redirect("/login/")

        else:
            msg = 'Form is not valid'
    else:
        form = SignUpForm()

    return render(request, "accounts/register.html", {"form": form, "msg": msg, "success": success})


