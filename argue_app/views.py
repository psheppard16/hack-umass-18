from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

from argue_app.models import *
from argue_app.forms import *
from argue_app.serializers import *
from django.urls import reverse

import logging
log = logging.getLogger('argue')

###########################################################################
#                                ARGUE VIEWS                              #
#                                                                         #
###########################################################################


def HomeView(request):
    context = {'title': "Home",
               'user': request.user
               }
    return render(request, 'pages/home.html', context)


def ChatView(request):
    context = {'title': "Chat",
               'user': request.user
               }
    return render(request, 'pages/chat.html', context)


def LoginView(request):
    context = {'title': "Login",
               'user': request.user
               }
    return render(request, 'pages/login.html', context)


def ProfileView(request):
    context = {'title': "Profile",
               'user': request.user
               }
    return render(request, 'pages/profile.html', context)


def ErrorView(request):
    context = {'title': "Error",
               }
    return render(request, 'shared/error.html', context)