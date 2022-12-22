# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import *
from .models import *

from users.models import UserProfile



@login_required(login_url="/login/")
def index(request):
    context = {'segment': 'index'}

    html_template = loader.get_template('home/index.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template

        html_template = loader.get_template(('' or 'home/') + load_template) 
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))

    

class MemberListView(ListView):
    model: Membership
    template_name = 'members/list.html'
    def get_context_data(self, **kwargs):
        context = super(MemberListView, self).get_context_data(**kwargs)
        context.update({
            "home_cell": HomeCell.objects.order_by('name'),
        })
        return context

    def get_queryset(self):
        return Membership.objects.order_by('ID')

         
# @login_required(login_url="/login/")
# def member_profile(request,):
#     template = "members/profile.html"
#     membership = Membership.objects.active()
#     member_sugroup = MemberSubGroup.objects.all()
#     home_cell = HomeCell.objects.all()
#     member_committee = MemberCommittee.objects.all()
#     employment_details = EmploymentDetails.objects.all()
#     education_information = EducationInformation.objects.all()
#     profile = UserProfile.objects.get_or_create(user=request.user)
#     context = {
#         "profile": profile,
#         "membership": membership, "member_sugroup": member_sugroup, "home_cell": home_cell, "member_committee": member_committee, "employment_details": employment_details, "education_information": education_information, "total": len(membership),
#         "total_active": len(Membership.objects.active()),
#         "total_delete": len(membership),
#         "status": "all"
#     }
#     return render(request, template, context)


@login_required(login_url="/login/")
def member_profile(request, pk):
    template = "members/profile.html"
    membership = get_object_or_404(Membership, pk=pk)
    member_sugroup = MemberSubGroup.objects.all()
    home_cell = HomeCell.objects.all()
    member_committee = MemberCommittee.objects.all()
    employment_details = EmploymentDetails.objects.all()
    education_information = EducationInformation.objects.all()
    profile = UserProfile.objects.get_or_create(user=request.user)
    context = {
        "profile": profile,
        "membership": membership, "member_sugroup": member_sugroup, "home_cell": home_cell, "member_committee": member_committee, "employment_details": employment_details, "education_information": education_information, 
        # "total": len(membership),
        # "membership": len(Membership.objects.active()),
        # "total_delete": len(membership),
        "status": "all"
    }
    return render(request, template, context)




@login_required(login_url="/login/")
def create_member(request):
    template = "members/create.html"
    context = {}
    return render(request, template, context)


@login_required(login_url="/login/")
def edit_member_profile(request):
    template = "members/edit.html"
    context = {}
    return render(request, template, context)


@login_required(login_url="/login/")
def confirm_delete_member(request):
    template = "members/create.html"
    context = {}
    return render(request, template, context)

