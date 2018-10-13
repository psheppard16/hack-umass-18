from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

from dog_app.models import *
from dog_app.forms import *
from dog_app.serializers import *
from django.urls import reverse

import logging
log = logging.getLogger('dog')

###########################################################################
#                             Dog VIEWS                           #
#                                                                         #
###########################################################################


# def HomeView(request):
#     context = {'title': "Home",
#                'user': request.user
#                }
#     return render(request, 'pages/home.html', context)