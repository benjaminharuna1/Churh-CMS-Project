import re
from django.urls import path, re_path
from member import views
from .views import *


# app_name = "member"

urlpatterns = [
    path('', views.index, name='home'),
    path('member/list/', views.MemberListView.as_view(), name=('member-list')),

    # path("profile/<int:pk>", views.MemberDetailView.as_view(), name="profile"),
    path('member/profile/<int:pk>', views.member_profile, name=('profile')),
    path('member/profile/edit-member', views.edit_member_profile, name=('edit-member')),
    # path('member/add-member/', views.create_member, name=('add-member')),
    path('member/add-member/', AddMemberView.as_view(), name='add-member'),

    re_path(r'^.*\.*', views.pages, name='pages'),

]